# -*- coding: utf-8 -*-
from model.group import Info, Tele

def test_add_new_contact(app):
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.contact.add_info(Info(name1="tester", name2="testerovich", name3="testovich", nickname="ptest", title="p", companyname="bro", adress="steret"))
        app.contact.add_telefon_number(Tele(telefon1="1111", telefon2="2222", telefon3="3333", fax="4444", box1="test@p.com", box2="test2@n.com", box3="test3@m.com", url="link"))
        app.contact.add_data()
        app.return_home_page()
        app.session.logout()



