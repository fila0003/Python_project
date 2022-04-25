# autor Evgenii Filatov
# 21F_CST8333_350 

import csv
from io import StringIO
from os import urandom
import sys
import global_var
import uuid


fileVac = r"C:\Users\Filat\Desktop\4 term AC\Python\Assignment4\Assignment4\vaccination-coverage-byVaccineType.csv"


    #Persistance method for update.
def loadFromFile():   
    try: 
        file = open(fileVac)
    except FileNotFoundError:
        print("The file does not exists.")
    except IOError:
        print("Problem opening file.")
        sys.exit()

    global_var.vaccineRecords.clear()
    global_var.listOfHeaders.clear()

    csvreader = csv.reader(file)
    tableHeaders = next(csvreader)  

        # This is a loop  for list of headers for 11 columns

    for i in range(0, 11):
        #global_var.listOfHeaders.append(tableHeaders[i])
        pass   
    
    # This is a loop  reading records from the csv-file.

    records = []
    for row in csvreader:
        id = uuid.uuid4()

        vaccineRecord = global_var.VaccineCoverage(id,row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
        #   global_var.vaccineRecords.append(vaccineRecord)
        records.append(vaccineRecord)
        

    # file output
    file.close()
    return records
    
      #Persistance method for saving
def saveToFile():
    f = open(fileVac, "w")
    f.write(','.join(global_var.listOfHeaders))
    
    for record in global_var.vaccineRecords:
        f.write(str(record))
        f.write('\n')

    f.close()