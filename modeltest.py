from classtree import ClassTree 
from classitem import ClassItem 

if __name__=='__main__':
	root = ClassItem(0,'root','root')
	root.setLocation([0,0],[100,100])
	artifical = root.addChild(101,'Artifical Surface','Artifical')
	bare = root.addChild(102,'Bare or Lightly-vegetated Surface')
	artifical.addChild(1,'Built-up area','built')
	bare.setLocation([10,10],[1000,300])
	tree = ClassTree(root)
	tree.fromJSONString(tree.toJSONString())
	print tree.toJSONString()
