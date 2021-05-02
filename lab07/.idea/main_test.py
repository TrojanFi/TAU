import main

def test_add():
    assert main.add(2,3) == 5

def test_add_strings():
    result = main.add('ale',' bryka')
    assert result == 'ale bryka'

def test_add_float():
    result = main.add(12.23,45.44)
    assert result == 57.67