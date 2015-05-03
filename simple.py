#!/usr/bin python
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

font_path = '/System/Library/Fonts/Menlo.ttc' 
save_path = 'images/allthethings.png'
d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'wordlist.txt')).read()
wordcloud = WordCloud(font_path).generate(text)

wordcloud.to_file(save_path)

# Open a plot of the generated image.
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()