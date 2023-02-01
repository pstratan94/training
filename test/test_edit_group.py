

def test_edit_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.edit_group()
    app.session.logout()
