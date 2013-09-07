import urllib2
import urllib
import os, shutil
import glob
from BeautifulSoup import BeautifulSoup as bs
from urllib2 import urlopen

def get_html(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html

def get_url_base(url):
    # turns
    # http://apod.nasa.gov/apod/astropix.html
    # into
    # http://apod.nasa.gov/apod/
    ri = url.rfind('/')
    return url[0:ri+1]

def get_url_filename(url):
    ri = url.rfind('/')
    return url[ri+1:]

def get_img_links(url):
    #html = get_html(url)
    soup = bs(urlopen(url))

    url_base = get_url_base(url)

    img_links = []

    for image in soup.findAll("img"):
        #print "Image: %(src)s" % image
        #print image["src"]
        src = image["src"].strip()
        if not src:
            continue
        elif src.lower().startswith("http"):
            link = src
        else:
            link = url_base + src
        img_links.append(link)
    return img_links

def dl_image(url, out='temp/'):
    if not os.path.isdir(out):
        os.mkdir(out)
    # get the filename
    urllib.urlretrieve( url, out + get_url_filename(url))

def rmdir(path):
    files = glob.glob(path + '*')
    for f in files:
        os.remove(f)
    os.rmdir(path)


# download all images to a temp folder
def dump_images(url, out='temp/'):
    for link in get_img_links(url):
        dl_image(link, out)

def get_main_img(url, out='wallpapers/'):
    
    temp = 'temp/'
    if os.path.exists(temp):
        shutil.rmtree(temp)

    dump_images(url, temp)

    #find the largest file in the group
    files = glob.glob(temp + '*')
    biggest_file = files[0]
    for f in files:
        if os.path.getsize(f) > os.path.getsize(biggest_file):
            biggest_file = f

    shutil.move(biggest_file, 'current_image')
    rmdir(temp)


url = 'http://apod.nasa.gov/apod/astropix.html'
#url = 'http://web.stagram.com/photooftheday/'
url = 'http://www.earthshots.org/'
url = 'http://epod.usra.edu/'
#url = 'http://photography.nationalgeographic.com/photography/photo-of-the-day/'
#link = 'http://apod.nasa.gov/apod/image/1309/sgra_gasChandra_900c.jpg'

#get_main_img(url)
