
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