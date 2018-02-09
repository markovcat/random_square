"""
Generate a random square.

"""

import numpy as np


def binary_square(img_size=30,
                  sqr_size=10):
    img = np.zeros((img_size, img_size), dtype=np.int)
    x, y = tuple(np.random.randint(0, img_size - sqr_size, size=2))
    img[x: x + sqr_size, y: y + sqr_size] = 1

    return img




