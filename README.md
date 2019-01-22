# Bert Pretrained Token Embeddings

BERT([BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)) yields pretrained token (=subword) embeddings. Let's extract and save them in the [word2vec](https://code.google.com/archive/p/word2vec/) format so that they can be used for downstream tasks.

## Requirements
* pytorch_pretrained_bert
* NumPy
* tqdm

## Extraction
* Check `extract.py`.

## Bert (Pretrained) Token Embeddings in word2vec format
| Models | # Vocab | # Dim | Notes |
|--|--|--|--|
|[bert-base-uncased](https://dl.dropboxusercontent.com/s/hcj1oh8ltqhqrk4/bert-base-uncased.30522.768d.vec.tar.gz) | 30,522 | 768 ||
|[bert-large-uncased](https://dl.dropboxusercontent.com/s/kdf932v3taa22zp/bert-large-uncased.30522.1024d.vec.tar.gz) | 30,522 | 1024 ||
|[bert-base-cased](https://dl.dropboxusercontent.com/s/7wb92gvc40jxvz9/bert-base-cased.28996.768d.vec.tar.gz) | 28,996 | 768 ||
| [bert-large-cased](https://dl.dropboxusercontent.com/s/ke68kjw7yui39s7/bert-large-cased.28996.1024d.vec.tar.gz) | 28,996 | 1024 ||
| [bert-base-multilingual-cased](https://dl.dropboxusercontent.com/s/kmyh9cxmu6hb1jx/bert-base-multilingual-cased.119547.768d.vec.tar.gz)| 119,547 | 768 | Recommended |
|[bert-base-multilingual-uncased](https://dl.dropboxusercontent.com/s/j2vz6hue7pze0ae/bert-base-multilingual-uncased.105879.768d.vec.tar.gz)| 30,522 | 768| Not recommended|
|[bert-base-chinese](https://dl.dropboxusercontent.com/s/gzb6kfjipw591vz/bert-base-chinese.21128.768d.vec.tar.gz)|21,128 | 768 ||

## Example
* Check `example.ipynb` to see how to load (sub-)word vectors with [gensim](https://github.com/RaRe-Technologies/gensim) and plot them in 2d space using [tSNE](https://lvdmaaten.github.io/tsne/). 

* Related tokens to <b>look</b><br>
<img src="look.png" width=1000>
* Related tokens to <b>##go</b><br>
<img src="go.png" width=1000>