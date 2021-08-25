// ---------------
// 程序：遍历每一个tag于tags列表中，重命名检索获得的相关item之tag之名称（未验证）

//// 设置项：
field_name = 'tag';
condition = 'is';
var num = 0; // num=0是手动，num=1是自动。
var str_re = "^(.*[^】]：.*)";
var str_split = "：";
var tag_new = "";
var name_tag_old = "";
var name_tag_new = "";
var path_list_tags = "/Users/ethan/LocalFiles/CodesFile/AO/AutomaticOperation/ZoteroOperation/data/original/list_tags_original_202108260012.json";
var pathname_output = "/Users/ethan/LocalFiles/CodesFile/AO/AutomaticOperation/ZoteroOperation/data/output/output_202108260012.txt";
var str_output = "";

//// 以下是正文
var count_tag_updated = 0;
var re = new RegExp(str_re);
// 获取数据，从json文件
var data_list_tags = Zotero.File.getContents(path_list_tags);
// 解析成json对象
list_tags = JSON.parse(data_list_tags);
// 遍历tag列表
for (let i in list_tags) {
    name_tag_old = list_tags[i][0];
    //return name_old
    // 判断该tag是否需要重命名：如果有匹配到相关字符串，则需要重命名
    if (name_tag_old.match(re)) {
        // 构建待对比的pattern
        let tag_splited = name_tag_old.split(str_split);
        name_tag_new = '【' + tag_splited[0] + '】：' + tag_splited[1];

        //// 以下操作Zotero
        let zotero_search = new Zotero.Search();
        zotero_search.libraryID = ZoteroPane.getSelectedLibraryID();
        zotero_search.addCondition(field_name, condition, name_tag_old);
        var id_items = await zotero_search.search();
        if (!id_items.length) {
            return "No items found";
        }
        items = Zotero.Items.get(id_items);
        await Zotero.DB.executeTransaction(async function () {
            for (let item of items) {
                item.removeTag(name_tag_old)
                item.addTag(name_tag_new, num);
                await item.save({
                    skipDateModifiedUpdate: true
                });
                // 累加输出结果
                str_output += "item title [ " + item.getField('title') + " ] has updated name of tag.\n";
            }
            // 累加输出结果
            str_output += items.length + " items has updated name of tag from [ " + name_tag_old + " ] to [ " + name_tag_new + " ] .\n";
        });
        // 计数已经重命名的tag个数
        count_tag_updated += 1;
    } else {
        // 累加输出结果
        str_output += "tag [ " + name_tag_old + " ] do not need rename.\n";
    }
}
// 累加输出结果
str_output += count_tag_updated + " tags updated.\n"
// 写出输出结果文件
await Zotero.File.putContentsAsync(pathname_output, str_output);
return count_tag_updated + " tags updated.";




//// 以下是测试：
// // 测试是否能够匹配正确变量名用的，在实际操作中，Zotero Client用不上。
// // 定义变量
// var field_name = 'tag';
// var condition = 'contains';
// var num = 0; // num=0是手动，num=1是自动。
// var str_re = "^(.*[^】]：.*)";
// var str_split="：";
// var tag_new = "";
// var name_old = "";
// var name_new = "";
// // 设置变量
// // import * as fs from 'fs';
// const fs = require('fs')
// var re = new RegExp(str_re);
// var path_list_tags = "/Users/ethan/LocalFiles/CodesFile/AO/AutomaticOperation/ZoteroOperation/data/original/list_tags_original_20210824.json";
// // 读取文件，用以操作
// fs.readFile(path_list_tags, function (err, data) {
//     if (err) {
//         throw err;
//     };
//     //// 以下是正文
//     // 解析成json对象
//     list_tags = JSON.parse(data);
//     console.log(list_tags);
//     // 遍历tag列表
//     for (let i in list_tags) {
//         name_old = list_tags[i][0];
//         // 判断该tag是否需要重命名：如果有匹配到相关字符串，则需要重命名
//         if (name_old.match(re)) {
//             // 构建待对比的pattern
//             let tag_splited = list_tags[i][0].split(str_split);
//             name_new = '【' + tag_splited[0] + '】：' + tag_splited[1];
//         }
//     }
// });