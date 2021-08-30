#!/bin/bash

## renameLinksAtMarkdownFiles
## 重命名Markdown文件内的链接为Zotero相应的文件

## 程序1：用命令sed
# 设置区
# cd ./ZoteroOperation/data/mdfiles
# replaced=${1}
# replace=${2}
# input=${3}
# output=${4}
# replaced="(?<=\[\[)(\(.*[^等], .*\))(?=\]\])"
replaced="^(.*)(\[\[\()(.*)\, (.*)(\)\]\])(.*)$"
replace='{"author":"\3","year":"\4"},'
input="/Users/ethan/LocalFiles/CodesFile/AO/AutomaticOperation/data/mdfiles/original.txt"
output="/Users/ethan/LocalFiles/CodesFile/AO/AutomaticOperation/data/output/output_01.txt"
# 操作区
# 提取作者
re="s/"${replaced}"/"${replace}"/p"
sed -En "${re}" ${input} > ${output}


## 程序2：用命令grep
cd data
replaced='(\[\[\()(.*)\,\s(.*)(\)\]\])'
replace='{"author":"\3","year":"\4"},'
# grep -E "${replaced}" ./mdfiles/original.txt > ./output/output_01.txt
egrep -o "${replaced}" ./mdfiles/original.txt > ./output/output_01.txt













