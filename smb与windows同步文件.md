```shell
#### 虚拟机与vm同步文件

sudo apt-get install samba -y

mkdir work 
sudo chmod +777 . -R


#### 添加一个用户, 密码
sudo smbpasswd -a tk

#### 
sudo cp /etc/samba/smb.conf  /etc/samba/smb.conf.bak
sudo vim /etc/samba/smb.conf

#### 末尾追加

[workspace]
comment = workspace folder
browseable = yes
path = /home/tk/workspace
create mask = 0700
directory mask = 0700
valid users = tk
force user = tk
force group = tk
public = yes
available = yes
writable = yes

#### 重启
sudo service smbd restart

#### windows 访问
\\192.168.xx.xx

#### 右键文件夹，点击右键，选择映射网络驱动器

```
