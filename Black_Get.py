import requests

def star( ):
    res_black = requests.get("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/gfwlist-banAD.acl")
#分行
    lines = res_black.text.split("\r\n")
    list_black = []
    file = open("BLACK.txt", 'w')
    for line in lines:
#筛选
        if line.startswith("#") or len(line)<2 or line.startswith("["):
            continue
        list_black.append(line)
#保存到文件
        file.write(line+"\n")
    file.close()
    print("****************Blacklist online update completed****************")

