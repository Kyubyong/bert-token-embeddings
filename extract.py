import torch
import numpy as np
np.set_printoptions(threshold=np.nan)
from multiprocessing import Pool
import re
from tqdm import tqdm

import os
os.system("pip install pytorch_pretrained_bert")
from pytorch_pretrained_bert import BertTokenizer, BertModel

def get_embeddings(mname):
    '''Gets pretrained embeddings of Bert-tokenized tokens or subwords
    mname: string. model name.
    '''
    print("# Model name:", mname)

    print("# Load pre-trained model tokenizer (vocabulary)")
    tokenizer = BertTokenizer.from_pretrained(mname)

    print("# Construct vocab")
    vocab = [token for token in tokenizer.vocab]

    print("# Load pre-trained model")
    model = BertModel.from_pretrained(mname)

    print("# Load word embeddings")
    emb = model.embeddings.word_embeddings.weight.data
    emb = emb.numpy()

    print("# Write")
    with open("{}.{}.{}d.vec".format(mname, len(vocab), emb.shape[-1]), "w") as fout:
        fout.write("{} {}\n".format(len(vocab), emb.shape[-1]))
        assert len(vocab)==len(emb), "The number of vocab and embeddings MUST be identical."
        for token, e in zip(vocab, emb):
            e = np.array2string(e, max_line_width=np.inf)[1:-1]
            e = re.sub("[ ]+", " ", e)
            fout.write("{} {}\n".format(token, e))

if __name__ == "__main__":
    mnames = (
              "bert-base-uncased",
              "bert-large-uncased",
              "bert-base-cased",
              "bert-large-cased",
              "bert-base-multilingual-cased",
              "bert-base-multilingual-uncased",
              "bert-base-chinese"
             )

    p = Pool(16)
    with tqdm(total=len(mnames)) as pbar:
        for _ in tqdm(p.imap(get_embeddings, mnames)):
            pbar.update()