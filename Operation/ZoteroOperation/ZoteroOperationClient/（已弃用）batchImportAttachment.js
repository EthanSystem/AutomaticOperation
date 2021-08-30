// ---------------
// 程序：批量导入附件（已弃用）
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

