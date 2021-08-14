
# -*- coding:utf-8 -*-
import os
import re
import time


def substitute_batch(root_path):
    for root, dirs, files in os.walk(root_path, topdown=False):
        # 循环文件
        for file_name in files:
            file_name_split = file_name.split('.')

            try:
                if file_name_split[-1] == 'md':
                    # 找到md文件并且复制一份md文件路径
                    file_path_md_from = os.path.join(root, '.'.join(file_name_split))
                    file_path_md_to = os.path.join(root, '.'.join([f'{file_name_split[0]}_copy', file_name_split[1]]))
                    #
                    # 打开md文件然后进行替换
                    with open(file_path_md_from, 'r', encoding='utf8') as file_read, open(file_path_md_to, 'w', encoding='utf8') as file_write:
                    # with open(file_path_md_from, 'r', encoding='utf8') as file_read:
                        data_from = file_read.read()
                        data_to = data_from

                        ########### 代码区之部分：需要替换的项目 ########################

                        ## 1. 加上HTML标签<date></date>
                        # data_matched = re.findall('### <datetime>',data_from,flags=re.MULTILINE)
                        # for idx in range(len(data_matched)):
                        #     data_to = data_to.replace(data_matched[idx],'</date>\n\n### <date><datetime>')

                        ## 2. 如果一个日期里面没有场景HTML标签，则添加之。
                        # li_data_matched_020 = re.findall(pattern='###\s<date>[\w\W]*?</date>',string=data_from,flags = re.MULTILINE)
                        # for idx in range(len(li_data_matched_020)):
                        #     pos_data_matched_030 = re.search(pattern='<sence[\w\W]*?</sence>',string= li_data_matched_020[idx],flags=re.MULTILINE)
                        #     if pos_data_matched_030==None:
                        #         print(idx)
                        #         pos_data_matched_040 = re.search(pattern=re.escape(li_data_matched_020[idx]),string=data_to)
                        #         print(pos_data_matched_040.span())
                        #         # pos_data_matched_045 = re.search(pattern=li_data_matched_020[idx],string=li_data_matched_020[idx])
                        #         str_data_subed_040 = re.sub(pattern='(###\s<date>.*)',repl='\g<1>\n\n<sence number="1">场景1：\n\n</sence>\n\n',string=li_data_matched_020[idx])
                        #         data_to = data_to.replace(data_to[pos_data_matched_040.start():pos_data_matched_040.end()],str_data_subed_040)
                        #         pass


                        ## TODO3. 场景标签组要嵌套内容。



                        ## TODO4. 类别标签放入场景标签里面，且在嵌套内容前面。




                        ################################################

                        file_write.write(data_to)  # 新文件一次性写入原文件内容


                    # 删除原文件
                    os.remove(file_path_md_from)

                    # 重命名新文件名为原文件名
                    os.rename(file_path_md_to, file_path_md_from)
                    print(f'{file_path_md_from} done...')
                    time.sleep(0.5)
            except FileNotFoundError as e:
                print(e)
        time.sleep(0.5)


if __name__ == '__main__':
    top = r'/Users/ethan/LocalFiles/CodesFile/AO/AutomaticOperation/SubstituteTexts/data/test'
    substitute_batch(top)
