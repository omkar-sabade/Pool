import re
import os
import argparse
from subprocess import call
from bs4 import BeautifulSoup
from urllib.parse import unquote
from urllib.request import urlretrieve as ur,build_opener,urlopen

def urlretrieve(url,filename):
    try:	
    	ur(url,filename)
    except Exception as e:
    	print(e)
    print("Done : " + filename)

def ifprint(messgae,not_end='\n'):
	if args.verbose:
		print(messgae,end = not_end)

parser = argparse.ArgumentParser()
parser.add_argument("url",help = "URL to the subdir")
parser.add_argument("-p","--path",help="Destination folder",default = '.')
parser.add_argument("-l","--limit",help="Max number of files to download",type = int,default = 10000)
parser.add_argument("-z","--zip",action = "store_true",help="Save the output as a zipped file")
parser.add_argument("-v","--verbose",action = "store_true",help = "To be or not to be")
parser.add_argument("ext",action = 'append',help = "file extensions to download")
args = parser.parse_args()

if args.path:
	path = args.path if args.path.endswith('/') else args.path + '/'

args.ext = '|'.join(['\.' + i + '$' for i in args.ext])
regex = ".*(" + args.ext + ")"

ifprint("Looking up " + args.url)

opener = build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

ifprint("Fetching page...",not_end = '')
html = opener.open(args.url)
ifprint("Done.")
bObject = BeautifulSoup(html,features='html5lib')

files = bObject.find_all("a",{'href':re.compile(regex)})
files = list(set(['https://github.com' + file['href'] for file in files]))
ifprint("Found {} urls.".format(len(files)))

if len(files) == 0:
	print("Exitting.")
	exit()

dir_name = path + str(unquote(args.url.split('/')[-1]))
ifprint("Saving to dir : " + dir_name)

call(['rm','-rf',dir_name])
os.makedirs(dir_name)

for file in files[:args.limit]:
    urlretrieve(file.replace('blob','raw'),dir_name + '/' + file.split('/')[-1])

if args.zip:
	ifprint("Zipping files")
	call(['zip',"-r",dir_name + ".zip",dir_name])
