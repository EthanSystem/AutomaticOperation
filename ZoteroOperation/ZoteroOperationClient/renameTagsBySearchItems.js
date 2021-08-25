// ---------------
// 程序：重命名检索获得的相关item之tag之名称
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

