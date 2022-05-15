import numpy as np
import pandas as pd
import math


def stable_marriage(dames, gents, marriages):
    dames_indexes = dames.index
    gents_indexes = gents.index
    dames_preferences = pd.DataFrame(False, index=dames_indexes, columns=gents_indexes)
    gents_preferences = pd.DataFrame(False, index=gents_indexes, columns=dames_indexes)

    for dame, gent in marriages:
        dame_preference_order = dames.loc[dame]
        gent_rank = dame_preference_order[dame_preference_order == gent].index[0]
        gents_ranked_better = dame_preference_order[:gent_rank].values
        gent_preference_order = gents.loc[gent]
        dame_rank = gent_preference_order[gent_preference_order == dame].index[0]
        dames_ranked_better = gent_preference_order[:dame_rank].values
        dames_preferences.loc[dame][gents_ranked_better] = True
        gents_preferences.loc[gent][dames_ranked_better] = True

    dames_preferences = dames_preferences.transpose()
    stable = not((dames_preferences & gents_preferences).any(axis=None))

    return stable



def main():
    dames = pd.DataFrame.from_dict({'mary': ['john', 'mathew', 'dan'],
                                    'sarah': ['mathew', 'john', 'dan'],
                                    'eve': ['dan', 'mathew', 'john']}, orient='index')

    gents = pd.DataFrame.from_dict({'john': ['mary', 'sarah', 'eve'],
                                    'mathew': ['sarah', 'mary', 'eve'],
                                    'dan': ['eve', 'mary', 'sara']}, orient='index')

    marriages = [('mary', 'john'), ('sarah', 'mathew'), ('eve', 'dan')]

    print(stable_marriage(dames, gents, marriages))


if __name__ == '__main__':
    main()