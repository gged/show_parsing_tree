# -*- coding: cp936 -*-
import sys
from MultiTree import *
import pygraphviz as pgv
'''
default graph file:tree.png
G.add_node(u"经理", fontname="Microsoft YaHei", shape="rect", style="rounded", fontsize=18) #雅黑
G.add_node(u"秘书", fontname="SimHei") #黑体
G.add_node(u"小兵", fontname="SimSun") #宋体
G.add_node(u"小卒", fontname="Kaiti") #楷体
'''

default_coding='gbk'

class treeWriter():
    def __init__(self, tree):
        self.num = 1       #mark each visible node as its key
        self.tree = tree
        self.fontname="Microsoft YaHei"
        
    def write(self, outfile = 'tree.png'):
        def writeHelp(root, A):
            if not root:
                return
            
            p = str(self.num)
            self.num += 1###
            #A.add_node(p, label = str(root.elem))
            A.add_node(p, label = root.elem,fontname=self.fontname)
            son_num=[]
            for son in root.nsons:
                anum=writeHelp(son, A)
                A.add_node(anum, label = son.elem)
                A.add_edge(p,anum)
                son_num.append(anum)
            if son_num!=[]:
                B = A.add_subgraph(son_num, rank = 'same')
                for i in xrange(0,len(son_num)-1):
                    B.add_edge(son_num[i], son_num[i+1], style = 'invis')
            
            return p  #return key root node
        ##########
        self.A = pgv.AGraph(directed=False,strict=True)#arrow,
        writeHelp(self.tree.root, self.A)
        self.A.graph_attr['epsilon']='0.001'
        #print self.A.string() # print dot file to standard output
        self.A.layout('dot') # layout with dot
        #'neato'|'dot'|'twopi'|'circo'|'fdp'|'nop'
        self.A.draw(outfile) # write to file        
        
  
if __name__ == '__main__':
    tree = MultiTree()
    ##sen a CTB tree##
    sen='( (IP (PP (P 对) (NP (PN 此))) (PU ，) (NP-PN-SBJ (NR 浦东)) (VP (VP (ADVP (AD 不)) (VP (VC 是) (VP (DVP (VP (VA 简单)) (DEV 的)) (VP (VV 采取) (NP-OBJ (CP-APP (IP (NP-SBJ (-NONE- *PRO*)) (VP (PU “) (VP (VV 干) (NP-EXT (QP (CD 一) (CLP (M 段))) (NP (NN 时间)))) (PU ，) (VP (PP (P 等) (LCP (IP (NP-SBJ (-NONE- *pro*)) (VP (VV 积累) (AS 了) (NP-OBJ (NN 经验)))) (LC 以后))) (ADVP (AD 再)) (VP (VP (VV 制定) (NP-OBJ (NN 法规) (NN 条例))))) (PU ”))) (DEC 的)) (NP (NN 做法))))))) (PU ，) (CC 而) (VP (VC 是) (VP (VP (VV 借鉴) (NP-OBJ (DNP (NP (NP (ADJP (JJ 发达)) (NP (NN 国家))) (CC 和) (NP (NP-PN-APP (NR 深圳) (ETC 等)) (NP (NN 特区)))) (DEG 的)) (NP (NN 经验) (NN 教训)))) (PU ，) (VP (VV 聘请) (NP-OBJ (NP (NN 国内外)) (ADJP (JJ 有关)) (NP (NN 专家) (NN 学者)))) (PU ，) (VP (DVP (ADVP (AD 积极) (PU 、) (AD 及时)) (DEV 地)) (VP (VP (VV 制定) (NP-OBJ (-NONE- *RNR*-1))) (CC 和) (VP (VV 推出) (NP-OBJ-1 (NN 法规性) (NN 文件))))) (PU ，) (VP (VV 使) (NP-OBJ (DP (DT 这些)) (NP (NN 经济) (NN 活动))) (IP (NP-SBJ (-NONE- *PRO*)) (VP (VP (ADVP (AD 一)) (VP (VV 出现))) (VP (ADVP (AD 就)) (VP (SB 被) (VP (VV 纳入) (NP-OBJ (NN 法制) (NN 轨道))))))))))) (PU 。)) )'
    tree.createTree(sen.decode(default_coding))
##    print '###'
##    tree.preorderTravel()
##    print '###'
    writer = treeWriter(tree)
    if len(sys.argv) > 1:#your graph file name
        outfile = sys.argv[1]
        writer.write(outfile) #write result to outfile
    else:
        writer.write() #write result to tree.png
    

