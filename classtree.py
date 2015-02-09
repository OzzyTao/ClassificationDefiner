# a tree structure group of classitems 
from classitem import ClassItem 
import json
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

	def toJSONString(self):
		return json.dumps(self.root.toJSONObject(),indent=4,separators=(',',':'))

	def fromJSONString(self,jsonstr):
		jsonObject = json.loads(jsonstr)
		self.root = _loadJSONObject(jsonObject)
		return self.root

def _loadJSONObject(jsonDict):
	obj = ClassItem(jsonDict['id'],jsonDict['name'],jsonDict['description'])
	if jsonDict['location']:
		obj.setLocation(*jsonDict['location'])
	for child in jsonDict['children']:
		childitem = _loadJSONObject(child)
		childitem.setParent(obj)
		obj.addChildItem(childitem)
	return obj 

	

	




		