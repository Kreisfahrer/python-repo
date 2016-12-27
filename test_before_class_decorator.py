import pytest


class Test:
    @pytest.fixture()
    def before(self):
        print('\nbefore each test')

    @pytest.mark.usefixtures("before")
    def test_1(self):
        print('test_1()')

    @pytest.mark.usefixtures("before")
    def test_2(self):
        print('test_2()')
