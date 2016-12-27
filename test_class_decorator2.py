import pytest


@pytest.mark.usefixtures("before")
class Test:

    @pytest.fixture
    def before(self):
        print('\nbefore each test')

    def test_1(self):
        print('test_1()')

    def test_2(self):
        print('test_2()')
