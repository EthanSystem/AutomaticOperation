## 程序：重命名各文件名以正则表达式规则。
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