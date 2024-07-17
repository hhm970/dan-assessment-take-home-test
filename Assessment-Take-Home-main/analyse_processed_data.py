"""A script to analyse book data."""

import pandas as pd
import altair as alt


def extract_decade_from_year(year: int) -> int:
    """Given a year, returns its decade."""

    result = (year // 10) * 10

    return result


def create_decade_releases_png(year_input: pd.Series) -> None:
    """
    Given a pd.Series object containing years, return a pie chart in a .png
    format, where each colour corresponds to a decade, and the angle of each
    sector corresponds to the number of books released in that decade.
    """
    
    decades_series = year_input.apply(extract_decade_from_year)

    data = decades_series.value_counts().reset_index()

    data = data.rename(columns={'year': 'Decade'})

    chart = alt.Chart(data, title="Book Releases by Decade").mark_arc().encode(
        color='Decade:N',
        theta='count:Q'
    )

    chart.save('decade_releases.png')


def create_top_authors_png(authors_input: pd.Series) -> None:
    """
    Given a pd.Series object containing author's names, return a sorted
    bar chart, where the x-axis has names of the ten most-rated authors, and
    the y-axis has the total number of ratings for each author.
    """

    data = authors_input.value_counts().reset_index()

    data = data.rename(columns={'author_name': 'Author'})

    top_ten_data = data.iloc[[str(i) for i in range(10)]]

    chart = alt.Chart(top_ten_data, title='Top Authors Read').mark_bar().encode(
        x=alt.X('Author:N').sort('-y'),
        y='count:Q',
        color='Author:N'
    )

    chart.save('top_authors.png')


if __name__ == "__main__":
    
    all_data = pd.read_csv("PROCESSED_DATA.csv")

    create_decade_releases_png(all_data['year'])

    create_top_authors_png(all_data['author_name'])
