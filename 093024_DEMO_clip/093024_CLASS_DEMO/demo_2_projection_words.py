from CLIP_helper import *
import numpy as np

#words to project
words = [
    "cat", "dog", "bird", "fish", "rabbit", "hamster", "turtle", "snake", "lizard", "parrot"
]

#semantic axes
axis1 = "mammals"
axis2 = "birds"

#we can precompute the vectors for the two axes
axis1_vec = encode_text(axis1)
axis2_vec = encode_text(axis2)

#initialize lists to store the coordinates of the words and their colors
x_data = []
y_data = []

#iterate over the words
for word in words:
    #encode the word
    word_vec = encode_text(word)
    #compute the similarity of the word to the two axes using the dot product (this is the cosine similarity since encode_text already normalized the vectors)
    x = np.dot(word_vec, axis1_vec)
    y = np.dot(word_vec, axis2_vec)
    #store the coordinates and the color of the word
    x_data.append(x)
    y_data.append(y)

#bounce of the data fits to the plot
x_min = min(x_data)
x_max = max(x_data)
y_min = min(y_data)
y_max = max(y_data)

#import matplotlib for plotting
import matplotlib.pyplot as plt

#set the colors for the plot
bg_color = (0.35, 0.45, 0.6)
axes_color = (0.5, 1.0, 1.0)
grid_color = (0.2, 0.6, 0.7)
text_color = (0.8, 1.0, 1.0)
text_bg_color = (0.1, 0.55, 0.6, 0.4)
dot_color = (1.0, 0.0, 1.0)

#create the plot with the specified bavkground color of the window
plt.figure(figsize=(6,6), facecolor=bg_color)
#set the title of the plot
plt.title(f"Planar projection along {axis1} and {axis2}")

#enable the grid and set its color
plt.grid(color = grid_color)

#set the limits of the plot (zoom level on the XY plane)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

#set the labels for the axes
plt.xlabel(axis1)
plt.ylabel(axis2)

#getthe current plot axes (matplotlib supports multiple axes (kind of viewports) in the same plot but in this and following examples we will use only one)
ax = plt.gca()

#set the background color of the plot
ax.set_facecolor(bg_color)
#draw the X and Y axes as a horizontal and vertical lines
ax.axhline(0, color=axes_color)
ax.axvline(0, color=axes_color)

#draw the word at the specified coordinates
#ax.text(x, y, word, fontsize=10, color=text_color, backgroundcolor=text_bg_color)
#draw a dot at the specified coordinates
ax.scatter(x_data, y_data, color=dot_color)

for i, word in enumerate(words):
    x = x_data[i]
    y = y_data[i]
    word = words[i]
    ax.text(x, y, word, fontsize=10, color=text_color, backgroundcolor=text_bg_color)

#show the plot
plt.show()
