# 分析常用Zotero操作









### 解决：「批量移动附件到Zotero」

#### 流程：

方案1：
状态：失败；
内容：
1. 移动原有文献笔记所在文件夹之所有文献笔记到ZotFile管理的文件夹中：
   1. 利用Zotero API for 「JS或者Web」移动笔记到Zotero每一item中；
      1. 定义original文件夹路径；
      2. 用shell获取路径下每个md文件，复制到mdfiles文件夹；
      3. 对mdfiles文件夹之文件名，生成txt；
      4. 用Zotero API导入txt；
      5. 遍历读取txt之每一文件名：
         1. 用Pyzotero匹配符合该文本的file所在的item；
            - 如果匹配：
              1. 则获取该item对应的id；
              2. 上传该文本对应的md文件到该item；
            - 如果不匹配：
              1. 则写不匹配文件到文件夹goal；
   2. 对不匹配的md文件，手动移动到Zotero；
   3. 手动移动其它格式文件到Zotero；
   4. 利用ZotFile依次重命名且移动文献笔记到ZotFile管理的文件夹中；

方案2：
状态：成功；
内容
1. 用Shell工具，重新命名md文件名，按照顺序："【title】\_【author】\_【date】"；
2. 手动批量移动md文件到Zotero之collection之名为”Collection“的分类中；
3. 在Zotero全局collection中，排序以title，然后手动移动md文件到Zotero对应的正确的item中；
4. 手动移动其余附件；
5. 手动移动后缀名为assets的附件文件夹至Zotfile管理的文件夹中；
6. 手动排查，删除无关的md附件；


