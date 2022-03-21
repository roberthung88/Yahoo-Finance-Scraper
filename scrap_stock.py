import pandas as pd
import yfinance as yf

def main():
    input_str = input("Enter stock tick symbols: ")
    thread = input("Use Multithreading for Mass Downloads? Enter 1 (Yes) or 0 (No): ")
    # checking for valid input
    while(True):
        try:
            thread = int(thread)
            if thread != 0 and thread != 1:
                raise Exception('Invalid Input')
            break
        except:
            print("Invalid Multithreading Selection!")

        thread = input("Use Multithreading for Mass Downloads? Enter 1 (Yes) or 0 (No): ")
    print()
    print("Checking for Symbol Validity... ")
    todays_data =  yf.download(input_str, period="1d", threads=thread)
    todays_data = todays_data.dropna(axis=1)
    todays_data = todays_data.drop(['Adj Close', 'Volume'], axis=1)
    todays_data.columns = todays_data.columns.swaplevel(0, 1)
    todays_data.sort_index(level=0, axis=1, inplace=True)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(todays_data)
    todays_data.to_csv("result.csv")


if __name__ == "__main__":
    main()