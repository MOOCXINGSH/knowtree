import cv2
import pygraphviz as pgv

G=pgv.AGraph("gtree.dot",encoding='UTF-8')

G.layout(prog="dot")
G.draw("xkngd.jpg")
img=cv2.imread("xkngd.jpg")
cv2.imshow("xkngdlayout",img)
cv2.waitKey(5000)

cv2.destroyAllWindows()