import numpy as np
import pandas as pd


def upper(df):
    return pd.DataFrame(df).applymap(lambda a: a.upper() if isinstance(a, str) else a)


def main():
    data1 = np.array([[1, "hellO", 3, 4, 5, 6],
                      [-1.5, 2, 5, "Fellow americans", 6.5, None],
                      [-1.3, 8, 70, 8, 9.5, None]])
    df = pd.DataFrame(data1)
    print(upper(df))

if __name__ == '__main__':
    main()