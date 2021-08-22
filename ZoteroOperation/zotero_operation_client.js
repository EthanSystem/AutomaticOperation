// ---------------
// 程序1：批量导入附件（已弃用）
// import md file.
var file_json_title = "./ZoteroOperation/data/goal/mdfilestitlename.json"
var fs = require('fs')
var data_json = JSON.parse(fs.readFileSync(file_json_title))
console.log(data_json)
// Get a item that by search.
var zoteroSearch = new Zotero.Search();
zoteroSearch.libraryID = Zotero.Libraries.userLibraryID;
for (let i in data_json) {
    zoteroSearch.addCondition('title', 'is', data_json[i][0])
    var itemIDs = await zoteroSearch.search();
    var items = await Zotero.Items.getAsync(itemIDs);
    var item = items[0];
    return item;
}
// Get an item's attachments
var fulltext = [];
if (item.isRegularItem()) { // not an attachment already
    let attachmentIDs = item.getAttachments();
    for (let id of attachmentIDs) {
        let attachment = Zotero.Items.get(id);
        if (attachment.attachmentContentType == 'application/pdf' ||
            attachment.attachmentContentType == 'text/html') {
            fulltext.push(await attachment.filename);
        }
    }
}
return fulltext;

// ---------------



// ---------------
// 程序2：修改tag之属性「自动、手动」。其中，item.addTag(tag, num)中，num=0是手动，num=1是自动。
var tag_name = "内容：国际金融危机";
var num = 0; // num=0是手动，num=1是自动。
var zotero_search = new Zotero.Search();
zotero_search.libraryID = ZoteroPane.getSelectedLibraryID();
zotero_search.addCondition('tag', 'is', tag_name);
var items = await zotero_search.search();
if (!items.length) {
    return "No items found";
}
await Zotero.DB.executeTransaction(async function () {
    for (let id of items) {
        let item = Zotero.Items.get(id);
        item.addTag(tag_name, num);
        await item.save({
            skipDateModifiedUpdate: true
        });
    }
});
return items.length + " tag(s) updated";

// ---------------




// ---------------
// 程序3：重命名检索获得的相关item之tag之名称
var field_name = 'tag';
var condition = 'contains';
var num = 0; // num=0是手动，num=1是自动。
var old_name = "压力测试";
var new_name = "【方法】：压力测试";
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





// ---------------
// 程序3-1：遍历每一个tag于tags列表中，重命名检索获得的相关item之tag之名称
var path_list_tags = "/Users/ethan/LocalFiles/CodesFile/AO/AutomaticOperation/ZoteroOperation/data/original/list_tags.json";
var list_tags = await Zotero.File.getContentsAsync(path_list_tags)
return list_tags
var field_name = 'tag';
var condition = 'contains';
var num = 0; // num=0是手动，num=1是自动。
var old_name = "压力测试";
var new_name = "【方法】：压力测试";
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





// ---------------
// 程序4：重命名选取的相关item之tag之名称
var old_name = "";
var new_name = "【内容】：影子银行";
var num = 0; // num=0是手动，num=1是自动。
var items = Zotero.getActiveZoteroPane().getSelectedItems();
if (!items.length) {
    return "No items found";
}
// return(items)
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