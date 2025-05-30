import numpy as np

def proposed_N7():
    a = 0.4526
    b = 0.5312
    c = 0.5045
    d = 0.3780
    e = 0.1765
    f = -0.0598
    g = -0.2844

    matrix1 = np.array([
        [ 1, 0, 1, 0, 0, 0, 0, 0],
        [-1, 0, 0, 1, 0, 0, 0, 0],
        [ 1, 0, 0, 0, 1, 0, 0, 0],
        [-1, 1, 0, 0, 0, 0, 0, 0],
        [ 1, 0, 0, 0, 0, 1, 0, 0],
        [-1, 0, 0, 0, 0, 0, 1, 0],
        [ 1, 0, 0, 0, 0, 0, 0, 1]
    ])
    # 7

    matrix2 = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0,-1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0,-1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0]
    ])

    matrix3 = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0,-1, 0, 0],
        [0, 0, 0, 1, 0, 0,-1, 0],
        [0, 0, 0, 0, 1, 0, 0,-1]
    ])
    # 6

    matrix4 = np.diag([
        1, 1, 1, 1, 1, 1, -1, 1
    ])

    matrix5 = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 1,-1, 0, 0, 0, 0],
        [0, 0, 1, 0,-1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 1,-1, 0],
        [0, 0, 0, 0, 0, 1, 0,-1]
    ])
    # 8

    matrix6 = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    ])
    # 4
    matrix7 = np.diag([
        d,
        d,
        (c + a + (-b) + e + g + (-f)) / 6,
        (-3 * c + 3 * (-b) - 3 * e + 3 * (-f)) / 6,
        (-3 * c + 3 * a - 3 * e + 3 * g) / 6,
        (2 * c - a - (-b) + 2 * e - g - (-f)) / 6,
        (c - a + (-b) - e + g - (-f)) / 6,
        (-3 * c + 3 * (-b) + 3 * e - 3 * (-f)) / 6,
        (-3 * c - 3 * a + 3 * e + 3 * g) / 6,
        (2 * c + a - (-b) - 2 * e - g + (-f)) / 6
    ])

    matrix8 = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1]
    ])
    # 4
    matrix9 = matrix5

    matrix10 = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0]
    ])

    matrix11 = matrix4

    matrix12 = matrix3


    matrix13_14 = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0,-1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0,-1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
    ])


    matrix15 = np.array([
        [0, 0, 0, 1, 0, 0, 0],
        [1,-1, 1, 0, 1,-1, 1],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1]
    ])

    result = matrix1 @ matrix2 @ matrix3 @ matrix4 @ matrix5 @ matrix6 @ matrix7 @ matrix8 @ matrix9 @ matrix10 @ matrix11 @ matrix12 @ matrix13_14 @ matrix15

    return result