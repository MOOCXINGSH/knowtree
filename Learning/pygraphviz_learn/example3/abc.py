import pygraphviz as pyg
g=pyg.AGraph()  #建立图  
g.add_node('A',color='red')  #建立点
g.add_edge('A','B')  #建立边
g.add_edge('A','C')  #建立边
g.add_edge('A','D')  #建立边
g.add_edge('D','f')
g.add_edge('f','A') 
g.layout(prog='dot')  #绘图类型
g.draw('pyg1.png')   #绘制
#g.draw('pyg1.pdf')   #绘制
