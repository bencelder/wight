import urllib2
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


url = 'http://apod.nasa.gov/apod/astropix.html'
#url = 'http://photography.nationalgeographic.com/photography/photo-of-the-day/'
for link in get_img_links(url):
    print link


#bits = url.split('/')
#bits = bits[0:-1]
#print bits
