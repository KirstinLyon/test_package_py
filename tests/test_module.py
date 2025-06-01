from test_package_py.message import hello, goodbye

def test_hello():
    assert hello() == "Hello"


def test_goodbye():
    assert goodbye() == "Goodbye"