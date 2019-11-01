import pytest

@pytest.mark.skip("Do not run this test")
def test_fail():
    assert True

@pytest.fixture(params=["mysql", "postgresql"])
def database(request):
    list_one = []
    list_one.append(request.param)
    yield list_one
    list_one=[]

def test_insert(database):
    database.append(123)
    print(database)
    assert ('mysql' in database or 'postgresql' in database)








