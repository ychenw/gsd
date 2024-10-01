#C. find the most similar words to a given word

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

sims = model.most_similar(positive = 'architecture', negative='art', topn=10)

print(f"the most similar words to architecture are:")
for s in sims:
    print(s)
