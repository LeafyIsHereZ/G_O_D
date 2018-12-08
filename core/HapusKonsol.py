import subprocess as sp
import sys

def Cek_OS_KONSOL():
    a=sys.platform
    if a=="win32" or a=="win62":
        sp.call('cls',shell=True)
    else:
        sp.call('clear',shell=True)
