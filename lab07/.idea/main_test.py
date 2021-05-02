import main
import pytest
@pytest.mark.parametrize('a,b,result',
                         [
                             (2,3,5),
                             ('ale',' bryka', 'ale bryka'),
                             (12.23,45.44,57.67),
                             ("at","ak","atak")
                         ]
                         )
def test_add(a,b,result):
    assert main.add(a,b) == result