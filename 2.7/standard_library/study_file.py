#  -*- coding=utf-8 -*-

"""
文件操作
"""

import errno
import os

import six


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print u'文件夹%s　已经存在' % path


def parent_dir(path):
    if path[-1] == '/': path = path[0:-1]
    return '/'.join(path.split('/')[0:-1])


def del_dir(path):
    if not all((os.path.exists(path), os.path.isdir(path))):
        return
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(path)


def create_file(name, mode='r', data=""):
    try:
        parent_path = parent_dir(name)
        if parent_path and not os.path.exists(parent_path):
            create_dir(parent_path)
        with open(name, mode)as f:
            f.write(data)
    except Exception, e:
        print u'%s 创建失败\n异常：%s' % (name, e)


def remove_file(file_path):
    try:
        os.remove(file_path)
    except OSError:
        pass


def get_file_size(file_obj):

    if (hasattr(file_obj, 'seek') and hasattr(file_obj, 'tell') and
            (six.PY2 or six.PY3 and file_obj.seekable())):
        try:
            curr = file_obj.tell()
            file_obj.seek(0, os.SEEK_END)
            size = file_obj.tell()
            file_obj.seek(curr)
            return size
        except IOError as e:
            if e.errno == errno.ESPIPE:
                return
            else:
                raise


if __name__ == '__main__':
    # create_file('/home/aric/pythontest/bb/bbb/abc.txt', 'w', 'hello world')

    del_dir('/home/liyuanjun/keys')
