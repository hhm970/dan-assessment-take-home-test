"""A script to process book data."""

from argparse import ArgumentParser

import pandas as pd

def args() -> str | None:
    """Sets up the argument of which raw file number the user wishes to access, and 
    None if no argument is given by the user."""
    pass


def merge_authors_df_w_raw_df(author_input: pd.DataFrame, 
                              raw_input: pd.DataFrame) -> pd.DataFrame:
    """
    Given a pd.DataFrame object with authors data, and a pd.DataFrame 
    object with raw data, returns the two objects merged into a single 
    pd.DataFrame object.
    """
    pass


def drop_irrelevant_columns(combined_input: pd.DataFrame) -> pd.DataFrame:
    """Given our merged pd.DataFrame object, drops all columns not needed."""
    pass


def assign_col_dtype(combined_input: pd.DataFrame) -> pd.DataFrame:
    """Given our merged pd.DataFrame object with relevant columns, we assign
    appropriate data types to each column."""
    pass


def drop_null_values(combined_input: pd.DataFrame) -> pd.DataFrame:
    """Given our merged pd.DataFrame object, we drop all rows with null values."""
    pass


def remove_bracketed_text(str_input: str) -> str:
    """Given a string with bracketed text, returns the string without this text."""
    pass


if __name__ == "__main__":

    authors_df = pd.read_csv("./data/AUTHORS.csv")

    raw_df = pd.read_csv("./data/RAW_DATA_0.csv")
