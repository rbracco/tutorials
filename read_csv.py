import csv
with open('data/daily.csv', newline="") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    #print(row["date"], row["positive"])
    print(row.keys())
    break