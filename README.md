# Are Pretrained Bert Token Embeddings effective in the Transformer Translation Tasks?
(Work in progress)

## Bert (Pretrained) Token Embeddings*
| Models | # Vocab | # Dim | Notes |
|--|--|--|--|
|[bert-base-uncased](https://www.dropbox.com/s/kxs4c2q41lgm0re/bert-base-uncased.30522.768d.npz?dl=0) | 30,522 | 768 ||
|[bert-large-uncased](https://www.dropbox.com/s/86wlzjo3smyaq31/bert-large-uncased.30522.1024d.npz?dl=0) | 30,522 | 1024 ||
|[bert-base-cased](https://www.dropbox.com/s/jsuc73w1cowj8v4/bert-base-cased.28996.768d.npz?dl=0) | 28,996 | 768 ||
| [bert-large-cased](https://www.dropbox.com/s/kjaze0l0na71psp/bert-large-cased.28996.1024d.npz?dl=0) | 28,996 | 1024 ||
| [bert-base-multilingual-cased](https://www.dropbox.com/s/mwbcnync8tzjjxv/bert-base-multilingual-cased.119547.768d.npz?dl=0)| 119,547 | 768 | Not recommended |
|[bert-base-multilingual-uncased](https://www.dropbox.com/s/i2mhiurc3nw9vqd/bert-base-multilingual-uncased.105879.768d.npz?dl=0)| 30,522 | 768||
|[bert-base-chinese](https://www.dropbox.com/s/4hlhcheaddj20td/bert-base-chinese.21128.768d.npz?dl=0)|21,128 | 768 ||

\* If you are curious as to how to make these, check [extract.py](`extract.py`).<Br>
\** To see how to use those files, check [test.py](`test.py`).

##