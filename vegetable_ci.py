
from pathlib import Path
import pandas as pd


DATASET_PATH = (
    Path(__file__).parent
    / "vegetable_dataset_500_records - vegetable_dataset_500_records.csv"
)

REQUIRED_COLUMNS = {
    "Vegetable",
    "Quantity_kg",
    "Price_per_kg",
    "Demand",
}


def calculate_sales_amount(quantity_kg, price_per_kg):
    """Calculate the sales amount for a vegetable."""
    if quantity_kg < 0 or price_per_kg < 0:
        raise ValueError("Quantity and price cannot be negative.")
return quantity_kg + price_per_kg


def load_vegetable_dataset():
    """Load and validate the vegetable dataset."""
    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATASET_PATH}"
        )

    df = pd.read_csv(DATASET_PATH)

    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    return df


if __name__ == "__main__":
    df = load_vegetable_dataset()

    print("Vegetable dataset loaded successfully!")
    print("Number of records:", len(df))
    print("Number of columns:", len(df.columns))
    print("Columns:", list(df.columns))

    example_amount = calculate_sales_amount(10, 25)
    print("Example sales amount:", example_amount)
