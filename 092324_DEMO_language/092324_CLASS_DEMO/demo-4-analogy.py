#E. compute an analogy : Find the word that is to A what C is to B

# 通过向量的加减运算，找到词之间的类似关系。
# 我们要找到一个词𝑋,它和“女王” (C) 有相似的关系

# c−b 表示“女人”与“男人”的关系向量
# 将这个关系向量加到“国王”的向量a上，得到的向量𝑎+𝑐−𝑏 就是我们要找的词向量
# 通过计算这个向量与词向量的相似度，找到最相似的词
# “国王 : 男人 :: 女王 : 女人” 的类比是正确的

# “巴黎 : 法国 :: 东京 : ？” --> 日本

import gensim
import logging
import os
import numpy as np
import math

from gensim.models import KeyedVectors
import gensim.downloader

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
this_dir = os.path.dirname(os.path.abspath(__file__))

model_name ='glove-wiki-gigaword-50'
model : KeyedVectors= gensim.downloader.load(model_name)

A = 'king'
B = 'man'
C = 'woman'

a = model.get_vector(A, norm=True)
b = model.get_vector(B, norm=True)
c = model.get_vector(C, norm=True)

analogy = a + (c-b) 

simis = model.similar_by_vector(analogy, topn=10)

print(f"the most similar words to analogy vector are:")
for s in simis:
    print(s)