•安装python3.6可能使用的依赖

yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel
 

•到python官网找到下载路径, 用wget下载

wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz

•解压tgz包

tar -zxvf Python-3.6.4.tgz

•把python移到/usr/local下面

mv Python-3.6.4 /usr/local

•进入python目录

cd /usr/local/Python-3.6.4/

•配置

./configure

•编译 make

make

•编译，安装

make install

•删除旧的软链接，创建新的软链接到最新的python

 - ln -s /usr/local/bin/python3.6 /usr/bin/python3
 - ln -s /usr/local/bin/pip3 /usr/bin/pip3

至此，python3就装好了，python3，pip3呼出对应功能。

---------------（以下不是必要步骤）

•安装虚拟环境

pip3 install  virtualenv  virtualenvwrapper

vim ~/.bashrc

在文末填入以下代码并保存

VIRTUALENVWRAPPER_PYTHON=/usr/local/python3/bin/python3    # 指定virtualenvwrapper执行的python版本
export WORKON_HOME=$HOME/.virtualenvs    # 指定虚拟环境存放目录，.virtualenvs目录名可自拟
source /usr/local/bin/virtualenvwrapper.sh    # virtualenvwrapper.sh所在目录

•运行.bashrc文件

source ~/.bashrc

•创建虚拟环境

# mkvirtualenv sp
也可指定虚拟环境的python版本

# mkvirtualenv --python=/usr/bin/python3 sp  (也可以不指定) 
•进入虚拟环境中，然后进入到项目所在目录，安装好相应的包（如无需要，可跳过此步）

•pip install -r requirements.txt