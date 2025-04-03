from datetime import datetime

import pytest
import pandas as pd
import numpy as np


@pytest.fixture
def sample_df():
    dates = pd.date_range("2023-01-01 00:00:01", "2023-01-01 00:00:03", freq="s")
    return pd.DataFrame({"dt": dates.repeat([1, 2, 3])})


@pytest.fixture
def empty_df():
    return pd.DataFrame(columns=["dt"])


@pytest.fixture
def unordered_df():
    start = datetime(year=2023, month=1, day=1, hour=0, minute=0)
    end = datetime(year=2023, month=1, day=1, hour=0, minute=1)
    return pd.DataFrame({"dt": [np.random.choice(pd.date_range(start, end, freq="s")) for _ in range(100)]})
