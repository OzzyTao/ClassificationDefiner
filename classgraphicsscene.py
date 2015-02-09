from PyQt4.QtGui import QGraphicsScene
from PyQt4.QtCore import SIGNAL
from classgraphicsitem import ClassGraphicsItem
from classpropertiesdlg import ClassPropertiesDlg 
OFFSET = 10
class ClassGraphicsScene(QGraphicsScene):
	"""docstring for ClassGraphicsScene"""
	def __init__(self,rect,tree, parent=None):
		super(ClassGraphicsScene, self).__init__(rect,parent)
		self.offset=0
		self.installData(tree)

	def installData(self,tree):
		self.datatree = tree
		self.clear()
		if self.datatree.root:
			for topclass in self.datatree.root.childIter():
				self.addNewTopClass(topclass)

	def addNewTopClass(self,model):
		newgraphicsitem = ClassGraphicsItem(model)
		self.addItem(newgraphicsitem)
		newgraphicsitem.setPos(self.offset,self.offset)
		self.offset+=OFFSET
		# if self.views():
		# 	self.views()[0].centerOn(graphicsitem)

	def addClass(self):
		dlg = ClassPropertiesDlg()
		if dlg.exec_():
			cid = int(dlg.idLineEditBox.text())
			name =dlg.nameLineEditBox.text()
			description = dlg.descriptionLineEditBox.toPlainText()
		else:
			return False
		parentItems = self.selectedItems()
		if parentItems:
			model = parentItems[0].model.addChild(cid,name,description)
			parentItems[0].addChild(model)
		else:
			model = self.datatree.root.addChild(cid,name,description)
			self.addNewTopClass(model)
		# self.listClasses()
		return True

	def removeClass(self):
		currentItems = self.selectedItems()
		if currentItems:
			currentModel = currentItems[0].model 
			currentModel.parent().removeChild(currentModel)
			self.removeItem(currentItems[0])
		else:
			self.emit(SIGNAL("StatusMessage(QString)"),'Select a targt class first.')

	def listClasses(self):
		print "-classes:"
		for classitem in self.items():
			print classitem.model.id()



