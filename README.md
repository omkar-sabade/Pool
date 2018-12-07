# Pool
Python script to download files from subdirectories on github

I'd been looking for ways to download sub-directories on github for which there are workarounds using SVN or you can just use GITzip.
The way that this script does that is painfully slow and is not the optimal way. It merely represents an idea and my afternoon curiosity.

PS:If you're using windows you may have to change a couple lines (56 and 64 as of now)
## Usage
1. Navigate to the sub directory on github copy the url of that page.
2. run python3 subdir.py <url> <extension>
  
**Help**
```
python3 subdir.py --help
```
usage: subdir.py [-h] [-p PATH] [-l LIMIT] [-z] [-v] url ext

positional arguments:
  url                   URL to the subdir
  ext                   file extensions to download

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Destination folder
  -l LIMIT, --limit LIMIT
                        Max number of files to download
  -z, --zip             Save the output as a zipped file
  -v, --verbose         To be or not to be
