# appium环境安装网址
入门案例  https://www.cnblogs.com/shuchengxiang/p/7145037.html
安装步骤  https://www.cnblogs.com/fnng/p/4552438.html
windows sdk 下载地址：https://dl.google.com/android/android-sdk_r24.4.1-windows.zip?utm_source=androiddevtools&utm_medium=website
platform-tools_r22-windows.zip  https://pan.baidu.com/s/1sj4ZfTb?utm_source=androiddevtools&utm_medium=websit

解决appium-dotor无效  https://www.cnblogs.com/yoyoketang/p/9123489.html





# macaca
###  切换到淘宝cnpm，npm装不了用cnpm
npm install -g cnpm --registry=https://registry.npm.taobao.org
npm i macaca-android -g
npm i app-inspector -g

解决不能build app https://testerhome.com/topics/10056?order_by=like&
error提示如下：
Warning: License for package Android SDK Build-Tools 25.0.2 not accepted.
Checking the license for package Android SDK Platform 26 in E:\ADT\sdk\licenses
Warning: License for package Android SDK Platform 26 not accepted.

android-sdk-windows\tools\bin>sdkmanager.bat --update 会出来两个许可提示 选y 回车 即可
(sdkmanager --licenses win10 cmd下 会提示不存在该参数 然后列出来许多可支持的参数 我看了下 选择了--update 后 就可以了.)最后一个 可能会卡一会 等一会儿 在ctrl+c 停止就可以了）
Android SDK Tools 必须在(25.2.3或者以上) 才会有sdkmanager.bat

*有问题重装必须 cd ~/AppData/Local/temp目录下删除npm开头所有文件再次卸载重装。*
rm npm* -rf

### doc
macaca doc https://macacajs.github.io/zh/python

wd doc  https://macacajs.github.io/wd.py/quickstart.html

#### macaca滑动
rect滑动参考 https://testerhome.com/topics/12255



#  Genymotion
http://www.genymotion.net/