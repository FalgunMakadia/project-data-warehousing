import pickle
import re

class Utilities:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
    def getLevelUtil(self , node, data, level):
        if (node == None):
            return 0
    
        if (node.data == data):
            return level
    
        downlevel = self.getLevelUtil(node.left,
                                data, level + 1)
        if (downlevel != 0):
            return downlevel
    
        downlevel = self.getLevelUtil(node.right,
                                data, level + 1)
        return downlevel
    
    
    def getLevel(self,node, data):
    
        return self.getLevelUtil(node, data, 1)

    def get_level(self):
            level = 0
            p = self.root
            while p:
                level += 1
                p = p.root
            return level  