from requests import get
from os import system,popen
import sys
import argparse
def getnlines(filename):
    n=int(popen("cat {} | wc -l".format(filename)).read()[:-1])
    return n

def tryone(url,word,s,f):
    r=get(url.format(word))
    if(s in r.text or not(f in r.text)):
        return True
    else:
        return False

parser = argparse.ArgumentParser()
parser.add_argument('-u',type=str,help='url with {} signe',required=True)
parser.add_argument('-w',type=str,help='wordlist',required=True)
parser.add_argument('-v',type=bool,help='verbous True or False',default=False)
parser.add_argument('-s',type=str,help='index of seccess',default='successful')
parser.add_argument('-f',type=str,help='index of failure',default='failed')
args=parser.parse_args()


try:
    nlines=getnlines(args.w)
except:
    print('not a valid wordlist')
    exit()
success=[]
file=open(args.w,'r')
for i in range(0,nlines):
    word=file.readline()[:-1]
    if(tryone(args.u,word,args.s,args.f)):
        if(args.v):
            print('[+] {} is successful'.format(word))
        success.append(word)
file.close()
if(not args.v):
    for i in success:
        print(i)

print('end ?')        