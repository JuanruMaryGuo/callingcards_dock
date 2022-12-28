import pandas as pd
from typing import List

def read_qbed(
    filename: str
    ) -> pd.DataFrame:

    """\
    Read .qbed file.

    :param filename: 
        Path to the qbed file.

    :Returns:
        pd.DataFrame for the qbed file.

    :example:
    >>> import pycallingcards as cc
    >>> qbed = cc.rd.read_qbed("https://github.com/The-Mitra-Lab/pycallingcards_data/releases/download/data/SP1_P10.txt")

       
    """

    return pd.read_csv(filename, sep = "\t",  header = None, names =  ["Chr", "Start", "End", "Reads", "Direction", "Barcodes"])

def combine_qbed(
    filelist: list, 
    name: List = ["Chr", "Start"]
    ) -> pd.DataFrame:

    """\
    Read .qbed file.

    :param filelist: 
        List containing all the pd.DataFrames need to be combined.
    :param name: 
        Name of the first two colums. Default is ["Chr", "Start"].

    :Returns:
        pd.DataFrame after combined.

    :example:
    >>> import pycallingcards as cc
    >>> P10 = cc.rd.read_qbed("https://github.com/The-Mitra-Lab/pycallingcards_data/releases/download/data/SP1_P10.txt")
    >>> P28 = cc.rd.read_qbed("https://github.com/The-Mitra-Lab/pycallingcards_data/releases/download/data/SP1_P28.txt")
    >>> qbed = cc.rd.combine_qbed([P10,P28])
    """

    return pd.concat(filelist).sort_values(by=name).reset_index(drop = True)

def read_rna(
    filename: str
):

    """\
    Read RNA file which column index is sample names and row index is gene names.

    :param filename: 
        Path to RNA file.

    :Returns:
        pd.DataFrame for the RNA file.

    :example:
    >>> import pycallingcards as cc
    >>> rna = cc.rd.read_rna("https://github.com/The-Mitra-Lab/pycallingcards_data/releases/download/data/dmso_MF.csv")

    """

    return pd.read_csv("dmso.csv", index_col = 0)



def save_qbed(
    file: pd.DataFrame,
    path: str
    ):

    """\
    Read .qbed file.

    :param file: 
        pd.Dataframe of the file
    :param path:
        Path to the qbed file.

    :example:
    >>> import pycallingcards as cc
    >>> qbed = cc.rd.read_qbed("https://github.com/The-Mitra-Lab/pycallingcards_data/releases/download/data/SP1_P10.txt")
    >>> qbed = cc.rd.save_qbed(qbed,"SP1_P10.txt")

       
    """

    file.to_csv(path,sep ="\t",header = None, index = None)


def save_bed(
    file: pd.DataFrame,
    path: str
    ):

    """\
    Read .qbed file.

    :param file: 
        pd.Dataframe of the file
    :param path:
        Path to the bed file.

    :example:
    >>> import pycallingcards as cc
    >>> SP1 = cc.rd.read_qbed("https://github.com/The-Mitra-Lab/pycallingcards_data/releases/download/data/SP1_P10.txt")
    >>> bed = cc.pp.callpeaks(SP1,  method = "CCcaller", reference = "mm10")
    >>> qbed = cc.rd.save_bed(bed,"SP1.bed")
       
    """

    file.to_csv(path,sep ="\t",header = None, index = None)
