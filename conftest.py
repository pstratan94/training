from model.group import Group
import pytest
from fixture.application import Application
from fixture.application import Webnote

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

# @pytest.fixture
# def app(request):
#     fixture = Webnote()
#     request.addfinalizer(fixture.destroy)
#     return fixture
