import numpy
class Camera:
    position = (0,0)
    screensize = (0,0)
    def __init__(self,position,screensize):
        self.position = position
        self.screensize = screensize
    def viewcut(self,totalmap):#定义摄像机显示区域切片函数，传入列表与切片开始坐标显示大小，并进行渲染
        endlist = totalmap[self.position[1] - 1:self.position[1] - 1 + self.screensize[1],self.position[0] - 1:self.position[0] - 1 + self.screensize[0]].tolist()
        time = 0
        for i in endlist: 
            endlist[time] = "".join(i)
            time = time + 1
        endlist = "\n".join(endlist)
        return endlist
        '''for i in range(self.screensize[1]):
            templine = totalmap[self.position[1] + i - 1][self.position[0] - 1:self.position[0] - 1 + self.screensize[0]]
            endlist.append(templine)
        time = 0
        for i in endlist:
            endlist[time] = "".join(i)
            time = time + 1
        endlist = "\n".join(endlist)'''




