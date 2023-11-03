from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile


class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        qfile_stats = QFile('QTwindow/qt_ORC.ui')
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(qfile_stats)

        self.ui.pushButton_clear.clicked.connect(self.ui.textEdit.clear)


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()

