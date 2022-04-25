# autor Evgenii Filatov
# 21F_CST8333_350

from os import truncate
import sqlite3
from sqlite3.dbapi2 import Cursor
from global_var import VaccineCoverage, vaccineRecords, listOfHeaders
import persistance

class Dao :

    def __init__(self) -> None:
        self.connection = sqlite3.connect(r"C:\Users\Filat\Desktop\4 term AC\Python\Assignment2+demo\CST8333Assignment2ByEvgeniiFilatov\vacination.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create()
        self.truncate()
        result = persistance.loadFromFile()
        for i in result: 
            self.add(i)
    
    def create (self) -> None:
        create_query = '''CREATE TABLE IF NOT EXISTS statistics(
            id TEXT NOT NULL UNIQUE,
            pruid TEXT,
            prename TEXT,
            prfname TEXT,
            week_end TEXT,
            product_name TEXT,
            numtotal_atleast1dose TEXT,
            numtotal_partially TEXT,
            numtotal_fully TEXT,
            prop_atleast1dose TEXT,
            prop_partially TEXT,
            prop_fully TEXT);'''

        self.cursor.execute(create_query)
        self.connection.commit()

    def truncate(self) -> None:
        truncateQuery = '''DELETE FROM statistics;'''
        self.cursor.execute(truncateQuery)
        self.connection.commit()
       


    def add (self,vaccineCoverage:VaccineCoverage)->None:
        addQuery = '''INSERT INTO statistics ( 
            id,
            pruid,
            prename,
            prfname,
            week_end,
            product_name,
            numtotal_atleast1dose,
            numtotal_partially,
            numtotal_fully,
            prop_atleast1dose,
            prop_partially,
            prop_fully) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);
            '''
        self.cursor.execute(addQuery, (
            str(vaccineCoverage._id),
            vaccineCoverage._pruid,
            vaccineCoverage._prename,
            vaccineCoverage._prfname,
            vaccineCoverage._week_end,
            vaccineCoverage._product_name,
            vaccineCoverage._numtotal_atleast1dose,
            vaccineCoverage._numtotal_partially,
            vaccineCoverage._numtotal_fully,
            vaccineCoverage._prop_atleast1dose,
            vaccineCoverage._prop_partially,
            vaccineCoverage._prop_fully))
        self.connection.commit()

    def update (self,vaccineCoverage: VaccineCoverage)->None:
        updateQuery = '''
        UPDATE statistics 
        set pruid=?, prename=?, prfname=?, week_end=?, product_name=?,
        numtotal_atleast1dose=?,
        numtotal_partially=?,
        numtotal_fully=?,
        prop_atleast1dose=?,
        prop_partially=?,
        prop_fully=?
        WHERE id=?;
        '''
        self.cursor.execute(updateQuery, ( 
            vaccineCoverage._pruid,
            vaccineCoverage._prename,
            vaccineCoverage._prfname,
            vaccineCoverage._week_end,
            vaccineCoverage._product_name,
            vaccineCoverage._numtotal_atleast1dose,
            vaccineCoverage._numtotal_partially,
            vaccineCoverage._numtotal_fully,
            vaccineCoverage._prop_atleast1dose,
            vaccineCoverage._prop_partially,
            vaccineCoverage._prop_fully,
            str(vaccineCoverage._id)
            ))
        self.connection.commit()

    def delete (self,key)->None:
        deleteQuery = "DELETE FROM statistics WHERE id=?;"
        self.cursor.execute(deleteQuery,(str(key),))
        self.connection.commit()

    def read (self)->None:
        selectQuery = '''SELECT * FROM statistics;'''
        self.cursor.execute(selectQuery)

        records = []
        for row in self.cursor.fetchall(): 
            records.append(VaccineCoverage(
            row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))

        headers = []
        names = list(map(lambda x: x[0], self.cursor.description))
        for columnName in names:
            headers.append(columnName)
        return headers,records

    #  DAO customer function for search records based on multiple columns at same time

    def customRead (self, columnList)->None:
        
        selectQuery ='''SELECT ''' + columnList + ''' FROM statistics;'''
        self.cursor.execute(selectQuery)

        records = []
        for row in self.cursor.fetchall(): 
            print(row)
            values = []
            for i in row:
                values.append(i)
            print (values)
            valuesMap = dict(zip(columnList.split(","),values))
            record = VaccineCoverage()
            for i in valuesMap:
                vM = valuesMap.get(i)
                exec(f"record._{i} = \"{vM}\"")
                
            records.append(record)

        headers = columnList.split(",")
        return headers,records








         
