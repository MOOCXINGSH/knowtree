import pygraphviz as  pgv
from pygraphviz import *
G =pgv.AGraph("yang.dot",encoding='UTF-8')
G.add_node("a")
G.add_node("我的世界",fontname="Microsoft YaHei", shape="rect", style="rounded", fontsize=18)



