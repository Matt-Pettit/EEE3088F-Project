import csv
from tabulate import tabulate

with open('BOM.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    headers = next(reader)
    rows = [row for row in reader]
    print(tabulate(rows, headers=headers, tablefmt='plain'))

