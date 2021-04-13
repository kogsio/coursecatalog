# Course Catalog
Scrape the MIT course catalog with using python.

## Quickstart
You can start by running  [quickstart.py](quickstart.py) and downloading a single catalog page.
```python
import urllib.request

# first page of MIT course catalog
url = 'http://student.mit.edu/catalog/m1a.html'

# Download the file from `url` and save it locally under `file_name`:
urllib.request.urlretrieve(url, 'm1a.html')
```

## All Catalog Pages
You can down all the pages of the catalog with file named [courseCatalog.py](courseCatalog.py).

## Merge pages
Marge the catalog pages with [merge.py](merge.py).

## Sensemaking
Before running [sensemaking.py](sensemaking.py), you need to download all the catalog pages and merge them into one file. You can do that by running [courseCatalog.py](courseCatalog.py) first and then [merge.py](merge.py).

Note: the merged file has over 45,000 lines of html. Parsing will be slow.