"""A script to analyse book data."""

import pandas as pd
import altair as alt


def extract_decade_from_year(year: int) -> int:
    """Given a year, returns its decade."""
    pass


def create_decades_list(year_input: pd.Series) -> list[int]:
    """
    Given a pd.Series object containing years, return a list, where
    elements are distinct, and each element is a year corresponding to the decade
    of every year in the input
    """
    pass


def create_decade_releases_png(year_input: pd.Series) -> None:
    """
    Given a pd.Series object containing years, return a pie chart in a .png
    format, where each colour corresponds to a decade, and the angle of each
    sector corresponds to the number of books released in that decade.
    """
    pass


def create_top_authors_png(authors_input: pd.Series) -> None:
    """
    Given a pd.Series object containing author's names, return a sorted
    bar chart, where the x-axis has names of the ten most-rated authors, and
    the y-axis has the total number of ratings for each author.
    """
    pass


if __name__ == "__main__":
    
    all_data = pd.read_csv("PROCESSED_DATA.csv")

