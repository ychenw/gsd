#install pytorch from https://pytorch.org/get-started/locally/
#install CLIP from https://github.com/openai/CLIP

#pip install ftfy regex tqdm
#pip install git+https://github.com/openai/CLIP.git

import torch
import clip
import numpy as np
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def encode_text(text : str, normalize : bool = True) -> np.ndarray:
    tokens = clip.tokenize(text).to(device)
    with torch.no_grad():
        text_features : torch.Tensor = model.encode_text(tokens)
        text_features = text_features[0].cpu().numpy()
    if normalize:
        text_features /= np.linalg.norm(text_features)
    return text_features

def encode_image(image : Image, normalize : bool = True) -> np.ndarray:
    if isinstance(image, str):
        image = Image.open(image)
    image = preprocess(image).unsqueeze(0).to(device)
    with torch.no_grad():
        image_features : torch.Tensor = model.encode_image(image)
        image_features = image_features[0].cpu().numpy()
    if normalize:
        image_features /= np.linalg.norm(image_features)
    return image_features
