#B. vectorize 3 words and check their similarity

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

A = 'architecture'
B = 'building'
C = 'city'

a = model.get_vector(A, norm=True)
b = model.get_vector(B, norm=True)
c = model.get_vector(C, norm=True)

ab_similarity = np.dot(a,b)
ac_similarity = np.dot(a,c)

print(f'Similarity between {A} and {B}: {ab_similarity}')
print(f'Similarity between {A} and {C}: {ac_similarity}')


