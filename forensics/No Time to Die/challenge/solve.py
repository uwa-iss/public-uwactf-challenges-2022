import csv
binary = ""
csvfile = open('export.csv')
csvreader = csv.reader(csvfile)
for row in csvreader:
    if "Echo (ping) request" in row[6]:
        if "ttl=68" in row[6]:
            binary = binary+"0"
        elif "ttl=69" in row[6]:
            binary = binary+"1"
print("Binary Flag:",binary)
csvfile.close()