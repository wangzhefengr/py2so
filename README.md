# py2so

> 对 Python 源代码进行加密(将`.py`文件编译为`.so`文件)

* 系统环境: Ubuntu 18.04
* Python 环境：Python 3.7.5

### 1.安装依赖库

```shell
$ sudo apt install python3-dev gcc
$ pip install cython
```

### 2.写一个测试 demo

```shell
$ mkdir script
$ cd script
$ touch test.py
$ touch so_test.py
$ touch setup.py
```

测试文件夹目录：

* `py2so/script/test.py`
* `py2so/script/so_test.py`
* `py2so/script/setup.py`

测试文件脚本：

```python
# test.py

import datetime

class Today():
    def get_time(self):
        print(datetime.datetime.now())

    def say(self):
        print("Hello World!")
```

```python
# so_test.py

from test import Today

t = Today()
t.get_time()
t.say()
```

```python
# setup.py

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(["test.py"]))
```

编译前测试：

```shell
$ python3 so_test.py
```

编译前测试输出结果：

```
2020-04-10 11:10:41.940473
Hello World!
```


### 3.对 `test.py` 进行编译加密

```shell
$ python3 setup.py build_ext
```

生成文件:

* `py2so/script/build`
    - `py2so/script/build/lib.linux-x86_64-3.7`
        + `test.cython-37m-x86_64-linux-gnu.so`
    - `py2so/script/build/temp.linux-x86_64-3.7`
        + `test.o`
* `py2so/script/__pycache__`
* `py2so/script/test.c`
* `py2so/script/test.py`
* `py2so/script/setup.py`
* `py2so/script/so_test.py`


### 4.运行加密后的文件

编译后测试：

```shell
$ mv ./bulid/lib.lib.linux-x86_64-3.7/test.cython-37m-x86_64-linux-gnu.so .
$ rm -rf test.py
$ python3 so_test.py
```

编译后测试输出结果：

```
2020-04-10 11:10:43.940473
Hello World!
```