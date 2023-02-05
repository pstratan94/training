class Group:
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer

class Info:

    def __init__(self, firstname, middlename, lastname, nickname, title, companyname, adress):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.companyname = companyname
        self.adress = adress

class Tele:

    def __init__(self, telefon1, telefon2, telefon3, fax, box1, box2, box3, url):
        self.telefon1 = telefon1
        self.telefon2 = telefon2
        self.telefon3 = telefon3
        self.fax = fax
        self.box1 = box1
        self.box2 = box2
        self.box3 = box3
        self.url = url


