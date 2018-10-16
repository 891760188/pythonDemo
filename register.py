# -*- coding: UTF-8 -*-

#   
# script to register Python 2.0 or later for use with win32all   
# and other extensions that require Python registry settings   
#   
# written by Joakim Loew for Secret Labs AB / PythonWare   
#   
# source:   
# http://www.pythonware.com/products/works/articles/regpy20.htm   
#   
# modified by Valentine Gogichashvili as described in http://www.mail-archive.com/distutils-sig@python.org/msg10512.html   
import sys
from _winreg import *
# tweak as necessary   
version = sys.version[:3]
installpath = sys.prefix
regpath = "SOFTWARE\\Python\\Pythoncore\\%s\\" % (version)
installkey = "InstallPath"
pythonkey = "PythonPath"
pythonpath = "%s;%s\\Lib\\;%s\\DLLs\\" % (
    installpath, installpath, installpath
)
reg = ''
def RegisterPy():
    try:
        reg = OpenKey(HKEY_CURRENT_USER, regpath)
    except EnvironmentError as e:
        try:
            reg = CreateKey(HKEY_CURRENT_USER, regpath)
            SetValue(reg, installkey, REG_SZ, installpath)
            SetValue(reg, pythonkey, REG_SZ, pythonpath)
            CloseKey(reg)
        except:
            print "*** Unable to register!"

        else:  print "*** Unable to register!" ;

if __name__ == "__main__":
    RegisterPy()