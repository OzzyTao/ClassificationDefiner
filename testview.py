from PyQt4.QtGui import *
from PyQt4.QtCore import *
from classtree import ClassTree  
from classitem import ClassItem
from classgraphicsscene import ClassGraphicsScene 
import sys
class ClassDefineDlg(QDialog):
	"""docstring for ClassDefineDlg"""
	def __init__(self, parent=None):
		super(ClassDefineDlg, self).__init__(parent)
		self.layoutUi()

	def layoutUi(self):
		controlLayout = QHBoxLayout()
		self.addButton = QPushButton("Add")
		self.deleteButton = QPushButton("Delete")
		controlLayout.addWidget(self.addButton)
		controlLayout.addWidget(self.deleteButton)

		mainLayout = QVBoxLayout()
		startmodel = ClassItem(0,'root')
		self.classtree = ClassTree(startmodel)
		self.scene = ClassGraphicsScene(QRectF(-500,-500,1000,1000),self.classtree)
		self.view = QGraphicsView(self.scene)
		self.statusBar = QStatusBar()
		mainLayout.addLayout(controlLayout)
		mainLayout.addWidget(self.view)
		mainLayout.addWidget(self.statusBar)
		self.setLayout(mainLayout)

		self.addButton.clicked.connect(self.scene.addClass)
		self.deleteButton.clicked.connect(self.scene.removeClass)
		QObject.connect(self.scene,SIGNAL("StatusMessage(QString)"),self.showMessage)

	def showMessage(self,string):
		self.statusBar.showMessage(string,2000)


if __name__=="__main__":
	app = QApplication(sys.argv)
	dlg = ClassDefineDlg()
	dlg.show()
	app.exec_()





		