import pandas as pd


def main():
    games_list = ["Farcry", "Dark Souls", "Crash", "Bloodborne", "NioH"]
    weekdays_list = ["Monday", "Day", "Wednesday", "Day", "Friday"]

    print(pd.Series(games_list, index=weekdays_list))


if __name__ == "__main__":
    main()
