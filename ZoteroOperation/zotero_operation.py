import os
from typing import NewType
from pyzotero import zotero as zt


# ---------------------
# 函数：批量添加附件
# ---------------------
def addAttachment(args):
    filepath_md_txt = args['filepath_md_txt']
    zotero_object = args['zotero_object']

    # 生成list，存储内容
    filepath_md_txt = os.path.realpath(
        os.curdir)+'/ZoteroOperation/data/goal/'+filepath_md_txt

    list_md_txt = []
    with open(filepath_md_txt, 'r') as f:
        for line in f:
            list_md_txt.append(list(line.strip('\n').split(',')))

    items = zotero_object.everything(zotero_object.top())

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
# 函数：批量按照正则表达式方式重命名Zotero标签
# -------------
def renameTags(args):
    old_tag = args['old_tag']
    new_tag = args['new_tag']
    zotero_object = args['zotero_object']

    zot_tags = zotero_object.everything(zotero_object.tags(q=old_tag))  # EDIT
    for old_tag in zot_tags:
        new_tag = old_tag.replace(old_tag, new_tag)  # EDIT
        print('Ersetze: %s -> %s' % (old_tag, new_tag))
        # 检索所有item，其之属性有旧的tag。
        items = zotero_object.everything(zotero_object.items(tag=old_tag))
        # 遍历每个item，其被检索出来的那些，添加新tag
        for item in items:
            print('Item Type: %s | Key: %s' %
                  (item['data']['itemType'], item['data']['key']))
            zotero_object.add_tags(item, new_tag)
    # 删除旧的tag
    for old_tag in zot_tags:
        print('update: %s' % old_tag)
        updated = zotero_object.delete_tags(old_tag)
# -------------------------------------


def selectFunction(function, args):
    functions = {
        'add attachment': addAttachment,
        'rename tags': renameTags
    }
    fun_selected = functions.get(function)
    if fun_selected:
        fun_selected(args)
    else:
        print("Not found a function !")


if __name__ == "__main__":

    # 设置Zotero账户信息
    filepath_library_id = '/Users/ethan/Documents/CoreFiles/DocumentsFile/【个人资料】/被应用程序调用的账号密码文本文件/Zotero_Library_id.txt'
    library_type = "user"
    filepath_api_key = '/Users/ethan/Documents/CoreFiles/DocumentsFile/【个人资料】/被应用程序调用的账号密码文本文件/Zotero_API_Key.txt'

    # 生成Zotero操作实例
    zotero_object = zt.Zotero(library_id=open(filepath_library_id).read(),
                              library_type=library_type, api_key=open(filepath_api_key).read())

    # --------------------
    # setting parameter

    # 选择功能函数（以下任意选择一个）：
    # “
    # add attachment
    # rename tags
    # ”

    select_function = 'rename tags'

    args1 = {
        'filepath_md_txt': 'mdfilestitlename.txt',
        'zotero_object': zotero_object
    }

    args2 = {
        'old_tag': '方法：复杂网络',
        'new_tag': '【方法】：复杂网络',
        'zotero_object': zotero_object
    }
    # --------------------

    # 函数：批量添加附件
    selectFunction(function=select_function, args=args2)
