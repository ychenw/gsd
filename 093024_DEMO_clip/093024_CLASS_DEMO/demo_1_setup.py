from CLIP_helper import *
import numpy as np

word = 'cat'
word_vec = encode_text(word)

axis1 = 'birds'
axis2 = 'mammals'

axis1_vec = encode_text(axis1)
axis2_vec = encode_text(axis2)

x = np.dot(word_vec, axis1)
y = np.dot(word_vec, axis2_vec)

print(f"similarity of{word} to {axis1} is {x}")
print(f"similarity of{word} to {axis2} is {y}")

import matplotlib.pyplot as plt

# set the colors for the plot
bg_color = (0.35,0.45,0.6)
axes_color = (0.3,0.3,0.3)
grid_color = (0.5,0.5,0.5)
text_color = (0.9,0.9,0.9)
text_bg_color = "black"
dot_color = 'red'

plt.figure(figsize=(6,6), facecolor=bg_color)

plt.xlim(-1.0,1.0)
plt.ylim(-1.0,1.0)

plt.text(x, y, word)
# visualize the point
plt.scattter([x], [y], color=dot_color)

plt.show()