
// ---------------
// 程序：遍历每一个tag于tags列表中，重命名检索获得的相关item之tag之名称（未验证）
var num = 0; // num=0是手动，num=1是自动。
var str_re = "：";
var re = /^(【.*】：.*)/;
var tag_new = "";
var name_old = "";
var name_new = "";
var path_list_tags = "/Users/ethan/LocalFiles/CodesFile/AO/AutomaticOperation/ZoteroOperation/data/original/list_tags_original_20210824.json";


//// 以下是正文

// import * as fs from 'fs';
// const fs = require('fs')
var re = new RegExp(str_re);

// 获取数据，从json文件
var data_list_tags = Zotero.File.getContents(path_list_tags);
// 解析成json对象
list_tags = JSON.parse(data_list_tags);

// 遍历tag列表
for (let i in list_tags) {
    name_old = list_tags[i][0];
    // 判断该tag是否需要重命名：如果有匹配到相关字符串，则需要重命名
    if (name_old.match(re)==false) {
        // 构建待对比的pattern
        var tag_splited = name_old.split(re);
        name_new = '【' + tag_splited[0] + '】：' + tag_splited[1];
        return name_new
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


//// 以下是Zotero Client用不到的

// import * as fs from 'fs';
// const fs = require('fs')
// var field_name = 'tag';
// var condition = 'contains';
// var num = 0; // num=0是手动，num=1是自动。
// var reg = /：/;
// var pattern = '';
// var path_list_tags = "/Users/ethan/LocalFiles/CodesFile/AO/AutomaticOperation/ZoteroOperation/data/original/list_tags_original_20210823.json";
// // const readfile = function (path, callback) {
// fs.readFile(path_list_tags, "utf-8", function (err, data) {
//     if (err) {
//         throw err
//     };
//     // console.log(data);
//     list_tags=JSON.parse(data);
//     for (let i in list_tags) {
//         // 构建待对比的pattern
//         pattern = '';
//         var res = list_tags[i][0].split(reg);
//         console.log(res)
//     }
// });
// old_name = tag
// var zotero_search = new Zotero.Search();
// zotero_search.libraryID = ZoteroPane.getSelectedLibraryID();
// zotero_search.addCondition(field_name, condition, old_name);
// var id_items = await zotero_search.search();
// if (!id_items.length) {
//     return "No items found";
// }
// items = Zotero.Items.get(id_items);
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

// ---------------




