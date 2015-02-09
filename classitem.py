# abstract model for individual class defination including all information related to the class
# public member: name, description
from PyQt4.QtCore import QObject, SIGNAL
class ClassItem(QObject):
	"""docstring for ClassItem"""
	def __init__(self, id, name, description=None, parent=None):
		super(ClassItem, self).__init__()
		self._parent = parent
		self._id = id
		self._children = []
		self._depth = 1
		self.name = name
		self.description = description
		self.location = None

	def id(self):
		return self._id

	def parent(self):
		return self._parent

	def setParent(self,otherItem):
		if isinstance(otherItem,ClassItem):
			self._parent = otherItem
			return True
		return False

	def isRoot(self):
		if self._parent:
			return False
		return True

	def isLeaf(self):
		if self._children:
			return False
		return True

	def childIter(self):
		for child in self._children:
			yield child

	def childrenLength(self):
		return len(self._children)

	def addChildItem(self,otherItem):	
		if isinstance(otherItem,ClassItem):
			self._children.append(otherItem)
			otherItem.setParent(self)
			self.checkLevelChange()
			return True
		return False

	def addChild(self, id, name, description=None):
		child = ClassItem(id,name,description,self)
		self._children.append(child)
		self.checkLevelChange()
		return child

	def location(self):
		return self.location

	def setLocation(self,localLoc,globalLoc):
		self.location = localLoc, globalLoc
		return True

	def removeChild(self,item):
		for i in range(len(self._children)):
			if self._children[i] == item:
				child = self._children.pop(i)
				del child
				self.checkLevelChange()
				return True
		return False

	def removeChildByID(self,id):
		for i in range(len(self._children)):
			if self._children[i].id == id:
				child = self._children.pop(i)
				del child
				self.checkLevelChange()
				return True
		return False

	def depth(self):
		maxDepth = 0
		for child in self._children:
			tempdepth = child.depth()
			maxDepth = tempdepth if tempdepth>maxDepth else maxDepth
		return maxDepth+1

	def checkLevelChange(self):
		prev = self._depth
		currentdepth = self.depth()
		if prev!= currentdepth:
			self._depth=currentdepth
			self.emit(SIGNAL("levelChanged(int)"),currentdepth)
			if self._parent:
				self._parent.checkLevelChange()


	def toJSONObject(self):
		childrenObjs = []
		for child in self._children:
			childrenObjs.append(child.toJSONObject())
		return {'id':self._id,
				'name':self.name,
				'description':self.description,
				'location':self.location,
				'children':childrenObjs}

	def __str__(self):
		return "%-5s%s" % (self._id,self.name)










