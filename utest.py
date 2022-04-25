import business as bus
import global_var
import unittest
from dao import dao

class TestDao(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        dao.add(global_var.VaccineCoverage("id","12","Example","Filatov","2021-05-08","AstraZeneca","42361","42359","2","4.33","4.33","0.00"))
        return super().setUpClass()
        
    #test for add new row in db
    #student  Filatov 

    def test_Dao_add(self):
        before = dao.cursor.execute( '''SELECT pruid FROM statistics WHERE id='new_id';''')
        self.assertIsNone(before.fetchone())
        dao.add(global_var.VaccineCoverage("new_id","new_pruid","Example","Filatov","2021-05-08","AstraZeneca","42361","42359","2","4.33","4.33","0.00"))
        after = dao.cursor.execute( '''SELECT pruid FROM statistics WHERE id='new_id';''')
        self.assertEqual( after.fetchone()[0], "new_pruid")

    #test update  row in db

    def test_Dao_update(self):
        before = dao.cursor.execute( '''SELECT pruid FROM statistics WHERE id='new_id';''')
        self.assertEqual(before.fetchone()[0], "new_pruid")
        dao.update(global_var.VaccineCoverage("new_id","new_new_pruid","Example","Filatov","2021-05-08","AstraZeneca","42361","42359","2","4.33","4.33","0.00"))
        after = dao.cursor.execute( '''SELECT pruid FROM statistics WHERE id='new_id';''')
        self.assertEqual( after.fetchone()[0], "new_new_pruid")

    #test delete  row from db

    def test_Dao_delete(self):
        before = dao.cursor.execute( '''SELECT pruid FROM statistics WHERE id='id';''')
        self.assertIsNotNone(before.fetchone()[0])
        dao.delete("id")
        after = dao.cursor.execute( '''SELECT pruid FROM statistics WHERE id='id';''')
        self.assertIsNone( after.fetchone())
        

   # def test_addRecord(self):
      # Test for array is empty

       # self.assertEqual (len (global_var.vaccineRecords), 0)

        # Test for array has records

       # bus.addRecord("12","Example","Filatov","2021-05-08","AstraZeneca","42361","42359","2","4.33","4.33","0.00")
       # self.assertEqual (len (global_var.vaccineRecords), 1)
        
        #test  correctness of record
      #  x = global_var.vaccineRecords[0]
      #  self.assertEqual (x._pruid, "12")



    


    
if __name__ == '__main__':
    unittest.main()   

