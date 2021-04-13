import urllib.request

# first page of MIT course catalog
url = 'http://student.mit.edu/catalog/m1a.html'

# Download the file from `url` and save it locally under `file_name`:
urllib.request.urlretrieve(url, 'm1a.html')

print('Ran to end!')
