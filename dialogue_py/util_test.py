import numpy as np
import pandas as pd
import anndata as ad
from scipy.sparse import csr_matrix
import scanpy as sc
import statsmodels.api as sm

from statsmodels.formula.api import ols
from statsmodels.stats.multitest import multipletests


# removed top
def get_abundant(v, abn_c=2, boolean_flag=False, decreasing=True):
    v = pd.Series(v)
    samples_sorted = v.value_counts()
    samples_sorted = samples_sorted[samples_sorted >= abn_c]
    abn_names = samples_sorted.index.values.tolist()
    # abn_names = np.concatenate(abn_names).ravel().tolist()

    if boolean_flag:
        return [x in abn_names for x in v]
    return abn_names


def average_mat_rows(m, ids):
    ids_u = get_abundant(ids)
    ids_u.sort()
    df_new = pd.concat([pd.DataFrame(ids).reset_index(drop=True), m.reset_index(drop=True)],
                       axis=1)  # check input of ids which is the sample
    df_new = df_new.iloc[[x in ids_u for x in ids]]
    mean_df = df_new.groupby('Sample').mean()

    ids_u1 = list(set(ids) - set(ids_u))  # how ids = samples['Sample']

    if len(ids_u1) == 0:
        return mean_df

    m0 = m.iloc[[x in ids_u1 for x in ids]]
    if sum([x in ids_u1 for x in ids]) == 1:
        m0 = np.transpose(m0)

    m0.index = ids[[x in ids_u1 for x in ids]]
    m2 = pd.concat([m0, mean_df])
    m2.sort_index(inplace=True)
    return m2


def apply_anova(df, y, margin=2):
    encoding = {k: v for v, k in enumerate(np.unique(y))}
    # X.columns = [f"PC_{i:d}" for i in range(len(X.columns))]
    # df = pd.concat([X.reset_index(drop=True), y.reset_index(drop=True)], axis=1)
    df['Sample'].replace(encoding, inplace=True)

    sig = []
    for variable in df.columns:
        model = ols('{} ~ Sample'.format(variable), data=df).fit()
        anova_table = sm.stats.anova_lm(model, typ=2)
        # print(anova_table['PR(>F)']['Sample'])
        sig.append(anova_table['PR(>F)']['Sample'])

    sig.pop()
    sig_corrected = multipletests(sig, method="fdr_bh")[1]
    return sig_corrected


def center_matrix(m, dim=1, sd_flag=False):
    if dim == 1:
        d = m.mean(axis=0)
        zscores = m.apply(lambda row: row - d, axis=1)
    else:
        d = m.mean(axis=1)
        zscores = m.apply(lambda column: column - d, axis=0)

    if sd_flag:
        sd = m.std()
        zscores = zscores.apply(lambda row: row / d, axis=1)

    return zscores

