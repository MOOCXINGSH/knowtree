
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)
text = open(path.join(d, 'text.txt')).read()
yang_mask = np.array(Image.open(path.join(d, "betago.jpg")))
stopwords = set(STOPWORDS)
stopwords.add("said")
wc = WordCloud(background_color="black", max_words=2000, mask=yang_mask,
               stopwords=stopwords)
# generate word cloud
wc.generate(text)
# store to file
wc.to_file(path.join(d, "betago1.jpg"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(yang_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
wc.to_file(path.join(d, "out.png"))
