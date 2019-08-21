import csv

FR = open("test.csv", "r")
data_frame = csv.reader(FR, delimiter=',', quotechar='"')
row_count = 0
for row in data_frame:
    row_count = row_count + 1
    if row_count == 1:
        continue
    new_row = row
    bmi = float(row[2])*float(row[3])
    new_row.append(bmi)
    print new_row
FR.close()

