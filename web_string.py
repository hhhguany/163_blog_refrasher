import random

web_root = [
    'www.baidu.com',
    'www.google.com',
    'www.qq.com',
    'www.163.com',
    'www.udidi.org'
]

web_category = [
    'sport', 'story', 'news', 'flower', 'women', 'boy', 'girl', 'pp', 'dick', 'mama', 'papa'
]


def dir(url):
    return(url + '/')

def random_str(i):
    ws = ''
    for k in range(i):
        w = random.sample('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789', 1)
        w = random.choice(w)
        ws = ws + w
    return ws
