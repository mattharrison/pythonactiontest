def add(x, y):
    return x + y
    
def num_parse(txt):
    res = []
    for item in txt.split(','):
        res.append(int(item))
    return res
