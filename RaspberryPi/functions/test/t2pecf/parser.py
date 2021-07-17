def parse(path:str):
    try:
        fp = open(path)
    except:
        return None
    source:str = fp.read()
    fp.close()
    if source[0:8] != 't2pecf==':
        return None
    DATA:dict = {}
    for container in source[8:].split('.'):
        if container[0:7] == 'prof===':
            DATA['professors'] = container[7:]
        if container[0:7] == 'student':
            DATA['students'] = container[7:]
        if container[0:7] == 'lecture':
            DATA['lecture'] = container[7:]
        if container[0:7] == 'attend=':
            DATA['attend'] = container[7:]
    return DATA


print(parse('test.dat'))
