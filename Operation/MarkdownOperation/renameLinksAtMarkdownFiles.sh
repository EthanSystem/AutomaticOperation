#!/bin/bash

## renameLinksAtMarkdownFiles
## 重命名Markdown文件内的链接为Zotero相应的文件

# 设置区
replaced=${1}
replace=${2}
input=${3}
output=${4}
# cd ./ZoteroOperation/data/mdfiles
# replaced="(?<=\[\[)(\(.*[^等], .*\))(?=\]\])"
# replaced="^(.*)(\[\[\()(.*)\, (.*)(\)\]\])(.*)$"
# replace='{"author":"\3","year":"\4"},'
# 操作区
# 提取作者
re="s/"${replaced}"/"${replace}"/p"
sed -En ${re} ${input} > ${output}











