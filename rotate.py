
# coding: utf-8

# In[2]:

import matplotlib.pyplot as plt
import numpy as np
import math


# from scipy.misc import imsave
# %matplotlib inline


def get_image(path: str = u"C:\\Users\\kübra", file: str = u"a_1.png"):
    """

    :rtype: object
    """
    if ((path is None) or (file is None)):
        path = u"C:\\Users\\kübra"
        file = u"a_1.png"

    image_file_1 = path + u"\\" + file
    img_1 = plt.imread(image_file_1)
    plt.imshow(img_1)
    plt.show()
    return img_1


def get_rotation_matrix_for_angle(angle: float):
    theta = angle
    rotation_matrix = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]], np.float)

    return rotation_matrix


def get_new_point(old_point: list, angle: float):
    old_point_i, old_point_j = old_point[0], old_point[1]
    rotation_matrix = get_rotation_matrix_for_angle(angle)
    point = np.array([old_point_i, old_point_j], np.float)
    point = point.reshape(2, 1)
    new_point = np.matmul(rotation_matrix, point)
    x = int(new_point[0])
    y = int(new_point[1])

    return [x, y]


def get_new_canvas_for_an_image(m: int, n: int, angle: float, dim: str = 3):
    old_corners = [[0, 0], [m, 0], [0, n], [m, n]]
    new_corners = []
    for p in old_corners:
        p_new = get_new_point(p, angle)
        new_corners.append(p_new)
        # print(p_new)

    y_min = min([y for x, y in new_corners])
    y_max = max([y for x, y in new_corners])
    y_min, y_max

    x_min = min([x for x, y in new_corners])
    x_max = max([x for x, y in new_corners])
    x_min, x_max

    m = int(abs(x_max - x_min))
    n = int(abs(y_max - y_min))

    img_2 = np.zeros((m, n, dim))

    return img_2


def get_rotated_image(image, angle: float):
    """

    :type angle: object
    """
    new_image_rotated = get_new_canvas_for_an_image(image.shape[0], image.shape[1], angle, image.ndim)

    offset_m = int((abs(new_image_rotated.shape[0] - image.shape[0])))
    offset_n = int((abs(new_image_rotated.shape[1] - image.shape[1])))

    rotation_matrix = get_rotation_matrix_for_angle(angle)

    for i in range(image.shape[0] - 15):
        for j in range(image.shape[1] - 15):
            new_point = get_new_point([i, j], angle)
            new_i = int(new_point[0] + offset_m)
            new_j = int(new_point[1] + offset_n)
            new_image_rotated[new_i, new_j, :] = image[i, j, :]
    return new_image_rotated


def get_new_coordinates(img, angle):
    new_coors = {}
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            new_coors[(i, j)] = get_new_point([i, j], angle)

    return new_coors


def rotate_image_by_angle(image, angle):
    im_10 = image
    angle = angle
    result = get_new_coordinates(im_10, angle)
    x_min = min([result[xy][0] for xy in result])
    x_max = max([result[xy][0] for xy in result])
    y_min = min([result[xy][1] for xy in result])
    y_max = max([result[xy][1] for xy in result])
    im_11 = get_new_canvas_for_an_image(im_10.shape[0], im_10.shape[1], angle, im_10.ndim)
    plt.imshow(im_11)
    plt.show()
    for x in result:
        # x , result[x]
        if x_min < 0:
            new_i = result[x][0] + abs(x_min)
        else:
            new_i = result[x][0] + abs(x_min)
        if y_min < 0:
            new_j = result[x][1] + abs(y_min)
        else:
            new_j = result[x][1] + abs(y_min)
        if 0 < new_i < im_11.shape[0] and 0 < new_j < im_11.shape[1]:
            im_11[new_i, new_j, :] = im_10[x[0], x[1], :]
    plt.imshow(im_11)
    plt.show()
    a = 10
    return im_11


image = rotate_image_by_angle(get_image(), math.pi/2)
plt.imshow(image)
plt.show()


# In[ ]:



