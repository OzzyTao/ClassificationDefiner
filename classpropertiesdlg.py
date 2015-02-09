from PyQt4.QtGui import QDialog, QLabel, QLineEdit, QValidator, QIntValidator, QDialogButtonBox, QGridLayout, QTextEdit

class ClassPropertiesDlg(QDialog):
	"""docstring for ClassPropertiesDlg"""
	def __init__(self, parent=None):
		super(ClassPropertiesDlg, self).__init__(parent)
		idlabel = QLabel("&ID(Digits)")
		self.idLineEditBox = QLineEdit(self)
		self.idLineEditBox.setValidator(QIntValidator())
		idlabel.setBuddy(self.idLineEditBox)

		namelabel = QLabel("&Name")
		self.nameLineEditBox = QLineEdit(self)
		namelabel.setBuddy(self.nameLineEditBox)

		descriptionlabel = QLabel("&Description")
		self.descriptionLineEditBox = QTextEdit(self)
		descriptionlabel.setBuddy(self.descriptionLineEditBox)

		self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

		layout = QGridLayout()
		layout.addWidget(idlabel,0,0)
		layout.addWidget(self.idLineEditBox,0,1)
		layout.addWidget(namelabel,1,0)
		layout.addWidget(self.nameLineEditBox,1,1,1,3)
		layout.addWidget(descriptionlabel,2,0,1,4)
		layout.addWidget(self.descriptionLineEditBox,3,0,3,4)
		layout.addWidget(self.buttonBox)

		self.setLayout(layout)

		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)
		self.setWindowTitle("Class Properties")


