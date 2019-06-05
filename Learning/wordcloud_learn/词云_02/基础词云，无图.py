from wordcloud import WordCloud
import matplotlib.pyplot as plt
f=open('haproxy.txt','r')
#with open('haproxy.txt','r') as f:
mytext = f.read()
    
wordcloud = WordCloud().generate(mytext)

plt.imshow(wordcloud,interpolation="bilinear")

plt.axis("off")

plt.show()
