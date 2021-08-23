// import * as fs from 'fs';
const fs = require('fs')


var path_list_tags = "/Users/ethan/LocalFiles/CodesFile/AO/AutomaticOperation/ZoteroOperation/data/original/list_tags_original_20210823.json";
// 读取文件，用以操作
fs.readFile(path_list_tags, function (err, data) {
    if (err) {
        throw err;
    };
    //// 以下是正文
    // 定义变量
    field_name = 'tag';
    condition = 'contains';
    num = 0; // num=0是手动，num=1是自动。
    re = /：/;
    tag_new = '';
    // 解析成json对象
    list_tags = JSON.parse(data);
    console.log(list_tags);
    for (let i in list_tags) {
        // 构建待对比的pattern
        var tag_splited = list_tags[i][0].split(re);
        console.log(tag_splited);
        tag_new = '【' + tag_splited[0] + '】：' + tag_splited[1];
        
    }
});