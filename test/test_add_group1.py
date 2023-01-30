# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group1(app):
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.open_groups_page()
        app.create_group(Group(name="test", header="tester", footer="tester"))
        app.return_to_groups_page()
        app.session.logout()

def test_add_empty_group1(app):
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.open_groups_page()
        app.create_group(Group(name="", header="", footer=""))
        app.return_to_groups_page()
        app.session.logout()


