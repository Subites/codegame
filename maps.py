import numpy
class Maps:
    mapsize = (0,0)
    mapfill = " "
    mapshow = []
    mapoutput = ""
    def __init__(self,mapsize,mapfill):
        self.mapsize = mapsize
        self.mapfill = mapfill
    def mapreset(self):
        self.mapshow = []#还原列表
        for i in range(self.mapsize[1]*3):
            self.mapshow.append([])
            for k in range(self.mapsize[0]*3):
                self.mapshow[i].append(self.mapfill)
        return numpy.array(self.mapshow)#返回列表矩阵
