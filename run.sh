#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

cd "$parent_path"
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 scrap_stock.py
deactivate
rm -r env