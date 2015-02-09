from classitem import ClassItem
from PyQt4.QtGui import QGraphicsItem, QBrush, QColor, QPainter, QTextOption
from PyQt4.QtCore import QRectF, Qt, QPoint

# Do not have graphics representation for root node


LEAFRECTSIZE = [30,20]
STRACHFACTOR = 4
LEAFCOLOR = QColor(0x2E8AE6)  #Dark Bule
COLORFACTOR = 1.25
OFFSET = 10




class ClassGraphicsItem(QGraphicsItem):
	def __init__(self,model,parent=None,size=None,color=None):
		super(ClassGraphicsItem,self).__init__(parent)
		self.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsMovable| QGraphicsItem.ItemClipsChildrenToShape | QGraphicsItem.ItemSendsGeometryChanges)
		self.model = model
		self._offset = 0
		self.depth = 0
		self.setGeometry()
		if size:
			self.rect = QRectF(-size[0]/2,-size[1/2],size[0],size[1])
		if color:
			self.color = color
		if self.model.location:
			self.setPos(*self.model.location[0])
		if not self.model.isLeaf():
			for child in self.model.childIter():
				ClassGraphicsItem(child,parent = self)
		self.setCursor(Qt.PointingHandCursor)


	def boundingRect(self):
		return self.rect.adjusted(-1,-1,1,1)

	def paint(self,painter,option,widget):
		if self.isSelected():
			painter.setPen(Qt.DashLine)
		else:
			painter.setPen(Qt.NoPen)
		painter.setBrush(QBrush(self.color))
		painter.drawRoundedRect(self.rect,5,5)
		painter.setPen(Qt.SolidLine|Qt.black)
		painter.drawText(self.rect,str(self.model.id()),option=QTextOption(Qt.AlignCenter))

	def addChild(self,modeldata):
		# self.model.addChild(modeldata)
		child=ClassGraphicsItem(modeldata,parent=self)

		child.setPos(self.x()+self.offset,self.y()+self.offset)
		self._offset+=OFFSET

		self.setGeometry()
		self.update()

	def setGeometry(self):
		if self.depth != self.model.depth():
			self.depth = self.model.depth()
			strachfactor = STRACHFACTOR**(self.depth-1)
			size = LEAFRECTSIZE[0]*strachfactor,LEAFRECTSIZE[1]*strachfactor
			self.rect = QRectF(-size[0]/2,-size[1]/2,size[0],size[1])
			colorfactor = COLORFACTOR**(self.depth-1)*100
			self.color = LEAFCOLOR.lighter(colorfactor)
			self.prepareGeometryChange()

	def mousePressEvent(self,event):
		self.setSelected(not self.isSelected())
		self.update()
		event.accept()

	def itemChange(self,change,value):
		if change == QGraphicsItem.ItemPositionHasChanged:
			self.model.setLocation([self.x(),self.y()],[self.scenePos().x(),self.scenePos().y()])
		super(ClassGraphicsItem,self).itemChange(change,value)





