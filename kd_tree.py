import numpy as np
import matplotlib.pyplot as plt
from ctypes import cdll
import mayavi.mlab
import os

#p = os.getcwd() + '/main.so'
#f = cdll.LoadLibrary(p)


def readFile(filename, separator):
    data = [[], [], []]
    f = open(filename, 'r')
    line = f.readline()
    point_num = 0

    while line:
        x_str, y_str, z_str = line.split(separator)

        data[0].append(x_str) #X coordinate
        data[1].append(y_str) #Y coordinate
        data[2].append(z_str) # Z coordinate

        point_num = point_num + 1
        line = f.readline()

    f.close()

    #string型转float型
    x = [float(data[0]) for data[0] in data[0]]
    y = [float(data[1]) for data[1] in data[1]]
    z = [float(data[2]) for data[2] in data[2]]

    print("输入点的个数为：{}个。".format(point_num))

    point = [x, y, z]
    return point


def viz_mayavi(data, title):

    x = data[0]
    y = data[1]
    z = data[2]

    #fig = mayavi.mlab.figure(bgcolor=(0, 0, 0), size=(640, 360))
    mayavi.mlab.points3d(
        x, y, z,
        #col = np.sqrt(x ** 2 + y ** 2),
        mode = "point",
        colormap='spectral',
        #figure = fig,
    )
    mayavi.mlab.show()


if __name__ == "__main__":
    points = readFile("n_new.txt", ',')
    viz_mayavi(points, "Point Cloud")
