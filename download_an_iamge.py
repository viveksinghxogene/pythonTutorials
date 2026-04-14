import urllib.request

url="https://tse3.mm.bing.net/th/id/OIP.9XKI54bo_4Duu9QQA6ZgAAHaEK?rs=1&pid=ImgDetMain&o=7&rm=3"
img_file=urllib.request.urlretrieve(url,"new_img.png")