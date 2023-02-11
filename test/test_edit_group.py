from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="test1", header="tester1", footer="tester1"))
    app.session.logout()
