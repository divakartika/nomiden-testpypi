import pandas as pd
import unittest
from datetime import datetime
from nomiden import kk

int_kk = [1101011001640000, 1101013101000000]
str_kk = ["1101011001640000", "1101013101000000"]

class TestKK(unittest.TestCase):
    def test_invalid_idnum_error(self):
        idnum_15 = 101011101000000
        idnum_17 = 11101011101000000

        with self.assertRaises(ValueError):
            kk._check_length(idnum_15)
            kk._check_length(idnum_17)

    def test_valid_idnum(self):
        for idnum in int_kk:
            valid_idnum = kk._check_length(idnum)
            self.assertEqual(len(valid_idnum), 16)
        for idnum in str_kk:
            valid_idnum = kk._check_length(idnum)
            self.assertEqual(len(valid_idnum), 16)

    def test_kk_province(self):
        for idnum in int_kk:
            prov = kk.province(idnum)
            self.assertIsInstance(prov, str)
        for idnum in str_kk:
            prov = kk.province(idnum)
            self.assertIsInstance(prov, str)

    def test_kk_city(self):
        for idnum in int_kk:
            city = kk.city(idnum)
            self.assertIsInstance(city, str)
        for idnum in str_kk:
            city = kk.city(idnum)
            self.assertIsInstance(city, str)

    def test_kk_district(self):
        for idnum in int_kk:
            dist = kk.district(idnum)
            self.assertIsInstance(dist, str)
        for idnum in str_kk:
            dist = kk.district(idnum)
            self.assertIsInstance(dist, str)
    
    def test_kk_regdate(self):
        for idnum in int_kk:
            rdate = kk.regdate(idnum)
            self.assertIsInstance(rdate, int)
        for idnum in str_kk:
            rdate = kk.regdate(idnum)
            self.assertIsInstance(rdate, int)

    def test_kk_regmonth(self):
        for idnum in int_kk:
            rmonth = kk.regmonth(idnum)
            self.assertIsInstance(rmonth, int)
        for idnum in str_kk:
            rmonth = kk.regmonth(idnum)
            self.assertIsInstance(rmonth, int)

    def test_kk_regyear(self):
        for idnum in int_kk:
            ryear = kk.regyear(idnum)
            self.assertIsInstance(ryear, int)
        for idnum in str_kk:
            ryear = kk.regyear(idnum)
            self.assertIsInstance(ryear, int)

    def test_kk_regdtm(self):
        for idnum in int_kk:
            rdtm = kk.regdtm(idnum)
            self.assertIsInstance(rdtm, datetime)
        for idnum in str_kk:
            rdtm = kk.regdtm(idnum)
            self.assertIsInstance(rdtm, datetime)

    def test_kk_regday(self):
        for idnum in int_kk:
            rday = kk.regday(idnum)
            self.assertIsInstance(rday, str)
        for idnum in str_kk:
            rday = kk.regday(idnum)
            self.assertIsInstance(rday, str)

    def test_kk_nthpub(self):
        for idnum in int_kk:
            nth = kk.nth_pub(idnum)
            self.assertIsInstance(nth, int)
        for idnum in str_kk:
            nth = kk.nth_pub(idnum)
            self.assertIsInstance(nth, int)

    def test_kk_kkreader(self):
        for idnum in int_kk:
            kk_dict = kk.all_info(idnum)
            self.assertIsInstance(kk_dict, dict)
        for idnum in str_kk:
            kk_dict = kk.all_info(idnum)
            self.assertIsInstance(kk_dict, dict)

if __name__ == '__main__':
    unittest.main()