import os
import csv

messages=["2020-02-04 4", 
          "2020-02-04 3", 
          "2020-02-04 4", 
          "2020-02-04 2", 
          "2020-02-04 1", 
          "2020-02-03 3", 
          "2020-02-03 2", 
          "2020-02-03 1", 
          "2020-02-03 2"]


dict = {}
keyList = [4, 3, 2, 1]

for elem in messages:

    keyValue = elem.split(" ")

    if keyValue[0] in dict:
        dict[keyValue[0]][int(keyValue[1])] +=1
    else:
        dict[keyValue[0]] = {k: 0 for k in keyList}
        dict[keyValue[0]][int(keyValue[1])] +=1
        print(dict)

print(dict)

output_path = os.path.join("new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Date', '4', '3', '2', '1'])

    # Write the second row
    for key, value in dict.items():
        newline = [key]
        for key, value1 in value.items():
            newline.append(value1)
        csvwriter.writerow(newline)