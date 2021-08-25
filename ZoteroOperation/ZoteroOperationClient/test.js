// 定义变量
var field_name = 'tag';
var condition = 'contains';
var num = 0; // num=0是手动，num=1是自动。
var re = /^(【.*】：.*)/;
var tag_new = "";
var name_old = "";
var name_new = "";


//// 以下是正文

import * as fs from 'fs';
const fs = require('fs')
var re = new RegExp(str_re);

var path_list_tags = "/Users/ethan/LocalFiles/CodesFile/AO/AutomaticOperation/ZoteroOperation/data/original/list_tags_original_20210824.json";
// 读取文件，用以操作
fs.readFile(path_list_tags, function (err, data) {
    if (err) {
        throw err;
    };
    //// 以下是正文

    // 解析成json对象
    list_tags = JSON.parse(data);
    console.log(list_tags);
    // 遍历tag列表
    for (let i in list_tags) {
        name_old = list_tags[i][0];
        // 判断该tag是否需要重命名：如果有匹配到相关字符串，则需要重命名
        if (name_old.includes(re)) {
            // 构建待对比的pattern
            var tag_splited = list_tags[i][0].split(re);
            console.log(tag_splited);
            name_new = '【' + tag_splited[0] + '】：' + tag_splited[1];
            
            // //// 以下操作Zotero
            // items = Zotero.getActiveZoteroPane().getSelectedItems();
            // if (!items.length) {
            //     return "No items found";
            // }
            // // return(items)
            // await Zotero.DB.executeTransaction(async function () {
            //     for (let item of items) {
            //         item.removeTag(old_name)
            //         item.addTag(new_name, num);
            //         await item.save({
            //             skipDateModifiedUpdate: true
            //         });
            //     }
            // });
            // return items.length + " tag(s) updated";
        }
    }
});