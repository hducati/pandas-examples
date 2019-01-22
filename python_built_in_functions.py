import pandas as pd

"""
You can work with built in functions from python and
use it with pandas library

Example:    max(csv_file)
            min(csv_file)
            sorted(csv_file)
"""

csv_file = pd.read_csv("csv_files\pokemon.csv", usecols=['Name'], squeeze=True)
print(sorted(csv_file))
