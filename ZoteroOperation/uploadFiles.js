// Get a item that by search.

var zoteroSearch = new Zotero.Search();
zoteroSearch.libraryID = Zotero.Libraries.userLibraryID;
zoteroSearch.addCondition('title', 'is', '系统性风险传递的研究')
var itemIDs = await zoteroSearch.search();
var items = await Zotero.Items.getAsync(itemIDs);
var item = items[0];

// Get an item's attachments
var fulltext = [];
if (item.isRegularItem()) { // not an attachment already
    let attachmentIDs = item.getAttachments();
    for (let id of attachmentIDs) {
        let attachment = Zotero.Items.get(id);
        if (attachment.attachmentContentType == 'application/pdf'
                || attachment.attachmentContentType == 'text/html') {
            fulltext.push(await attachment.attachmentText);
        }
    }
}
return fulltext;