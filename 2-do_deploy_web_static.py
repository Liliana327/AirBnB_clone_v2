#!/usr/bin/python3
'''Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers
using the function do_deploy: '''

from fabric.api import put, run, env
import os.path
env.hosts = ['35.196.101.171', '35.237.255.234	']


def do_deploy(archive_path):
    '''Deploy archive'''
    if os.path.isfile(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1]
        not_ext = filename.split(".")[0]
        not_path = "/data/web_static/releases/{}/".format(not_ext)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(not_path))
        run("tar -xzf /tmp/{} -C {}".format(filename, not_path))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(not_path, not_path))
        run("rm -rf {}web_static".format(not_path))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(not_path, symlink))
        if result.failed:
            return False
        return True
    except:
        return False
