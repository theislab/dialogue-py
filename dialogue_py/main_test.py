from __future__ import annotations

from typing import Literal

import numpy as np
import pandas as pd
import scanpy as sc
import statsmodels.api as sm
from anndata import AnnData


class Dialogue:

    def __init__(self):


    def create_cell_type_obj(
        self,
        adata: AnnData,
        meta: pd.DataFrame,
        cell_type_label: str,
    ) -> AnnData:
        """

        Args:
            adata:
            meta:
            cell_type_label:

        Returns:


        Generate the main anndata object to work with, which is the celltype object equivalent

        """
        # assumption: Anndata object is basic cell * gene matrix
        # 1. take the main AnnData object, tether other information to the object in terms of layers / observations
        # 1a. adata.obs['CellQ'] to add cellq information
        # 1b. adata.obsm['X'] to add X features matrix (n x k), e.g., PCs, NMF components, tpm etc.; these features will be used to identify the multicellular programs.
        # 1c. adata.obsm['samples'] samples of each cell (n x 1)
        # 1d. adata.obs['Metadata'] to add metadata information
        # 1e. adata.obs['cell_type_label'] to add information to create anndata subsets - (remove)
        # 2. additional computation such as tpmAv and qcAv need to be added
        pass

    def dialogue1(
        self,
        adata: AnnData,
        k: int,
        main: str,
        results_dir: str,
        conf : str,
        covar: str,
        n_genes: int,
        pmd2: bool,
        extra_sparse: bool,
        averaging_function: str,
        p_anova: int,
        specific_pair: str,
        center_flag: bool,
        seed1: int,
        bypass_emp: bool
    ) -> AnnData:
        """

        Args:
            adata:
            k:
            main:
            results_dir:
            conf:
            covar:
            n_genes:
            pmd2:
            extra_sparse:
            averaging_function:
            p_anova:
            specific_pair:
            center_flag:
            seed1:
            bypass_emp:

        Returns:

        """
        #first trial at implementing first half of dialogue1. dataset
        cell_type_labels = ['fibroblast', 'epithelial']
        p_anova = 0.05
        X = []
        samples = []
        for i in cell_type_labels:
            data = pd.DataFrame(dataset[dataset[0:].obs['cell_type_label'] == i].obsm['X_pca'])
            data.columns = [f"PC_{i:d}" for i in range(len(data.columns))]
            sample = dataset[dataset[0:].obs['cell_type_label'] == i].obs['Sample']
            X1 = average_mat_rows(data, sample)
            b = get_abundant(sample, abn_c=15, boolean_flag=True)
            df = pd.concat([data.iloc[b, :].reset_index(drop=True), sample[b].reset_index(drop=True)], axis=1)
            p = apply_anova(df=df, y=sample[b])
            # df = df.set_index('Sample')
            X1 = X1.iloc[:, p < p_anova]

            X.append(X1)
            samples.append(X1.index)

        # print(X)

        # need to guve a name to the list items
        samples = [item for subl in samples for item in subl]
        samplesU = get_abundant(samples, len(cell_type_labels))

        if len(samplesU < 5):
            print('Error: Cannot run DIALOGUE with less than 5 samples')


        return adata
