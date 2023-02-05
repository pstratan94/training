from model.group import Group
import pytest
from fixture.application import Application

@pytest.fixture (scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
