import os
from typing import NewType
from pyzotero import zotero as zt


# setting
filepath_library_id = '/Users/ethan/Documents/CoreFiles/DocumentsFile/【个人资料】/被应用程序调用的账号密码文本文件/Zotero_Library_id.txt'
library_type = "user"
filepath_api_key = '/Users/ethan/Documents/CoreFiles/DocumentsFile/【个人资料】/被应用程序调用的账号密码文本文件/Zotero_API_Key.txt'



# 生成Zotero操作实例
zot = zt.Zotero(library_id=open(filepath_library_id).read(),
                library_type=library_type, api_key=open(filepath_api_key).read())


# # ---------------------
# # 以下各程序是功能程序


# ---------------------
# 程序一：批量添加附件
# ---------------------
filepath_md_txt = 'mdfilestitlename.txt'

# 生成list，存储内容
filepath_md_txt = os.path.realpath(
    os.curdir)+'/ZoteroOperation/data/goal/'+filepath_md_txt

list_md_txt = []
with open(filepath_md_txt, 'r') as f:
    for line in f:
        list_md_txt.append(list(line.strip('\n').split(',')))

items = zot.everything(zot.top())

for md_txt in list_md_txt:
    for item in items:
        if item['data'].__contains__('title') == True:
            if item['data']['title'] == md_txt[0]:
                print('has upload file to item : ', item['data']['title'])
            else:
                print('not match item by get md text : ', md_txt[0])
        else:
            print('the item ', item['data'], ' has not key title.')

pass
# ---------------------


# ------------
# 程序二：重命名标签（转载）
# -------------
old_tag = '财政政策'
new_tag = '内容：财政政策'
zot_tags = zot.everything(zot.tags(q=old_tag))  # EDIT
for old_tag in zot_tags:
    new_tag = old_tag.replace(old_tag, new_tag)  # EDIT
    print('Ersetze: %s -> %s' % (old_tag, new_tag))
    # 检索所有item，其之属性有旧的tag。
    items = zot.everything(zot.items(tag=old_tag))
    # 遍历每个item，其被检索出来的那些，添加新tag
    for item in items:
        print('Item Type: %s | Key: %s' % (item['data']['itemType'], item['data']['key']))
        zot.add_tags(item, new_tag)
# 删除旧的tag
for old_tag in zot_tags:
    print('update: %s' % old_tag)
    updated = zot.delete_tags(old_tag)
# -------------------------------------
