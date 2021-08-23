
// ---------------
// 程序3-2：遍历每一个tag于tags列表中，重命名检索获得的相关item之tag之名称（未验证）
import * as fs from 'fs';
const fs = require('fs')
var field_name = 'tag';
var condition = 'contains';
var num = 0; // num=0是手动，num=1是自动。
var reg = /：/;
var pattern = '';
var path_list_tags = "/Users/ethan/LocalFiles/CodesFile/AO/AutomaticOperation/ZoteroOperation/data/original/list_tags_original_20210823.json";
// const readfile = function (path, callback) {
fs.readFile(path_list_tags, "utf-8", function (err, data) {
    if (err) {
        throw err
    };
    // console.log(data);
    list_tags=JSON.parse(data);
    for (let i in list_tags) {
        // 构建待对比的pattern
        pattern = '';
        var res = list_tags[i][0].split(reg);
        console.log(res)
    }
});
old_name = tag
var zotero_search = new Zotero.Search();
zotero_search.libraryID = ZoteroPane.getSelectedLibraryID();
zotero_search.addCondition(field_name, condition, old_name);
var id_items = await zotero_search.search();
if (!id_items.length) {
    return "No items found";
}
items = Zotero.Items.get(id_items);
await Zotero.DB.executeTransaction(async function () {
    for (let item of items) {
        item.removeTag(old_name)
        item.addTag(new_name, num);
        await item.save({
            skipDateModifiedUpdate: true
        });
    }
});
return items.length + " tag(s) updated";

// ---------------




