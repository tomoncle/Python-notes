# Python Study
> 控制台打印乱码： **` print '你好，世界！'.decode('utf-8') `**

```python
url = 'http://{0}:{1}/{2}'.format('0.0.0.0', 2375, 'xxx')
url = 'http://{ip}:{port}/{uri}'.format(ip='0.0.0.0', port=2375, uri='xxx')
url = 'http://%s:%d/%s' % ('0.0.0.0', 2375, 'xxx')
```

## Windows Python 依赖库[ **PythonLibs**](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
* 1.找到对应的 `whl` 包下载
* 2.直接`pip install *.whl` 或者修改`.whl`文件为`.zip`文件，解压缩文件的`Python文件夹`复制到--`python`安装目录下的`Lib`--目录下

## [Python 中文翻译文档集合](http://python.usyiyi.cn/)
## [Python 官方文档](https://docs.python.org/2.7/)
## [Top Python APIs](https://www.programcreek.com/python/index/module/list)

## Python2.7环境变量
> 假如`sys.path`不对,则使用Python终端 ` sys.path = [...] `重新设置即可.
> 默认环境配置如下：

```shell
root@node-40:~# python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys 
>>> sys.path
['', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/PILcompat', '/usr/lib/python2.7/dist-packages/gtk-2.0', '/usr/lib/pymodules/python2.7']
>>> 
```
```shell
# /etc/profile

export PYTHONPATH=/usr/lib/python2.7:/usr/lib/python2.7/plat-x86_64-linux-gnu:/usr/lib/python2.7/lib-tk:/usr/lib/python2.7/lib-old:/usr/lib/python2.7/lib-dynload:/usr/local/lib/python2.7/dist-packages:/usr/lib/python2.7/dist-packages:/usr/lib/python2.7/dist-packages/PILcompat:/usr/lib/python2.7/dist-packages/gtk-2.0:/usr/lib/pymodules/python2.7
export PATH=$PATH:$PYTHONPATH
```

## `Python2.7`与`Python3.x` 共同使用

* Python2.7 : `$ py -2`
* Python3.x : `$ py -3`
* Python2.7 pip : `$ py -2 -m pip xxx`
* Python3.x pip : `$ pip3 xxx`

## pycharm
> settings

* enable Code compatibility inspection: `settings` --> `code compatibility inspection`

## Python内置工具

* 下载服务器：
  * Python2.x
     * `$ python -m SimpleHttpServer` 默认端口8000
     * `$ py -2 -m SimpleHTTPServer` 默认端口8000
     * `$ py -2 -m SimpleHTTPServer 9090` 指定端口9090
     * 使用代码：
     ```python
     import SimpleHTTPServer

     SimpleHTTPServer.test()
     ```
  * Python3.x
     * `$ python -m http.server`
     * `$ py -3 -m http.server`

* Json格式化：`$ curl http://localhost:8080/get | python -m json.tool`

* 执行Python代码：`$ python -c "print 'hello world!'"`

* 解压zip包：
  * 创建zip包：`$ python -m zipfile -c tom.zip tom.txt`
  * 解压zip包：`$ python -m zipfile -e tom.zip .`
  * 查看zip包：`$ python -m zipfile -l tom.zip`


* 文件处理：
  ```python
  import shutil

  shutil.copy('C:\Users\Administrator\Desktop\ctools2.rar','q.rar')
  ```


## 关于Python工作中的一些总结性技术

* [爬虫](https://github.com/tomoncle/PythonStudy/tree/master/crawlers/)
* [RPC](https://github.com/tomoncle/PythonStudy/tree/master/rpc/)
* [定时任务](https://github.com/tomoncle/PythonStudy/tree/master/scheduler_task/study_apscheduler/)
* [mysql](https://github.com/tomoncle/PythonStudy/tree/master/contributed_modules/mysql/)
* [mongodb](https://github.com/tomoncle/PythonStudy/tree/master/contributed_modules/mongodb/)
* [redis](https://github.com/tomoncle/PythonStudy/tree/master/contributed_modules/redis/)
* [数据分析](https://github.com/tomoncle/PythonStudy/tree/master/data_analysis/)：`maptplotlib`, `malb` , `numpy`, `tesseract`
* [页面解析技术](https://github.com/tomoncle/PythonStudy/tree/master/page_parser/): `bs4`, `xpath`
* [openstack开源模块](https://github.com/tomoncle/PythonStudy/tree/master/OpenStack/oslo_/)
* [Python 装饰器](https://github.com/tomoncle/PythonStudy/tree/master/decorator.md)
* [Python 多线程/多进程](https://github.com/tomoncle/PythonStudy//tree/masterstandard_library/threads/)
* [Python 内置模块](https://github.com/tomoncle/PythonStudy/tree/master/standard_library/)
* [Python 使用技巧](https://github.com/tomoncle/PythonStudy/tree/master/skills)

