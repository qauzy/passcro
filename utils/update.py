







import os,time,requests,base64


hdrs = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'}




def pjzy():

    url = 'https://raw.githubusercontent.com/pojiezhiyuanjun/freev2/master/'+time.strftime('%m%d')+'clash.yml'
    try:
        rsp = requests.get(url,headers = hdrs)
        yamltent = rsp.text.replace('(油管:破解资源君2.0)','')
        dirs = './subs'
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        if rsp.status_code == 200:
            with open(dirs + '/' + 'pjzy.yaml', 'w', encoding='utf-8') as f:
                f.write(yamltent)
    except Exception:
        pass
    
def miao():
    url = 'https://raw.githubusercontent.com/Strongmiao168/Clash/main/'+time.strftime('%m%d')+'clash.yml'
    try:
        rsp = requests.get(url,headers = hdrs)
        yamltent = rsp.text.replace('(油管:破解资源君2.0)','')
        dirs = './subs'
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        if rsp.status_code == 200:
            with open(dirs + '/' + 'miao.yaml', 'w', encoding='utf-8') as f:
                f.write(yamltent)
    except Exception:
        pass


if __name__ == '__main__':

    pjzy()
    miao()

