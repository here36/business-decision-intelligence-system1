import pandas as pd
import os

def load_data():
    """
    Loads the cleaned Excel dataset and converts date columns.
    Returns:
        pandas.DataFrame
    """

    current_dir = os.path.dirname(__file__)

    file_path = os.path.join(
        current_dir,
        "..",
        "data",
        "superstore_clean.xlsx"
    )

    df = pd.read_excel(file_path)

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        origin="1899-12-30",
        unit="D"
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        origin="1899-12-30",
        unit="D"
    )

    return df