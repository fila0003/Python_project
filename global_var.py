# autor Evgenii Filatov
# 21F_CST8333_350 

vaccineRecords = []
listOfHeaders = []


class VaccineCoverage(): 

    #  create constructor for the table
    def __init__(self, id="1", pruid = "", prename = "", prfname = "", week_end = "", product_name = "", 
                numtotal_atleast1dose = "", numtotal_partially = "", numtotal_fully = "",
                prop_atleast1dose = "", prop_partially = "", prop_fully = ""):
            self._id = id
            self._pruid = pruid
            self._prename = prename
            self._prfname = prfname
            self._week_end = week_end 
            self._product_name = product_name 
            self._numtotal_atleast1dose = numtotal_atleast1dose 
            self._numtotal_partially = numtotal_partially 
            self._numtotal_fully = numtotal_fully 
            self._prop_atleast1dose = prop_atleast1dose
            self._prop_partially = prop_partially
            self._prop_fully = prop_fully

    # This method is similar to method toString in Java. Create output format.    
    def __repr__(self):
        return "{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}|{10}|{11}".format(
            self._id,
            self._pruid,self._prename,self._prfname,
            self._week_end,self._product_name,
            self._numtotal_atleast1dose,self._numtotal_partially,
            self._numtotal_fully,self._prop_atleast1dose,
            self._prop_partially,self._prop_fully)

    def __str__(self):
        return "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}".format(
            self._id,
            self._pruid,self._prename,self._prfname,
            self._week_end,self._product_name,
            self._numtotal_atleast1dose,self._numtotal_partially,
            self._numtotal_fully,self._prop_atleast1dose,
            self._prop_partially,self._prop_fully)
