
from setuptools import setup, find_packages

setup( name = "SusoCrawler12",
       version = "0.2",
       packages = find_packages(),
       scripts = ['SusoCrawler12'],
       install_requires = ['BeautifulSoup'],
       package_data = { 'pysusocrawler': [''], },
       author = "Jesus Urcera",
       author_email = "jurcera@gmail.com",
       description = "SusoCrawler2012 crawler MSWL",
       license = "GPLv3",
       keywords = "crawler web",
       url = "https://github.com/jurcera/SusoCrawler",
       long_description = "Web crawler for DevTools subject in MSWL",
       download_url = "https://github.com/jurcera/SusoCrawler", )
