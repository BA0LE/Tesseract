from math import sin, cos
import numpy as np

def rot_xy(a):
    c, s = cos(a), sin(a)
    return np.array([
        [c, -s, 0, 0],
        [s, c, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def rot_xz(a):
    c, s = cos(a), sin(a)
    return np.array([
        [c, 0, -s, 0],
        [0, 1, 0, 0],
        [s, 0, c, 0],
        [0, 0, 0, 1]
    ])

def rot_yz(a):
    c, s = cos(a), sin(a)
    return np.array([
        [1, 0, 0, 0],
        [0, c, -s, 0],
        [0, s, c, 0],
        [0, 0, 0, 1]
    ])

def rot_xw(a): # w is the 4 dimention
    c, s = cos(a), sin(a)
    return np.array([
        [c, 0, 0, -s],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [s, 0, 0, c]
    ])

def rot_yw(a):
    c, s = cos(a), sin(a)
    return np.array([
        [1, 0, 0, 0],
        [0, c, 0, -s],
        [0, 0, 1, 0],
        [0, s, 0, c]
    ])

def rot_zw(a):
    c, s = cos(a), sin(a)
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, c, -s],
        [0, 0, s, c]
    ])

#position (x, y, z, w)

def projection_4d_to_3d(p4: np.ndarray, w_dist = 2.0):#hi vong no hoat dong :)))
    d = 1.0/(w_dist-p4[3]) #goi la perspective factor theo 'W'
    return p4[:3]*d #np.ndarray

def projection_3D_to_2D(p3: np.ndarray, fov, W, H)-> tuple[int, int]:
    z = p3[2]
    x = int(p3[0] * fov/z + W / 2)
    y = int(-p3[1] * fov/z + H / 2)
    return x, y

