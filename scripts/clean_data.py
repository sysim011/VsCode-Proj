import pandas as pd

def clean_sales_data(input_path: str, output_path: str) -> None:
    df = pd.read_csv(input_path)

    df["date"] = pd.to_datetime(df["date"])
    df["sales"] = df["quantity"] * df["unit_price"]
    df["month"] = df["date"].dt.to_period("M")

    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    clean_sales_data(
        "data/sample_sales.csv",
        "outputs/cleaned_sales.csv"
    )