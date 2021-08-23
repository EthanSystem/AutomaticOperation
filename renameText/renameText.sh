#!/bin/bash
# Ethan Lin

## TODO 程序：重命名文件内之内容，替换以正则表达式规则。

# 定义文件夹路径
cd ./ZoteroOperation/data/original
# 正则替换文本内容，然后写入新的txt文件
sed 's/^\([^】]*\)：\(.*\)$/【\1】：\2/' list_tags_original.txt | sed 's/^\([^】]*\)：\(.*\)$/\[\"【\1】：\2\"\],/' list_tags_original.txt

