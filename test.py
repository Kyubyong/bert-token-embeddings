import numpy as np
import glob

files = glob.glob('*npz')
for f in files:
    print(f)
    arrz = np.load(f)
    vocab, emb = arrz.files
    vocab, emb = arrz[vocab], arrz[emb]
    print(vocab.shape, emb.shape)