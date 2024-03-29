import pandas as pd
import unittest
from datetime import datetime
from nomiden import nik

int_nik = [1101016401640000, 1101013101000000]
str_nik = ["1101016401640000", "1101013101000000"]

class TestNIK(unittest.TestCase):
    def test_invalid_idnum_error(self):
        idnum_15 = 101014101000000
        idnum_17 = 11101014101000000

        with self.assertRaises(ValueError):
            nik._check_length(idnum_15)
            nik._check_length(idnum_17)

    def test_valid_idnum(self):
        for idnum in int_nik:
            valid_idnum = nik._check_length(idnum)
            self.assertEqual(len(valid_idnum), 16)
        for idnum in str_nik:
            valid_idnum = nik._check_length(idnum)
            self.assertEqual(len(valid_idnum), 16)

    def test_nik_province(self):
        for idnum in int_nik:
            prov = nik.province(idnum)
            self.assertIsInstance(prov, str)
        for idnum in str_nik:
            prov = nik.province(idnum)
            self.assertIsInstance(prov, str)

    def test_nik_city(self):
        for idnum in int_nik:
            city = nik.city(idnum)
            self.assertIsInstance(city, str)
        for idnum in str_nik:
            city = nik.city(idnum)
            self.assertIsInstance(city, str)

    def test_nik_district(self):
        for idnum in int_nik:
            dist = nik.district(idnum)
            self.assertIsInstance(dist, str)
        for idnum in str_nik:
            dist = nik.district(idnum)
            self.assertIsInstance(dist, str)

    def test_nik_gender(self):
        for idnum in int_nik:
            gend = nik.gender(idnum)
            self.assertIsInstance(gend, str)
            self.assertIn(gend, {'Male', 'Female'})
        for idnum in str_nik:
            gend = nik.gender(idnum)
            self.assertIsInstance(gend, str)
            self.assertIn(gend, {'Male', 'Female'})
    
    def test_nik_birthdate(self):
        for idnum in int_nik:
            bdate = nik.birthdate(idnum)
            self.assertIsInstance(bdate, int)
        for idnum in str_nik:
            bdate = nik.birthdate(idnum)
            self.assertIsInstance(bdate, int)

    def test_nik_birthmonth(self):
        for idnum in int_nik:
            bmonth = nik.birthmonth(idnum)
            self.assertIsInstance(bmonth, int)
        for idnum in str_nik:
            bmonth = nik.birthmonth(idnum)
            self.assertIsInstance(bmonth, int)

    def test_nik_birthyear(self):
        for idnum in int_nik:
            byear = nik.birthyear(idnum)
            self.assertIsInstance(byear, int)
        for idnum in str_nik:
            byear = nik.birthyear(idnum)
            self.assertIsInstance(byear, int)

    def test_nik_birthdtm(self):
        for idnum in int_nik:
            bdtm = nik.birthdtm(idnum)
            self.assertIsInstance(bdtm, datetime)
        for idnum in str_nik:
            bdtm = nik.birthdtm(idnum)
            self.assertIsInstance(bdtm, datetime)

    def test_nik_birthday(self):
        for idnum in int_nik:
            bday = nik.birthday(idnum)
            self.assertIsInstance(bday, str)
        for idnum in str_nik:
            bday = nik.birthday(idnum)
            self.assertIsInstance(bday, str)

    def test_nik_age(self):
        for idnum in int_nik:
            age = nik.age(idnum)
            self.assertIsInstance(age, int)
        for idnum in str_nik:
            age = nik.age(idnum)
            self.assertIsInstance(age, int)

    def test_nik_nthperson(self):
        for idnum in int_nik:
            nth = nik.nth_person(idnum)
            self.assertIsInstance(nth, int)
        for idnum in str_nik:
            nth = nik.nth_person(idnum)
            self.assertIsInstance(nth, int)

    def test_nik_nikreader(self):
        for idnum in int_nik:
            nik_dict = nik.all_info(idnum)
            self.assertIsInstance(nik_dict, dict)
        for idnum in str_nik:
            nik_dict = nik.all_info(idnum)
            self.assertIsInstance(nik_dict, dict)

if __name__ == '__main__':
    unittest.main()