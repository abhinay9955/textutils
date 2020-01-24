# This is my file -Abhinay

from django.http import HttpResponse as Res
import os
def home(request):
    with open(os.getcwd()+'/myproject/sample.txt','r') as smp:
        line=smp.readline()
        s=""
        while line:
            s=s+line
            s=s+'\n'
            line=smp.readline()
    return  Res(s)


def about(request):
    return Res('Bhagwa Mera Mahan')