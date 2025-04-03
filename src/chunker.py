from typing import Generator

import pandas as pd


def chunk_df(
    df: pd.DataFrame,
    chunk_size: int,
    chunk_column: str = "dt",
    sort: bool = False
) -> Generator[pd.DataFrame, None, None]:
    """
    Generates a series of dataframe chunks.
    Final chunk size depends on passed data and can be bigger than initial chunk_size
    if there's a continuous series of repeating values in dataframe.

    :param df: pd.DataFrame
        Input dataframe.
    :param chunk_size: int
        Chunk size to split dataframe.
    :param chunk_column: str, default "dt"
        Column name to use at chunker base.
    :param sort: bool, default False
        Flag to set dataframe sort.

    :return: Generator[pd.DataFrame, None, None]
    """

    # prevent passing incorrect chunk size
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")

    # initial dataframe size check to prevent unnecessary processing
    if df.empty:
        yield df
        return
    elif len(df) <= chunk_size:
        yield df.sort_values(by=chunk_column) if sort else df
        return

    # group df by `chunk_column` to get all indexes
    # added `sort` not to run sort on each returned chunk if it's needed
    grouped_df = df.groupby(chunk_column, sort=sort)

    chunk_indexes = []

    for _, group_indexes in grouped_df.groups.items():
        chunk_indexes += list(group_indexes)

        if len(chunk_indexes) >= chunk_size:
            yield df.loc[chunk_indexes]
            chunk_indexes = []

    # check for last groups iteration not to miss last group
    if chunk_indexes:
        yield df.loc[chunk_indexes]
