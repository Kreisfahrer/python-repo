import pytest

@pytest.fixture()
def before():
	print('before was called')

@pytest.mark.usefixtures('before')
def test_one():
	print('test one called')

@pytest.mark.usefixtures('before')
def test_two():
	print('test two called')