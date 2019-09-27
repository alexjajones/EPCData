import time

from config_utils import read_config
from data_utils import get_epc_data, clean_data
from postgres import Postgres


def main():
    print("Reading configuration")

    config = read_config()

    print("Fetching data")

    raw_epc_data = get_epc_data(config.epc_data_url, True)

    print("Cleaning data")

    data = clean_data(raw_epc_data, config.data_columns)

    print("Writing data")

    # Wait for postgres to start ... should be handled at the infra level
    time.sleep(5)

    pg = Postgres(config)

    pg.write_data(data, config.postgres_table_name)

    print("Verifying data")

    print(pg.read_data())

    print("Complete")


if __name__ == "__main__":
    main()
