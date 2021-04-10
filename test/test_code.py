import code

def test_parse():
    txt = '1,2,10'
    res = code.parse(txt)
    assert res == [1,2,10]
