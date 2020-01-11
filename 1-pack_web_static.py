#!/usr/bin/python3
'''script that generates a tgz archive from the contents of the web_static
'''
from datetime import datetime
from fabric.api import local


def do_pack():
    '''generates a .tgz archive from the contents of the web_static folder'''
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(time)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except:
        return None
