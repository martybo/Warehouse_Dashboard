import json
import math

# Path to your JSON file
json_path = "StockDashboardData.json"

def is_nan(value):
    return isinstance(value, float) and math.isnan(value)

def validate_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            print("❌ JSON root is not a list.")
            return

        invalid_entries = []

        for i, item in enumerate(data):
            if not isinstance(item, dict):
                invalid_entries.append((i, "Not a dictionary", item))
                continue

            for key, value in item.items():
                if is_nan(value):
                    invalid_entries.append((i, key, value))

        if invalid_entries:
            print(f"❌ Found {len(invalid_entries)} invalid entries with NaN values:")
            for entry in invalid_entries:
                print(f"  Row {entry[0]}, Key '{entry[1]}': Value = {entry[2]}")
        else:
            print("✅ JSON is valid and contains no NaN values.")

    except json.JSONDecodeError as e:
        print(f"❌ JSON decoding error: {e}")
    except FileNotFoundError:
        print("❌ File not found.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Run the validator
validate_json(json_path)
