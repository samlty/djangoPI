from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
import subprocess
import os




def start(request):
    killExisted('raspivid')
    killExisted('vlc')
    startProcess()



    return HttpResponse(" start successful")


def stop(request):
    killExisted('raspivid')
    killExisted('vlc')

    return HttpResponse(" start successful")


def killExisted(processName):
    sub_process = os.popen('ps -ef|grep ' + processName)
    lines = sub_process.readlines()
    for line in lines:
        pid = line.split()[1]
        os.system('kill -9 ' + pid)

def startProcess():
    cmd = "raspivid -o - -t 0 -w 640 -h 360 -fps 25 | cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264 1>/dev/null 2>/dev/null &" 
    try:
        sub_process = os.popen(cmd)
    except Exception as e:
        print e
