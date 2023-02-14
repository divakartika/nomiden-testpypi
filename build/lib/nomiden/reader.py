from nomiden import nik
from nomiden import kk

class NIK:
    def __init__(self, idnum):
        self.province = nik.province(idnum)
        self.city = nik.city(idnum)
        self.district = nik.district(idnum)
        self.gender = nik.gender(idnum)
        self.birthdate = nik.birthdate(idnum)
        self.birthmonth = nik.birthmonth(idnum)
        self.birthyear = nik.birthyear(idnum)
        self.birthdtm = nik.birthdtm(idnum)
        self.birthday = nik.birthday(idnum)
        self.age = nik.age(idnum)
        self.nth_person = nik.nth_person(idnum)
        self.all_info = nik.all_info(idnum)

class KK:
    def __init__(self, idnum):
        self.province = kk.province(idnum)
        self.city = kk.city(idnum)
        self.district = kk.district(idnum)
        self.regdate = kk.regdate(idnum)
        self.regmonth = kk.regmonth(idnum)
        self.regyear = kk.regyear(idnum)
        self.regdtm = kk.regdtm(idnum)
        self.regday = kk.regday(idnum)
        self.nth_pub = kk.nth_pub(idnum)
        self.all_info = kk.all_info(idnum)