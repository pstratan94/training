from model.group import Group

def test_edit_group(app):
    app.group.edit_group(Group(name="test1", header="tester1", footer="tester1"))
