# a tree structure group of classitems 
from classitem import ClassItem 

class ClassTree(object):
	"""docstring for ClassTree"""
	def __init__(self, root=None):
		super(ClassTree, self).__init__()
		self.root = root

	def locateDescendantByID(id,currentNode):
		if currentNode.id() == id:
			return currentNode
		for child in currentNode.childIter():
			result = locateDescendantByID(id,child)
			if result:
				return result
		return None

	def toXML(self):
		pass

	def loadFromXML(self):
		pass

	




		