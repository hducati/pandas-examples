import pandas as pd


def main():

    """
    By default, the squeeze method is False, when changed to True,
    we are specifying we want a pandas Series not a pandas DataFrame
    """

    file = pd.read_csv("csv_files\pokemon.csv", usecols=['Name'], squeeze=True)
    print(file)


if __name__ == "__main__":
    main()
