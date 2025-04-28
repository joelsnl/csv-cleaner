import pandas as pd

def clean_csv(input_file, output_file):
    df = pd.read_csv(input_file)
    df.drop_duplicates(inplace=True)
    df.fillna("N/A", inplace=True)
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    df.to_csv(output_file, index=False)
    print(f"Cleaned CSV saved to {output_file}")

if __name__ == "__main__":
    clean_csv("input.csv", "cleaned_output.csv")
