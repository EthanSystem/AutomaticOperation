#!/bin/bash

# 定义文件夹路径
cd ./data/original
# 获取路径下每个md文件，复制到mdfiles文件夹
find . -name '*.md' -print -exec cp '{}' ../mdfiles \;
# 对mdfiles文件夹之文件名，生成txt
ls -R ./data/mdfiles > ./data/goal/mdfilesname.txt





