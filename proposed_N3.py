import numpy as np

def proposed_N3():
    a = -0.2113
    b = 0.5774

    matrix0 = np.array([
        [1, 1, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 1],
    ])
    matrix1 = np.array([
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
    ])

    matrix2 = np.diag([1, a, 1, b, 1])

    matrix3 = np.array([
        [1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]
    ])

    matrix4 = np.diag([
        1,
        2,
        1,
        1,
        1
    ])

    matrix5 = np.array([
        [0, 1, 0],
        [0, 1, 0],
        [1, 0, 0],
        [1, -1, 1],
        [0, 0, 1],
    ])


    result = matrix0 @ matrix1 @ matrix2 @ matrix3 @ matrix4 @ matrix5

    return result