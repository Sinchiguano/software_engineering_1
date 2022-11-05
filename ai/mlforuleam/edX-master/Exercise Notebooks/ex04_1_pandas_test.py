import pandas as pd

def test_year_max_std(func, ratings):
    assert func(ratings) == 1998, "Error: wrong year identified"
