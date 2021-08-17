import os
from pyzotero import zotero as zt


# setting
filepath_library_id = '/Users/ethan/Documents/CoreFiles/DocumentsFile/【个人资料】/被应用程序调用的账号密码文本文件/Zotero_Library_id.txt'
library_type = "user"
filepath_api_key = '/Users/ethan/Documents/CoreFiles/DocumentsFile/【个人资料】/被应用程序调用的账号密码文本文件/Zotero_API_Key.txt'
filepath_md_txt = 'mdfilestitlename.txt'


# 生成list，存储内容
filepath_md_txt = os.path.realpath(
    os.curdir)+'/ZoteroOperation/data/goal/'+filepath_md_txt

list_md_txt = []
with open(filepath_md_txt, 'r') as f:
    for line in f:
        list_md_txt.append(list(line.strip('\n').split(',')))


# print(list_md_txt)


# list_md_txt=file_md_txt.read().strip('\n').split(',')


# 生成Zotero操作实例
zot = zt.Zotero(library_id=open(filepath_library_id).read(),
                library_type=library_type, api_key=open(filepath_api_key).read())


# zot.file(item=)

items = zot.everything(zot.top())

for md_txt in list_md_txt:
    for item in items:
        if item['data'].__contains__('title') == True:
            if item['data']['title'] == md_txt[0]:
                print('has upload file to item : ',item['data']['title'])
            else:
                print('not match item by get md text : ',md_txt[0])
        else:
            print('the item ',item['data'],' has not key title.')
            


pass
