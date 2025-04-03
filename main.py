import argparse

import pandas as pd

from src import chunker


def run_chunker_example(chunk_size, repeat_size):
    dfs = pd.date_range("2023-01-01 00:00:00", "2023-01-01 00:00:05", freq="s")
    df = pd.DataFrame({"dt": dfs.repeat(repeat_size)})

    for chunk in chunker.chunk_df(df, chunk_size=chunk_size, chunk_column="dt", sort=True):
        print(chunk)


def main():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION]",
        description="Dataframe chunker"
    )
    parser.add_argument(
        "-e", "--example", help="Run chunker example", action='store_true'
    )
    parser.add_argument(
        "-c", "--chunk", help="Set chunk size", default=4, type=int
    )
    parser.add_argument(
        "-r", "--repeat", help="Set dataframe repeat size", default=3, type=int
    )
    args = parser.parse_args()

    if args.example:
        run_chunker_example(args.chunk, args.repeat)


if __name__ == "__main__":
    main()
