import NodegraphAPI
from Katana import KatanaFile
import os




# import NodegraphAPI

# node = NodegraphAPI.GetNode("Dot")


# ff =NodegraphAPI.BuildNodegraphXmlIO()

# for x in ff:
#     print ff


# import sys
# for x,y in sys.modules.items():
#     print x,y

# NodegraphAPI.Util.GetAllConnectedInputs([node])

# graphUtil = NodegraphAPI.Util

# help(graphUtil)


# from Katana import KatanaFile

# for n in NodegraphAPI.Util.GetAllConnectedInputs([node]):
#     if n.getParent() ==  NodegraphAPI.GetRootNode():
#         print n


# path  = r"Z:\wzrylan\assets\char\c001006cwjkb\surface\look\main\ok\c001006cwjkb_look_main.katana"

# nodes = KatanaFile.Import(path,True)

# node = [n for n in nodes if node.getName() == "Dot"]
# topNodeBeforeDot = []


# nn =NodegraphAPI.GetNode("cloth_kuabao2")


# xmlTree = NodegraphAPI.BuildNodesXmlIO(NodegraphAPI.GetAllSelectedNodes())

# rootNode = NodegraphAPI.GetRootNode()
# node = KatanaFile.Paste(xmlTree, rootNode)

# outputs = NodegraphAPI.Util.GetAllConnectedOutputs([nn])
# root_group = NodegraphAPI.GetNode("Group")

# output_top = [n for n in outputs if n.getParent() == root_group]


# [n for n in NodegraphAPI.GetAllNodesByType("Backdrop",) if n.getParent() == root_group]




def getUsefullNodeFromLookVarientFile(file_path):
    if file_path and os.path.isfile(file_path) and file_path.endswith(".katana"):
        # 导入文件
        # 创建一个临时储存位置
        root = NodegraphAPI.GetRootNode()
        temp_group = NodegraphAPI.CreateNode('Group', root)
        fileNodes = KatanaFile.import(file_path,False,temp_group)
        # 过滤有用的节点
        # materials 节点
        
        # 属性设置节点





