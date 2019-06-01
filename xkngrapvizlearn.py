import cv2
import pygraphviz as pgv

G=pgv.AGraph("graphdemo.dot",encoding='UTF-8')
G.add_node("a")
G.add_node("我的世界",fontname="Microsoft YaHei", shape="rect", style="rounded", fontsize=18)
G.add_node("你的世界",fontname="Microsoft YaHei")
G.add_node("我的世界",fontname="Microsoft YaHei", shape="rect", fontsize=30)
G.add_edge("a","我的世界")
nlist=["T1","T2","T3"]
G.add_nodes_from(nlist,color="blue")

nd=G.get_node("你的世界")
nd.attr["shape"]="box"
nd.attr["color"]="red"
nd.attr["style"]="filled"

e=G.get_edge("a","我的世界")
e.attr["color"]="green"
G.graph_attr["label"]="Minecraft Python Teaching"

nd=G.get_node("我的世界")
nd.attr["shape"]="doubleoctagon"
nd.attr["color"]="blue"
nd.attr["style"]="filled"


G.layout()
G.draw("xkngd.jpg")
img=cv2.imread("xkngd.jpg")
cv2.imshow("xkngdlayout",img)
cv2.waitKey(5000)

G.layout(prog="dot")
G.draw("xkngd.jpg")
img=cv2.imread("xkngd.jpg")
cv2.imshow("xkngdlayout",img)
cv2.waitKey(5000)

cv2.destroyAllWindows()