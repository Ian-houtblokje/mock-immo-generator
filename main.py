import numpy as np
import pandas as pd
from config import CSV_PATH, N_ROWS
from generator import genereer_panden
import os
from pathlib import Path 


def main():
    data = genereer_panden(N_ROWS)
    df = pd.DataFrame(data)

    #sample als 1e check
    print("Sample of generated properties:")
    print(df.head(10))

    csv_file = f"{CSV_PATH}.csv"
    try:
        df.to_csv(csv_file, index=False)
        print(f"\nDataset saved to: {csv_file}")
    except PermissionError:
        # try fallback to user's Documents folder
        alt_path = Path.home() / "Documents" / f"{CSV_PATH}.csv"
        try:
            df.to_csv(alt_path, index=False)
            print(f"\nPermission denied writing to cwd; dataset saved to: {alt_path}")
        except PermissionError:
            print("Permission denied when saving CSV. Close any program locking the file or set CSV_PATH to a writable location.")

if __name__ == "__main__":
    main()