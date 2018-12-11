# Docker安装与build记录

## install



## usage
 	- docker search 
 	- docker pull
	- 推到阿里云仓库仓库上：
	   - docker login --username=[AliyunAccount] registry.cn-hangzhou.aliyuncs.com
	   - docker tag [imageID]  registry.cn-hangzhou.aliyuncs.com/[namespace]/[build_name]:[tag]
	   - docker push registry.cn-hangzhou.aliyuncs.com/[namespace]/[build_name]:[tag]

    - 删除所有容器
      -  docker rm $(docker ps -qa)
 
    - 删除所有镜像
      -  docker images -a|awk '{print $3 }'|xargs docker rmi -f
    - commit
      -  docker commit -m "add change timezone" p3rt_dev sayheya/p3rt_ubu:1.1



###### build之后cron不自动启动的暂时解决方案
    使用启动命令启动cron
    docker run -it --name p3rt_dev  d2a7141c5bb3 /bin/sh -c "/usr/sbin/cron;/bin/bash"

###### 更改ubuntu镜像时区
		1、共享主机的localtime  
		创建容器的时候指定启动参数，挂载localtime文件到容器内，保证两者所采用的时区是一致的。（:ro是只读的意义）
		docker run --name <name> -v /etc/localtime:/etc/localtime:ro ....
		2、复制主机的localtime  
		docker cp /etc/localtime containerid:/etc/localtime
		3、软连接
		ln -sf /usr/share/zoneinfo/Asia/Shanghai/etc/localtime
		echo "Asia/Shanghai" >/etc/timezone
