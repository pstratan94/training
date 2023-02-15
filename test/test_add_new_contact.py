# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_contact(app):
        app.contact.add_new_contact(Contact(firstname="tester", middlename="testerovich", lastname="testovich", nickname="ptest", title="p", companyname="bro", adress="steret", telefon1="1111", telefon2="2222", telefon3="3333", fax="4444", box1="test@p.com", box2="test2@n.com", box3="test3@m.com", url="link"))

