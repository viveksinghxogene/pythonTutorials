import urllib.request

try:
    url=urllib.request.urlopen('https://www.python.org/')
    content=url.read()
except urllib.error.URLError:
    print('Error in opening the URL of the website.')
    exit()

write_file=open('sample.txt','w')
write_file.write(str(content))
write_file.close()
