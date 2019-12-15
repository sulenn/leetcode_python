from . import Node
class Solution:
    def connect(self, root):
        if not root:
            return None
        curLevel = [root]
        while curLevel:
            nextLevel = []
            for k,v in enumerate(curLevel):
                if k != len(curLevel)-1:
                    if v.left:
                        nextLevel.append(v.left)
                    if v.right:
                        nextLevel.append(v.right)
                    v.next = curLevel[k+1]
                else:
                    if v.left:
                        nextLevel.append(v.left)
                    if v.right:
                        nextLevel.append(v.right)
            curLevel = nextLevel
        return root