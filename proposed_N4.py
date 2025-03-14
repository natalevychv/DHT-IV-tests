import numpy as np

def proposed_N4():
    a = 0.6533
    b = 0.2706

    matrix0 = np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, -1]
    ])

    matrix1 = np.array([
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, -1, 0],
        [0, 1, 0, -1]
    ])
    matrix2 = np.array([
        [1, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 1]
    ])

    matrix3 = np.diag([
        a - b,
        -a - b,
        b,
        a - b,
        -a - b,
        b
    ])

    matrix4 = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 1]
    ])

    matrix5 = matrix0


    result = matrix0 @ matrix1 @ matrix2 @ matrix3 @ matrix4 @ matrix5

    return result