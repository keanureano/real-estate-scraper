import pandas as pd


def main():
    # Assuming you have two CSV files: french.csv and arabic.csv
    df_french = pd.read_csv("output.csv")
    df_arabic = pd.read_csv("output (1).csv")

    # Merge dataframes on ID columns
    df_merged = pd.merge(
        df_french,
        df_arabic,
        on=["ID_City", "ID_District", "ID_Town"],
        suffixes=("_French", "_Arabic"),
        how="outer",
    )

    # Remove columns starting with "ID_"
    columns_to_drop = [col for col in df_merged.columns if col.startswith("ID_")]
    df_result = df_merged.drop(columns=columns_to_drop)

    # Reorder columns
    columns_order = [
        "City_French",
        "City_Arabic",
        "District_French",
        "District_Arabic",
        "Town_French",
        "Town_Arabic",
    ]

    df_result = df_result[columns_order]

    # Save the result to a new CSV file
    df_result.to_csv("final_output.csv", index=False, encoding="utf-8-sig")


if __name__ == "__main__":
    main()
