from model.contact import Contact

def test_edit_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(Contact(firstname="tester1", middlename="testerovich1", lastname="testovich1", nickname="ptest1", title="p1", companyname="bro1", adress="steret1" , home_tel="11111", mobile_tel="22221", work_tel="33331", fax="44441", box1="test1@p.com", box2="test21@n.com", box3="test31@m.com", url="link1"))
    app.session.logout()
