import cv2
import pygraphviz as pyg
g=pyg.AGraph(encoding='UTF-8')  #建立图

g.add_node('人工智能',color='red',fontname="Microsoft YaHei", shape="rect", fontsize=18)  #建立点
g.add_node('3D打印',color='red',fontname="Microsoft YaHei", shape="rect", fontsize=18)  #建立点
g.add_node("电子积木",color='blue',fontname="Microsoft YaHei", shape="rect", fontsize=18)
g.add_node("Python",color='green',fontname="Microsoft YaHei", shape="rect", fontsize=18)
#3D打印
g.add_node("123D Design",fontname="Microsoft YaHei", fontsize=18)
g.add_node("Fusion360",fontname="Microsoft YaHei", fontsize=18)
g.add_node("TinkerCAD",fontname="Microsoft YaHei", fontsize=18)
g.add_node("3dOne",fontname="Microsoft YaHei", fontsize=18)

g.add_node("花瓶",fontname="Microsoft YaHei", fontsize=18)
g.add_node("象棋",fontname="Microsoft YaHei", fontsize=18)
g.add_node("水杯",fontname="Microsoft YaHei", fontsize=18)
g.add_node("五角星挂件",fontname="Microsoft YaHei", fontsize=18)

#电子积木
g.add_node("Arduino",fontname="Microsoft YaHei", fontsize=18)
g.add_node("mCookie",fontname="Microsoft YaHei", fontsize=18)
g.add_node("Uknow",fontname="Microsoft YaHei", fontsize=18)
g.add_node("比特小镇",fontname="Microsoft YaHei", fontsize=18)
g.add_node("201套件",fontname="Microsoft YaHei", fontsize=18)
g.add_node("301套件",fontname="Microsoft YaHei", fontsize=18)
#Python
g.add_node("我的世界",fontname="Microsoft YaHei", fontsize=18)
g.add_node("树莓派",fontname="Microsoft YaHei", fontsize=18)
g.add_node("OpenCV",fontname="Microsoft YaHei", fontsize=18)
g.add_node("图像识别",fontname="Microsoft YaHei", fontsize=18)
g.add_node("语音识别",fontname="Microsoft YaHei", fontsize=18)
g.add_node("神经网络",fontname="Microsoft YaHei", fontsize=18)

g.add_edge('人工智能','3D打印')
g.add_edge('人工智能','电子积木')
g.add_edge('人工智能','Python')

g.add_edge('3D打印','123D Design')
g.add_edge('3D打印','Fusion360')
g.add_edge('3D打印','TinkerCAD')
g.add_edge('3D打印','3dOne')
g.add_edge('123D Design','花瓶')
g.add_edge('123D Design','象棋')
g.add_edge('123D Design','水杯')
g.add_edge('123D Design','五角星挂件')

g.add_edge('电子积木','Arduino')
g.add_edge('电子积木','mCookie')
g.add_edge('电子积木','Uknow')

g.add_edge('Python','我的世界')
g.add_edge('Python','树莓派')
g.add_edge('Python','OpenCV')
g.add_edge('OpenCV','图像识别')
g.add_edge('OpenCV','图像识别')
g.add_edge('OpenCV','语音识别')
g.add_edge('OpenCV','神经网络')

g.add_edge('mCookie','比特小镇')
g.add_edge('mCookie','201套件')
g.add_edge('mCookie','301套件')


nd=g.get_node("人工智能")
nd.attr["shape"]="box"
nd.attr["color"]="blue"
nd.attr["style"]="filled"


g.graph_attr["label"]="MOOCXING Teaching"


g.layout(prog="dot")
g.draw("yang.png")
img=cv2.imread("yang.png")
cv2.imshow("yang",img)
cv2.waitKey(9000)

cv2.destroyAllWindows()
