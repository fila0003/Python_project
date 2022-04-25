# autor Evgenii Filatov
# 21F_CST8333_350 

import uuid
from global_var import VaccineCoverage
import global_var

class CRUD:
    def __init__(self, dao) -> None:
        self.dao = dao
    
    def deleteRecord(self,recNum):
        self.dao.delete(recNum)

    def printVacc(self, recNumStart=0, recNumEnd=100):
        headers,records = self.dao.read()
        output = ""
        output += '|'.join(headers)
        output += "\n"
        for idx, record in enumerate(records):
            if idx >= recNumStart and idx <= recNumEnd:
                output += str(idx) + ' ' + str(record)
                output += "\n"
        return output

        #Business Method for add rows into the table
    def addRecord(self, id=str(uuid.uuid4()), pruid = "", prename = "", prfname = "", week_end = "", product_name = "", 
                    numtotal_atleast1dose = "", numtotal_partially = "", numtotal_fully = "",
                    prop_atleast1dose = "", prop_partially = "", prop_fully = ""):
        vaccineRecord = global_var.VaccineCoverage(id, pruid, prename, prfname, week_end, product_name, numtotal_atleast1dose, 
                    numtotal_partially, numtotal_fully, prop_atleast1dose,  prop_partially,prop_fully)  
        self.dao.add(vaccineRecord)

        #Business Method for edit rows

    def editRecord(self, recNum, pruid="", prename="", prfname="", week_end="", product_name="",
                   numtotal_atleast1dose="", numtotal_partially="", numtotal_fully="",
                   prop_atleast1dose="", prop_partially="", prop_fully=""):
        a = global_var.VaccineCoverage()
        a._pruid = pruid or a._pruid
        a._prename = prename or a._prename
        a._prfname = prfname or a._prfname
        a._week_end = week_end or a._week_end
        a._product_name = product_name or a._product_name
        a._numtotal_atleast1dose = numtotal_atleast1dose or a._numtotal_atleast1dose
        a._numtotal_partially = numtotal_partially or a._numtotal_partially
        a._numtotal_fully = numtotal_fully or a._numtotal_fully
        a._prop_atleast1dose = prop_atleast1dose or a._prop_atleast1dose
        a._prop_partially = prop_partially or a._prop_partially
        a._prop_fully = prop_fully or a._prop_fully
    
        self.dao.update(global_var.VaccineCoverage (str(recNum),
            str(a._pruid) ,
            str(a._prename),
            str(a._prfname),
            str(a._week_end),
            str(a._product_name),
            str(a._numtotal_atleast1dose),
            str(a._numtotal_partially),
            str(a._numtotal_fully),
            str(a._prop_atleast1dose),
            str(a._prop_partially),
            str(a._prop_fully) 
        )
        )

    # This function  for users to read  vaccine table
    
    def printCustomVacc (self, columnList,recNumStart,recNumEnd ):
        headers,records = self.dao.customRead(columnList)
        output = ""
        output += '|'.join(headers)
        output += "\n"
        for idx, record in enumerate(records):
            if idx >= recNumStart and idx <= recNumEnd:
                output += str(idx) + ' ' + str(record)
                output += "\n"
        return output   
  

        