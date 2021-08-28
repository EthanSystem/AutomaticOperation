// Get a item that by search.

https: //api.zotero.org


    // 设置Zotero账户信息
    filepath_library_id = '/Users/ethan/Documents/CoreFiles/DocumentsFile/【个人资料】/被应用程序调用的账号密码文本文件/Zotero_Library_id.txt'
library_type = "user"
filepath_api_key = '/Users/ethan/Documents/CoreFiles/DocumentsFile/【个人资料】/被应用程序调用的账号密码文本文件/Zotero_API_Key.txt'

# 生成Zotero操作实例
zotero_object = zt.Zotero(library_id = open(filepath_library_id).read(),
    library_type = library_type, api_key = open(filepath_api_key).read())