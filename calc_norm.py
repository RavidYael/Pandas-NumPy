import numpy as np
import pandas as pd
import math



def partial_sum(s):
    s_not_null = s[s.notnull()]
    return math.sqrt(abs(s_not_null).sum())


def main():
    data1 = np.array([1, -4.5, 2, None, -1.5])
    ser = pd.Series(data1)
    print(partial_sum(ser))

if __name__ == '__main__':
    main()