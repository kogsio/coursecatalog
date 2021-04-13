import urllib.request;

urls = [];
urls.append('http://student.mit.edu/catalog/m1a.html');
urls.append('http://student.mit.edu/catalog/m1b.html');
urls.append('http://student.mit.edu/catalog/m1c.html');
urls.append('http://student.mit.edu/catalog/m2a.html');
urls.append('http://student.mit.edu/catalog/m2b.html');
urls.append('http://student.mit.edu/catalog/m2c.html');
urls.append('http://student.mit.edu/catalog/m3a.html');
urls.append('http://student.mit.edu/catalog/m3b.html');
urls.append('http://student.mit.edu/catalog/m4a.html');
urls.append('http://student.mit.edu/catalog/m4b.html');
urls.append('http://student.mit.edu/catalog/m4c.html');
urls.append('http://student.mit.edu/catalog/m4d.html');
urls.append('http://student.mit.edu/catalog/m4e.html');
urls.append('http://student.mit.edu/catalog/m4f.html');
urls.append('http://student.mit.edu/catalog/m4g.html');
urls.append('http://student.mit.edu/catalog/m5a.html');
urls.append('http://student.mit.edu/catalog/m5b.html');
urls.append('http://student.mit.edu/catalog/m6a.html');
urls.append('http://student.mit.edu/catalog/m6b.html');
urls.append('http://student.mit.edu/catalog/m6c.html');
urls.append('http://student.mit.edu/catalog/m7a.html');
urls.append('http://student.mit.edu/catalog/m8a.html');
urls.append('http://student.mit.edu/catalog/m8b.html');
urls.append('http://student.mit.edu/catalog/m9a.html');
urls.append('http://student.mit.edu/catalog/m9b.html');
urls.append('http://student.mit.edu/catalog/m10a.html');
urls.append('http://student.mit.edu/catalog/m10b.html');
urls.append('http://student.mit.edu/catalog/m11a.html');
urls.append('http://student.mit.edu/catalog/m11b.html');
urls.append('http://student.mit.edu/catalog/m11c.html');
urls.append('http://student.mit.edu/catalog/m12a.html');
urls.append('http://student.mit.edu/catalog/m12b.html');
urls.append('http://student.mit.edu/catalog/m12c.html');
urls.append('http://student.mit.edu/catalog/m14a.html');
urls.append('http://student.mit.edu/catalog/m14b.html');
urls.append('http://student.mit.edu/catalog/m15a.html');
urls.append('http://student.mit.edu/catalog/m15b.html');
urls.append('http://student.mit.edu/catalog/m15c.html');
urls.append('http://student.mit.edu/catalog/m16a.html');
urls.append('http://student.mit.edu/catalog/m16b.html');
urls.append('http://student.mit.edu/catalog/m17a.html');
urls.append('http://student.mit.edu/catalog/m17b.html');
urls.append('http://student.mit.edu/catalog/m18a.html');
urls.append('http://student.mit.edu/catalog/m18b.html');
urls.append('http://student.mit.edu/catalog/m20a.html');
urls.append('http://student.mit.edu/catalog/m21a.html');
urls.append('http://student.mit.edu/catalog/m22a.html');
urls.append('http://student.mit.edu/catalog/m22b.html');
urls.append('http://student.mit.edu/catalog/m22c.html');
urls.append('http://student.mit.edu/catalog/m24a.html');
urls.append('http://student.mit.edu/catalog/m24b.html');

for counter, url in enumerate(urls):
    try:
        urllib.request.urlretrieve(url, f'data/{counter}.html')
    except:
        print('Error: ' + url)

print('Ran to end!')

