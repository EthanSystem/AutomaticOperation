
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
        if (attachment.attachmentContentType == 'application/pdf'
            || attachment.attachmentContentType == 'text/html') {
            fulltext.push(await attachment.filename);
        }
    }
}
return fulltext;

// ---------------



// ---------------
// 程序2：修改tag之属性「自动、手动」。其中，item.addTag(tag, num)中，num=0是手动，num=1是自动。
var old_name = "内容：国际金融危机";
var num = 1;
var zotero_search = new Zotero.Search();
zotero_search.libraryID = ZoteroPane.getSelectedLibraryID();
zotero_search.addCondition('tag', 'is', old_name);
var items_id = await zotero_search.search();
if (!items_id.length) {
    return "No items found";
}
await Zotero.DB.executeTransaction(async function () {
    for (let id of items_id) {
        let item = Zotero.Items.get(id);
        item.addTag(old_name, num);
        await item.save({
            skipDateModifiedUpdate: true
        });
    }
});
return items_id.length + " tag(s) updated";

// ---------------




// ---------------
// 程序3：修改检索获得的相关item之field之名称（未验证）
var field_name = 'tag';
var condition = 'is';
var old_name = "财政政策";
var new_name = "内容：财政政策";
var zotero_search = new Zotero.Search();
zotero_search.libraryID = ZoteroPane.getSelectedLibraryID();
zotero_search.addCondition(field_name, condition, old_name);
var items_id = await zotero_search.search();
if (!items_id.length) {
    return "No items found";
}
await Zotero.DB.executeTransaction(async function () {
    for (let item_id of items_id) {
        let item = Zotero.Items.get(item_id);
        let mapped_field_id=zot.
        await item.save({
            skipDateModifiedUpdate: true
        });
    }
});
return items_id.length + " tag(s) updated";

// ---------------




// ---------------
// 程序4：修改选取的相关item之field之名称（未验证）
var field_name = 'tag';
var condition = 'is';
var old_name = "财政政策";
var new_name = "内容：财政政策";
var items = Zotero.getActiveZoteroPane().getSelectedItems();
if (!items.length) {
    return "No items found";
}
// return(items)
await Zotero.DB.executeTransaction(async function () {
    for (let item_id of items_id) {
        let item = Zotero.Items.get(item_id);
        let mapped_field_id=zot.
        await item.save({
            skipDateModifiedUpdate: true
        });
    }
});
return items_id.length + " tag(s) updated";

// ---------------