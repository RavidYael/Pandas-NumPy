import pandas as pd
import math


# ~~~~~~~~~ Q2.1 ~~~~~~~~~ #
def three_x_plus_1(s):
    mask = s % 2 == 0
    res = s.copy()
    res[mask] /= 2
    res[~mask] = (res * 3) + 1

    return res


# ~~~~~~~~~ Q2.2 ~~~~~~~~~ #
def reindex_up_down(s):
    res = s.copy()
    new_cased_names = pd.DataFrame(res).apply(lambda a: a.name.upper() if a.name[0].isupper() else a.name.lower(), 1)
    res.index = new_cased_names.values

    return res


# ~~~~~~~~~ Q2.3 ~~~~~~~~~ #
def no_nans_idx(s):
    res = s.copy()
    res = res.isna()

    return res


# ~~~~~~~~~ Q2.4 ~~~~~~~~~ #
def partial_sum(s):
    s_not_null = s[s.notnull()]
    return math.sqrt(abs(s_not_null).sum())


# ~~~~~~~~~ Q2.5 ~~~~~~~~~ #
def partial_eq(s1, s2):
    s1_not_null = s1[s1.notnull()]
    s2_not_null = s2[s2.notnull()]
    intersected_indexes = s1_not_null.index & s2_not_null.index
    inters = pd.Series(s1_not_null[intersected_indexes] == s2_not_null[intersected_indexes], index=intersected_indexes)

    return inters


# ~~~~~~~~~ Q2.6 ~~~~~~~~~ #
def dropna_mta_style(df, how='any'):
    df_rows_dropped = df.dropna(axis=0, how=how)
    df_cols_dropped = df.dropna(axis=1, how=how)
    df = df.loc[df_rows_dropped.index]
    df = df[df_cols_dropped.columns]

    return df


# ~~~~~~~~~ Q2.7 ~~~~~~~~~ #
def get_n_largest(df, n=0, how='col'):
    altered_df = df.copy()
    if how == 'row':
        altered_df = altered_df.transpose()

    altered_df = altered_df.apply(lambda a: a.sort_values(ascending=False).values)

    return altered_df.iloc[n]


# ~~~~~~~~~ Q2.8 ~~~~~~~~~ #
def unique_dict(df, how='col'):
    altered_df = df.copy()
    if how == 'row':
        altered_df = altered_df.transpose()

    res = {}

    for col in altered_df.columns:
        curr_col = altered_df[col]
        curr_uniques = curr_col.unique()
        res[col] = pd.Series(curr_uniques)

    return res


# ~~~~~~~~~ Q2.9 ~~~~~~~~~ #
def upper(df):
    return pd.DataFrame(df).applymap(lambda a: a.upper() if isinstance(a, str) else a)