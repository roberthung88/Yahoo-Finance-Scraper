# Yahoo-Finance-Scraper

This python application scraps stock prices from Yahoo Finance using 3rd party library yfinance. It takes in one or more more stock tick symbols and returns each of the stocks’ high, low, open, and close prices today. Results are exported to a csv file **`result.csv`**.

## Installation and Usage

Simply run the script:

```bash
sh run.sh
```


Alternatively, run the following:

```bash
# creates python virtual environment
python3 -m venv env
source env/bin/activate

# installs requirements
pip install -r requirements.txt

# calls python file
python3 scrap_stock.py

# deactivates virtual environment
deactivate

# removes virual environment
rm -r env
```
The program will prompt for tick symbols. Please separate them with whitespace. It will also ask whether you'd like to utilize asynchronous multithreading for mass downloading. Please enter 1 (Yes) or 0 (No).

Alternatively, use input redirection. A test file **`input.txt`** is provided:
```bash
python3 scrap_stock.py < input.txt
```
