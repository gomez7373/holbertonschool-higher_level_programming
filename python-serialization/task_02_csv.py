#!/usr/bin/env python3

import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)

        with open('data.json', 'w') as json_file:
            json.dump(rows, json_file)

        return True
    except Exception as e:
        print(f"Error during CSV to JSON conversion: {e}")
        return False
