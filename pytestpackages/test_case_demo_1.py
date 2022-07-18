import pytest


@pytest.fixture()
def s():
    print("Running once before every method")
    yield
    print("Running once after every method")


def test_methodA(s):
    print("running method A")


def test_methodB(s):
    print("running method B")
