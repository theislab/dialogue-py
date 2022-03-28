from __future__ import annotations

from anndata import AnnData


def run_dialogue(
    adata: AnnData,
    k: int = 3,
    confounders: list[str] = None,
    phenotype: str = None,
    n_genes: int = 200,
    averaging_function: str = "col_medians",
    p_anova: float = 0.05,
    specific_pair: tuple[str, str] = None,
    output_dir: str = "./results",
) -> list[str] | None:
    """Runs DIALOGUE and finds sets of MCPs.

    Updates the AnnData object with:

        * MCPs' scores per cell

        * Cross cell type p-values per gene in the MCP

        * The correlation (R) and association (mixed-effects p-value) between the cell type specific components of each MCP

        * The association of each MCP with the phenotype of interest given as direction times -log10(p-value)

    Args:
        adata: The AnnData object to determine MCPs for.
        k: The number of MCPs to identify.
        confounders: Any potential confounders DIALOGUE needs to account for.
        phenotype: A phenotype of interest to test for association with the MCPs.
        n_genes: The number of genes to account for.
        averaging_function: The averaging function to use. One of XXX TODO
        p_anova: p-value cutoff for anova
        specific_pair: A specific pair of cell types to use for MCP calculation.
        output_dir: Output directory to write the MCPs to.

    Returns:
        MCPs - the MCPs given as a list of gene sets;
    """
    dialogue_1()
    dialogue_2()
    dialogue_3()

    return None


def dialogue_1():
    pmd()
    pmd_empirical()
    pmd_pairwise()


def pmd():
    pass


def pmd_empirical():
    pass


def pmd_pairwise():
    pass


def dialogue_2():
    hlm()
    pair()
    mixed_effects()


def hlm():
    pass


def pair():
    pass


def mixed_effects():
    pass


def dialogue_3():
    pass


def get_oe():
    pass


def fix_signature_names():
    pass


def multi_gene_pvals():
    pass


def find_scoring():
    pass


def initialize():
    pass


def iternative_nnls():
    pass


def hlm_pvals():
    pass


def add_metadata():
    pass


def sig2MCP():
    pass


def identify_cell_types():
    pass


def pcor_mat():
    pass


def p_adjust_matrix_per_label():
    pass
