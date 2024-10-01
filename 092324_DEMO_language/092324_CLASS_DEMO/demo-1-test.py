import gensim
# lib to access files on the system and for login
import logging
import os
import numpy as np
# math
import math

# gensim sub-liberaries, just import 1 thing from a package
from gensim.models import KeyedVectors
# can be found on the model website
import gensim.downloader

#these are needed to avoid SSL certificate error when downloading models from gensim api. Especially on MacOS
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#this is needed to display logging information when loading the model in case of an error
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#give info of where the file, standard python command 
this_dir = os.path.dirname(os.path.abspath(__file__))



model_name ='glove-wiki-gigaword-50'
model : KeyedVectors= gensim.downloader.load(model_name)

# print(model.vector_size)

word = 'architecture'

# in operator: to examine whether a word exists in the model
# useful when training own model
if word in model:
    vec1 = model.get_vector(word, norm=True)
    print(f'Vector for {word} (normalized):{vec1}')
else:
    print(f'{word} not in the model')