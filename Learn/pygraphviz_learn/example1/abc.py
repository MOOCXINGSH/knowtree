import cv2
import pygraphviz as pyg
g=pyg.AGraph(encoding='UTF-8')  #建立图  
g.add_node('看',color='red',fontname="Microsoft YaHei", shape="rect", fontsize=38)  #建立点
g.add_edge('A','B')  #建立边
g.add_edge('A','C')  #建立边
g.add_edge('A','D')  #建立边
g.add_edge('D','f')
g.add_edge('f','看')
nlist=["T1_yang","T2","T3"]
g.add_nodes_from(nlist,color="pink")

nd=g.get_node("1111")
nd.attr["shape"]="box"
nd.attr["color"]="red"
nd.attr["style"]="filled"

g.layout(prog='dot')  #绘图类型
g.draw('pyg1.png')   #绘制
#g.draw('pyg1.pdf')   #绘制

#nd=g.add_node("你的世界")
#nd.attr["shape"]="box"
#nd.attr["color"]="red"
#nd.attr["style"]="filled"
