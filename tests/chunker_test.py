import pytest
import pandas as pd

from src import chunker


def test_empty_dataframe(empty_df):
    chunks = list(chunker.chunk_df(empty_df, chunk_size=2))
    assert len(chunks) == 1, "On empty df return itself"
    assert chunks[0].empty


@pytest.mark.parametrize("chunk_size,expected_chunks", [
    (2, 2),
    (3, 2),
    (6, 1),
])
def test_chunk_sizes(sample_df, chunk_size, expected_chunks):
    chunks = list(chunker.chunk_df(sample_df, chunk_size=chunk_size))
    assert len(chunks) == expected_chunks, f"For chunk_size - {chunk_size} expected - {expected_chunks}"


def test_zero_chunk_size(sample_df):
    with pytest.raises(ValueError):
        list(chunker.chunk_df(sample_df, chunk_size=0))


def test_sorting_w_unordered_df(unordered_df):
    # Check for sorting within chunks
    chunks = list(chunker.chunk_df(unordered_df, chunk_size=6, sort=True))
    for chunk in chunks:
        sorted_chunk = chunk.sort_values(by="dt")
        pd.testing.assert_frame_equal(
            chunk.reset_index(drop=True),
            sorted_chunk.reset_index(drop=True),
            check_like=True
        )
