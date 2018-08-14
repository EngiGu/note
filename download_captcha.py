import requests,os
from contextlib import closing
from multiprocessing import Pool


captcha_url = 'http://wap.10010hb.net/weixin/validateCode.action?'
out_dir = './captcha/wxhubei'
ip_url = 'http://123.207.35.36:5010/get/'


def download(i):
    ret_ip = requests.get(ip_url)
    IP = ret_ip.content.decode()
    img_name = str(i) + '.png'
    proxies = { "http": "http://%s" % IP, "https": "https://%s" % IP}

    try:
        with closing(requests.get(captcha_url, stream=True, timeout=5)) as r:
            with open(os.path.join(out_dir, img_name), 'wb') as f:
                for data in r.iter_content(1024):
                    f.write(data)

        print('第 %s 张下载完成。。' % str(i))
    except:
        print('第 %s 张下载失败！！' % str(i))


if __name__ == '__main__':
    p = Pool(8)
    for i in range(1, 5000 + 1):
        p.apply_async(download, (i,))
    p.close()
    p.join()





