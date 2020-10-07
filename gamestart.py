import maps
import camera
import UI
from time import *
mainmap = maps.Maps((150,50),"o")#实例化地图
totalmap = mainmap.mapreset()#重置地图
maincamera = camera.Camera(mainmap.mapsize,mainmap.mapsize)
UI.reset()
while True:
    start = perf_counter()
    UI.UIdraw(maincamera.viewcut(totalmap))
    end = perf_counter()
    print(end - start)



