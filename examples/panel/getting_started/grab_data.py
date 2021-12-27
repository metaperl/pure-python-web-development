# https://svaderia.github.io/articles/downloading-and-unzipping-a-zipfile/

from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
zipurl = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00357/occupancy_data.zip'
with urlopen(zipurl) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extractall('.')
