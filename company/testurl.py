
import urllib2, urlparse

def testurl(url, timeout=0.3):
    response = None
    try:
        p = urlparse.urlparse(url)
        if p.netloc:
            response = urllib2.urlopen(url, timeout=timeout)
        else:
            return True
    except urllib2.URLError, err:
        pass
    if response:
        return response.getcode()==200
    else:
        return False
