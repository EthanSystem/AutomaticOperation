

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


