import pytest

@pytest.fixture
def before():
    print('\nbefore each test')
 
def test_1(before):
    print('test_123()')
 
def test_2(before):
    print('test_2()')
