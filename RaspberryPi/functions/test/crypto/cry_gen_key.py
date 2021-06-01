import string, random

def genKey():
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(50)])

if __name__ == '__main__':
    print(genKey())