# This is my file -Abhinay

from django.http import HttpResponse as Res
import os
def read(request):
    with open(os.getcwd()+'/myproject/sample.txt','r') as smp:
        line=smp.readline()
        s=""
        while line:
            s=s+line
            s=s+'\n'
            line=smp.readline()
    return  Res(s)

def newlineremove(request):
    return Res('New Line Remove')


def spaceremove(request):
    return Res('Space Remove')
def puncremove(request):
    return Res('Punctuation Remove')
def charcount(request):
    return Res('Character Count')
def capitalizefirst(request):
    return Res('Capitalize First')
def home(request):
    return Res('Home')


def about(request):
    return Res('Bhagwa Mera Mahan')