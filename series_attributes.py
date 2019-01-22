import pandas as pd

"""
    Some examples of usage from series attributes:

    You can check all the values on a pandas Series by use the following:
    Example:    pokemon.values

    Or check the index values.
    Example:    pokemon.index

    Check if there are any duplicates:
    Example:    pokemon.is_unique

    Number of dimension:
    Example:    pokemon.ndim
    If it's 1, then you're working with a Series object
    Otherwise, you're working with a DataFrame

    Total of elements and cells:
    Example:    pokemon.size

    Check the name or change:
    Example:    pokemon.name
"""

pokemon = pd.read_csv("csv_files\pokemon.csv", usecols=['Name'], squeeze=True)
print(pokemon.size)
