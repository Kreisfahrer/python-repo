import pytest


def f():
    raise SystemExit(1)

def test_exception():
    with pytest.raises(SystemExit):
        f()
