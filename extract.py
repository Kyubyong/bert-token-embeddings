import torch
import numpy as np
from multiprocessing import Pool
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
    vocab = np.array([token for token in tokenizer.vocab])

    print("# Load pre-trained model")
    model = BertModel.from_pretrained(mname)

    print("# Load word embeddings")
    emb = model.embeddings.word_embeddings.weight.data
    emb = emb.numpy()

    print("# Write")
    fname = "{}.{}.{}d.npz".format(mname, len(vocab), emb.shape[-1])
    with open(fname, 'wb') as fout:
        np.savez(fout, vocab, emb)

if __name__ == "__main__":
    mnames = ("bert-base-uncased",
              "bert-large-uncased",
              "bert-base-cased",
              "bert-large-cased",
              "bert-base-multilingual-cased",
              "bert-base-multilingual-uncased",
              "bert-base-chinese")

    p = Pool(4)
    with tqdm(total=len(mnames)) as pbar:
        for _ in tqdm(p.imap(get_embeddings, mnames)):
            pbar.update()