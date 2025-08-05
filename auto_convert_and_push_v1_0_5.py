import os
import json
import pandas as pd
from pathlib import Path
from github import Github
from dotenv import load_dotenv
from datetime import date

# Load .env
load_dotenv()

# Load config
with open("config.json") as f:
    config = json.load(f)

stock_csv = Path(config["stock_csv"])
barcode_txt = Path(config["barcode_txt"])
output_json = Path(config["output_json"])
github_repo = config["github_repo"]
target_path_in_repo = config["target_repo_path"]

# Load stock data
print(f"Loading: {stock_csv.name}")
stock_df = pd.read_csv(stock_csv, dtype=str).applymap(lambda x: x.strip() if isinstance(x, str) else x)
stock_df.columns = stock_df.columns.str.strip()

# Classify Stock Status
def classify_status(weeks):
    try:
        wks = float(weeks)
        if wks > 1:
            return "Green"
        elif 0 < wks <= 1:
            return "Amber"
        else:
            return "Red"
    except:
        return "Red"

stock_df["Stock Status"] = stock_df["Weeks of Stock (supplied)"].apply(classify_status)

# Load barcode data
print(f"Loading: {barcode_txt.name}")
barcode_df = pd.read_csv(barcode_txt, sep=",", dtype=str)
barcode_df.columns = barcode_df.columns.str.strip()
barcode_df = barcode_df.rename(columns={"Product Code": "Code", "Barcode 1": "barcode1"})
barcode_df = barcode_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Merge datasets
print("Merging on 'Code'...")
merged_df = pd.merge(stock_df, barcode_df, how="left", on="Code")

# Format JSON output
print("Formatting dashboard output...")
output_df = pd.DataFrame({
    "Product Name": merged_df.get("Product Name", ""),
    "Pack": merged_df.get("Pack", ""),
    "Code": merged_df.get("Code", ""),
    "barcode1": merged_df.get("barcode1", ""),
    "Stock Status": merged_df.get("Stock Status", ""),
    "On Order": merged_df.get("On Order", "").apply(lambda x: str(x).strip().lower() if pd.notna(x) else ""),
    "Last Updated": date.today().isoformat()
})


# Fully clean up the DataFrame before JSON conversion
output_df = output_df.replace([pd.NA, pd.NaT, None, float('nan')], "", regex=False)
output_df = output_df.fillna("")  # fill remaining NaNs
output_df = output_df.astype(str)  # convert all to strings

# Optional debug check:
# print(output_df.head(10).to_dict())

# Convert to JSON (no NaN will leak at this point)
json_data = output_df.to_dict(orient="records")

# Save to local file
print(f"Saving JSON: {output_json}")
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(json_data, f, indent=2)

# Upload to GitHub
print("Uploading to GitHub...")
token = os.getenv("GITHUB_TOKEN")
if not token:
    raise RuntimeError("GITHUB_TOKEN is missing from environment or .env file")

g = Github(token)
repo = g.get_repo(github_repo)

with open(output_json, "r", encoding="utf-8") as f:
    contents = f.read()

try:
    existing_file = repo.get_contents(target_path_in_repo)
    repo.update_file(
        existing_file.path,
        "v1.0.5: Final NaN-safe JSON output",
        contents,
        existing_file.sha
    )
    print("Updated existing file on GitHub.")
except Exception:
    repo.create_file(
        target_path_in_repo,
        "Initial stock JSON upload (v1.0.5)",
        contents
    )
    print("Created new file on GitHub.")
