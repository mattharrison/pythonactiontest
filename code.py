def add(x, y):
    return x + y
    
def parse(txt):
    res = []
    for item in txt.split(','):
        res.append(int(item))
    return res
