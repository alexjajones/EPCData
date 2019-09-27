from typing import List

import requests, zipfile
from io import BytesIO, StringIO
import pandas as pd


def get_epc_data(zip_file_url: str, local: bool) -> pd.DataFrame:
    """
    Takes the local of the epc data and outputs a string
    :param zip_file_url: location of file
    :param local: Whether or not file is local
    :return: string of certificates file
    """
    if local:
        archive = zipfile.ZipFile(zip_file_url, 'r')
    else:
        file = requests.get(zip_file_url, stream=True).content
        archive = zipfile.ZipFile(StringIO(file))

    data = archive.open('certificates.csv').read()

    return pd.read_csv(BytesIO(data), encoding='utf8', sep=",")


def clean_data(csv: pd.DataFrame, data_columns: List[str]) -> pd.DataFrame:
    """
    Takes a pandas data frame and picks data columns
    :param csv: raw pd
    :param data_columns: columns to filter
    :return:
    """
    return csv[data_columns]
