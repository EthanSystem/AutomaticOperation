流程：
1. 移动原有文献笔记所在文件夹之所有文献笔记到ZotFile管理的文件夹中：
   1. 利用Zotero API for 「JS或者Web」移动笔记到Zotero每一item中；
      1. 定义文件夹路径；
      2. 用shell获取路径下每个md文件，复制到mdfiles文件夹；
      3. 对mdfiles文件夹之文件名，生成txt；
      4. 用Zotero API导入json；
      5. 读取json之每一文件名，循环：
         1. 匹配相关item之id
   2. 利用ZotFile依次重命名且移动文献笔记到ZotFile管理的文件夹中；