from dataclasses import dataclass
from typing import List
import json


def read_config(conf_loc="config/config.json"):
    """
    Helper method used to parse config
    :param conf_loc: str of directory
    :return: Config class
    """
    with open(conf_loc) as json_file:
        data = json.load(json_file)
        return Config(**data)


@dataclass
class Config:
    """
    Class used to map configurations values from config file
    """
    postgres_host: str
    postgres_password: str
    postgres_db: str
    postgres_table_name: str
    postgres_user: str
    epc_data_url: str
    data_columns: List[str]
