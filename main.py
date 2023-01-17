import os
import re

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import *
from PyQt5 import uic


class MyGUI(QMainWindow):

    def __init(self):
        super(MyGUI, self).__init__()
        uic.loadUi('bulkgui.ui', self)
        self.show()


app=QApplication([])
window=MyGUI()
app.exec_()

# import os
# import re
#
# def rename_files(directory,pattern,newname):
#     files = os.listdir(directory)
#     counter=0
#     for file in files:
#         if re.match(pattern,file):
#          filetype= file.split('.')[-1]
#          os.rename(directory +'/' +file,directory + '/' +newname +str(counter)+'.'+filetype)
#          print(f"Renaming {file} to {newname} {str(counter)} . {filetype}")
#          counter+=1
#
#
# rename_files("F:\\jku uni\\firstsemester\\python I\\projects\\bulk file renaming\\testdir",".*[0-9]","different")
