"""A script to process book data."""

from argparse import ArgumentParser

import pandas as pd

def file_number_args() -> str:
    """Sets up the argument of which raw file number the user wishes to access, and 
    None if no argument is given by the user."""

    parser = ArgumentParser()
    parser.add_argument("--filenumber")
    args = parser.parse_args()

    file_number = args.filenumber

    return file_number


def merge_authors_df_w_raw_df(author_input: pd.DataFrame,
                              raw_input: pd.DataFrame) -> pd.DataFrame:
    """
    Given a pd.DataFrame object with authors data, and a pd.DataFrame 
    object with raw data, returns the two objects merged into a single 
    pd.DataFrame object.
    """

    result = pd.merge(author_input, raw_input, how="inner", on="author_id")

    return result


def drop_irrelevant_columns(combined_input: pd.DataFrame) -> pd.DataFrame:
    """
    Given our merged pd.DataFrame object, drops all columns not needed, while
    renaming relevant columns as required.
    """

    combined_input = combined_input[['book_title', 'name',
                             'Year released', 'Rating', 'ratings']]

    result = combined_input.rename(columns={'name': 'author_name',
                           'book_title': 'title', 
                           'Year released': 'year',
                           'Rating': 'rating'})

    return result


def assign_col_dtype(combined_input: pd.DataFrame) -> pd.DataFrame:
    """Given our merged pd.DataFrame object with relevant renamed columns, we assign
    appropriate data types to each column."""

    combined_input['rating'] = combined_input['rating'].str.replace(',', '.')

    combined_input['ratings'] = combined_input['ratings'].str.replace('`', '')

    combined_input['year'] = combined_input['year'].astype('int64')

    combined_input['rating'] = combined_input['rating'].astype('float64')

    combined_input['ratings'] = combined_input['ratings'].astype('int64')

    return combined_input


def drop_null_values(combined_input: pd.DataFrame) -> pd.DataFrame:
    """Given our merged pd.DataFrame object, we drop all rows with null values."""

    combined_input.dropna(inplace=True)

    return combined_input


def remove_bracketed_text(str_input: str) -> str:
    """Given a string with bracketed text, returns the string without this text."""

    str_input_bracket_split = str_input.split("(")

    return str_input_bracket_split[0]


if __name__ == "__main__":

    raw_file_number = file_number_args()

    if raw_file_number is None:

        raw_file_number = "0"

    raw_file_path = f"./data/RAW_DATA_{raw_file_number}.csv"

    authors_df = pd.read_csv("./data/AUTHORS.csv")

    raw_df = pd.read_csv(raw_file_path)

    combined_df = merge_authors_df_w_raw_df(authors_df, raw_df)

    combined_df_cleaned_col = drop_irrelevant_columns(combined_df)

    combined_df_formatted_col = assign_col_dtype(combined_df_cleaned_col)

    combined_df_final = drop_null_values(combined_df_formatted_col)

    combined_df_final['title'] = combined_df_final['title'].apply(
        remove_bracketed_text)

    combined_df_final_sorted = combined_df_final.sort_values(by=['rating'],
                                                             ascending=False)

    combined_df_final_sorted.to_csv('PROCESSED_DATA.csv', index=False)
