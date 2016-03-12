import urllib.request, random, web_string

k = input('请输入需要刷新的次数：\n')
k = int(k)

for i in range (k):
    #产生一个 web 地址
    w_fir = web_string.dir(random.choice(web_string.web_root))
    w_sec = web_string.dir(random.choice(web_string.web_category))
    w_last = web_string.random_str(8)
    w = w_fir + w_sec +w_last
    #print('正在开始第' + chr(i) + '次刷新,当前进度为' + chr(i/k*100) + '\n' +'您所使用的Header为：' + w)
    #print('您所使用的Header为：' + w)
    #需要刷访问的 url
    url = 'http://hhhguany.blog.163.com'

    #创建一个 opener 模拟浏览器访问
    opener = urllib.request.build_opener()
    opener.addheaders = [
     #   ('Host', 'nsclick.baidu.com'),
     #   ('Accept-Encoding', 'gzip, deflate'),
     #   ('Cookie', 'BAIDUID=D4837791B287B35863AE816E46A070DF:FG=1; BDRCVFR[5Bri_i5nG73]=mk3SLVN4HKm; BDUSS=dFWmpRZDBvNm5JfnJmQlQ3UXA2ZGxVOEtjZXVhbDU4SEJHTnNMTlBCMXhxc0pXQVFBQUFBJCQAAAAAAAAAAAEAAADGtzgEaGhoZ3VhbnkAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
        ('Connection', 'keep-alive'),
        ('Accept', '*/*'),
        ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/537.86.4'),
        ('Accept-Language', 'zh-cn'),
        ('Referer', w),
        ('Cache-Control', 'max-age=0')
        ]

    html = opener.open(url).read()#.decode('utf-8')
    print ('ok')
