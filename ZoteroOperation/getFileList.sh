#!/bin/bash

## 程序1
# 定义文件夹路径
cd ./ZoteroOperation/data/original
# 获取路径下每个md文件，复制到mdfiles文件夹
find . -name '*.md' -print -exec cp '{}' ../mdfiles \;
# 对mdfiles文件夹之文件名，生成txt
ls -R ./ZoteroOperation/data/mdfiles > ./ZoteroOperation/data/goal/mdfilesname.txt



## 程序2：去掉文件名后缀名。
# 定义文件夹路径
cat ./ZoteroOperation/data/goal/mdfilesname.txt | while read txtline
do
    bbname=${txtline%.md}
    echo "${bbname}" >> ./ZoteroOperation/data/goal/mdfilesmetaname.txt
done

## 程序3：提取文献之title对应之名称写出到txt文件。
# 定义文件夹路径
re="(.*)_(.*)\.md$"
cat ./ZoteroOperation/data/goal/mdfilesname.txt | while read txtline
do
    if [[ ${txtline} =~ ${re} ]]
    then
        echo ${BASH_REMATCH[2]} >> ./ZoteroOperation/data/goal/mdfilestitlename.txt
    fi
done

## 程序4：重命名md文件名以正则表达式规则。
# 定义文件夹路径
cd ./ZoteroOperation/data/mdfiles
re="^(.*)_(.*)(\.md)$"
for filename in *
do
    if [[ ${filename} =~ ${re} ]]
    then
        mv "${filename}" "${BASH_REMATCH[2]}_${BASH_REMATCH[1]}${BASH_REMATCH[3]}"
    fi
done


