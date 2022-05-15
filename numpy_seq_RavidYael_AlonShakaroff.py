import numpy as np


# ~~~~~~~~~ Q1.1 ~~~~~~~~~ #
def half(x):
    res_arr = np.copy(np.array(x))
    res_arr = res_arr[1::2, ::2]
    res_arr = (res_arr / 2)
    return res_arr


# ~~~~~~~~~ Q1.2 ~~~~~~~~~ #
def outer_product(x, y):
    x = np.array(x).reshape(1, np.array(x).shape[0])
    y = np.array(y).reshape(np.array(y).shape[0], 1)
    mult_matrix = (np.matmul(np.array(y), np.array(x)))
    return mult_matrix


# ~~~~~~~~~ Q1.3 ~~~~~~~~~ #
def extract_logical(x, arr):
    ind = (arr % 1 == 0)
    z = x[ind == True]
    return z, ind


def extract_integer(x, arr):
    z, _ = extract_logical(x, arr)
    ind = np.zeros((x.ndim, z.size), dtype=int)
    return z, ind

# ~~~~~~~~~ Q1.4 ~~~~~~~~~ #
def calc_norm(x, axis=0):
    powered_x = x ** 2
    x_summed = np.sum(powered_x.transpose(), axis=axis)
    x_res = np.sqrt(x_summed)
    return x_res


def normalize(x, axis=0):
    norms = calc_norm(x, axis)
    identity_norms = 1 / norms
    if(axis == 1):
        res = x * identity_norms
    else:
        res = identity_norms.reshape(-1,1) * x

    return res


# ~~~~~~~~~ Q1.5 ~~~~~~~~~ #
def matrix_norm(x, k=1000):
    A = x
    n = x.shape[0]
    X = np.random.randn(n, k)
    X_normalized = normalize(X, axis=1)
    Z = A @ X_normalized
    u = calc_norm(Z, axis=1)
    return np.max(u)


# ~~~~~~~~~ Q1.6 ~~~~~~~~~ #
def det(A):
    A = np.array(A)
    print(A)
    if A.shape[0] <= 2:
        d = A[0][0]*A[1][1] - A[0][1]*A[1][0]

    else:
        d = 0
        for i in range(A.shape[0]):
            slicedA = np.delete(A, i, 1)
            slicedA = np.delete(slicedA, 0, 0)
            d += ((-1)**i) * A[0][i] * det(slicedA)
            print(d)

    return d


# ~~~~~~~~~ Q1.7 ~~~~~~~~~ #
def black_white_segment(im, thresh):
    seg = im.copy()
    seg[seg < thresh] = 0
    seg[seg >= thresh] = 255
    return seg


def segment(im, thresh=128):
    im = np.array(im)
    if im.ndim == 3:
        im = np.mean(im, axis=2)

    return black_white_segment(im, thresh)


# ~~~~~~~~~ Q1.9 ~~~~~~~~~ #
def is_magic(A):
    A = np.array((A))
    s = np.sum(A[:,0])
    main_diagonal = np.diagonal(A)
    second_diagonal = np.diagonal(np.fliplr(A))
    cols_sums = A.sum(axis = 0)
    rows_sums = A.sum(axis = 1)
    main_diagonal_sum = np.sum(main_diagonal)
    second_diagonal_sum = np.sum(second_diagonal)
    all_distincts = np.unique(A).size == A.size
    sums_are_equal = ((main_diagonal_sum == s) and (second_diagonal_sum == s) and (np.all(cols_sums == s)) and (np.all(rows_sums == s)))
    return all_distincts and sums_are_equal

