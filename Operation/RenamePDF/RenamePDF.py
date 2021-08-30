# encoding:utf-8

'''

需要到：http://pybrary.net/pyPdf/   下载安装pyPdf库

'''

import os
import operator
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader


# 对取得的文件命格式化，去掉其中的非法字符
def format(filename):
    if (isinstance(filename, str)):
        tuple = ('?', '\\', '*', '/', ',', '"', '<', '>',
                 '|', '“', '"', '，', '‘', '”', ',', ':')
        for char in tuple:
            if (filename.find(char) != -1):
                filename = filename.replace(char, "_")
        return filename
    else:
        return 'None'

# 通过递归调用次方法依次遍历文件夹中的每个文件,如果后缀名是.pdf，则对其处理
def VisitDir(path):
    list_path = os.listdir(path)
    for p in list_path:
        pathname = os.path.join(path, p)
        if not os.path.isfile(pathname):
            VisitDir(pathname)
        else:
            back = os.path.splitext(pathname)
            backname = back[1]
            if backname == '.pdf':
                print(pathname)
                rename(pathname)
                

# 文件改名程序
def rename(pathname):
    stream =  open(pathname, "rb")
    input1 = PdfFileReader(stream)
    isEncrypted = input1.isEncrypted
    if not(isEncrypted):
        # 这里的pathname包含路径以及文件名，根据/将起分割成一个list然后去除文件名，保留路径
        list = pathname.split("/")
        oldname = ""
        for strname in list:
            oldname += strname+'/'
        old_filename = oldname[0:len(oldname)-1]
        # 这就是去除文件名
        list.pop()

        string = ""
        for strname in list:
            string += strname+'/'
        print("string= %s" % string)
        title = str(input1.getDocumentInfo().title)
        print("title = %s" % (input1.getDocumentInfo().title))

        title = format(title)
        # 这里就是把先前得到的路径名加上得到的新文件名，再加上后缀名，得到新的文件名
        new_filename = string+title+".pdf"
        print("old=%s " % old_filename)
        print("new = %s " % new_filename)
        # 这里一定要对新的文件名重新定义编码格式
        new_filename = new_filename.encode('utf-8')
        # 关闭文件流，不然无法更名
        stream.close()
        if(str(title) != "None"):
            try:
                os.rename(old_filename, new_filename)
            except WindowsError as e:
                 # print(str(e))
                print(e)
        else:
            print("The file contian no title attribute!")
    else:
        print("This file is encrypted!")


if __name__ == "__main__":
    path = r"/Users/ethan/LocalFiles/CodesFile/RenamePDF/resources"
    VisitDir(path)
