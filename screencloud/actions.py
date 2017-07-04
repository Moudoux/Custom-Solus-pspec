#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf screencloud_%s.*_amd64.deb" % Version)
    shelltools.system("tar xf data.tar.gz")

def install():
    pisitools.insinto("/", "usr")
    pisitools.dosym("/usr/share/screencloud/screencloud.desktop", "/usr/share/applications/screencloud.desktop")
