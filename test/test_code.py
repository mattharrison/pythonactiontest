import pyaction

import pytest

def skipit(name):
    return pytest.mark.skipif(name not in dir(pyaction),               reason='missing')

@skipit('parse')
def test_parse():
    txt = '1,2,10'
    res = pyaction.parse(txt)
    assert res == [1,2,10]


@skipit('sub')
def test_sub():
    res = pyaction.sub(1,2)
    assert res == -1
