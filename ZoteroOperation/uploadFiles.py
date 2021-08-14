
from pyzotero import zotero as zt


## setting
filepath_library_id='/Users/ethan/Documents/CoreFiles/DocumentsFile/【个人资料】/被应用程序调用的账号密码文本文件/Zotero_Library_id.txt';
library_type="user";
filepath_api_key='/Users/ethan/Documents/CoreFiles/DocumentsFile/【个人资料】/被应用程序调用的账号密码文本文件/Zotero_API_Key.txt';

zot=zt.Zotero(library_id=open(filepath_library_id).read(),library_type=library_type,api_key=open(filepath_api_key).read())
