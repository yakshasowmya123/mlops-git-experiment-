
import unittest
from vegetable_ci import calculate_sales_amount, load_vegetable_dataset


class TestVegetableCI(unittest.TestCase):

    def test_sales_amount_calculation(self):
        result = calculate_sales_amount(10, 25)
        self.assertEqual(result, 250)

    def test_negative_quantity_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_sales_amount(-5, 25)

    def test_dataset_contains_at_least_500_records(self):
        df = load_vegetable_dataset()
        self.assertGreaterEqual(len(df), 500)

    def test_dataset_has_required_columns(self):
        df = load_vegetable_dataset()

        required_columns = {
            "Vegetable",
            "Quantity_kg",
            "Price_per_kg",
            "Demand"
        }

        self.assertTrue(
            required_columns.issubset(set(df.columns))
        )


if __name__ == "__main__":
    unittest.main()
