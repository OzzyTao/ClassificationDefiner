# abstract model for individual class defination including all information related to the class
# public member: name, description
class ClassItem(object):
	"""docstring for ClassItem"""
	def __init__(self, id, name=None, description=None, parent=None):
		super(ClassItem, self).__init__()
		self._parent = parent
		self._id = id
		self._children = []
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

	def addChild(self,otherItem):
		if isinstance(otherItem,ClassItem):
			self._children.append(otherItem)
			return True
		return False

	def addChild(self, id, name=None, description=None):
		child = ClassItem(id,name,description,self)
		self._children.append(child)
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
				return True
		return False

	def removeChildByID(self,id):
		for i in range(len(self._children)):
			if self._children[i].id == id:
				child = self._children.pop(i)
				del child
				return True
		return False


	def __str__(self):
		return "%-5s%s" % (self._id,self.name)










