import numpy as np


def calc_rows_norm(x):
    rows_norm = np.array(x).shape(np.array().shape()[0])
    rows_norm[::] = np.array(x)[::]


def calc_cols_norm(x):



def calc_norm(x, axis = 0):
    if axis == 0:
        return calc_rows_norm(x)
    else:
        return calc_cols_norm(x)