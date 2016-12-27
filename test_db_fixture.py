import pytest


@pytest.fixture(scope='module')
def cheese_db():
    print('\n[setup] cheese_db, connect to db')
    a_dictionary_for_now = {'Brie': 'No.', 'Camenbert': 'Ah! We have Camenbert, yessir.'}
    yield a_dictionary_for_now
    print('\n[teardown] cheese_db finalsizer, disconnect from db')

def test_cheese_database(cheese_db):
    print('in test_cheese_database()')
    for variety in cheese_db.keys():
        print('%s : %s' % (variety, cheese_db[variety]))


def test_brie(cheese_db):
    print('in test_brie()')
    assert cheese_db['Brie'] == 'No.'


def test_camenbert(cheese_db):
    print('in test_camenbert()')
    assert cheese_db['Camenbert'] != 'No.'
