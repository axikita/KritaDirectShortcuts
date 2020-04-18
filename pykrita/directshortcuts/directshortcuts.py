from krita import *

class DirectShortcuts(Extension):
	def __init__(self, parent):
		#This is initialising the parent, always  important when subclassing.
		super().__init__(parent)

	def setup(self):
		pass

	def createActions(self, window):
		action1 = window.createAction("setOpacity10","setOpacity10","tools/scripts") #unique id, name in tools menu, menu to place option in.
		action1.triggered.connect(self.setOpacity10)

		action2 = window.createAction("setOpacity20","setOpacity20","tools/scripts") #unique id, name in tools menu, menu to place option in.
		action2.triggered.connect(self.setOpacity20)

		action3 = window.createAction("setOpacity30","setOpacity30","tools/scripts") #unique id, name in tools menu, menu to place option in.
		action3.triggered.connect(self.setOpacity30)

		action4 = window.createAction("setOpacity40","setOpacity40","tools/scripts") #unique id, name in tools menu, menu to place option in.
		action4.triggered.connect(self.setOpacity40)

		action5 = window.createAction("setOpacity50","setOpacity50","tools/scripts") #unique id, name in tools menu, menu to place option in.
		action5.triggered.connect(self.setOpacity50)

		action6 = window.createAction("setOpacity60","setOpacity60","tools/scripts") #unique id, name in tools menu, menu to place option in.
		action6.triggered.connect(self.setOpacity60)

		action7 = window.createAction("setOpacity70","setOpacity70","tools/scripts") #unique id, name in tools menu, menu to place option in.
		action7.triggered.connect(self.setOpacity70)

		action8 = window.createAction("setOpacity80","setOpacity80","tools/scripts") #unique id, name in tools menu, menu to place option in.
		action8.triggered.connect(self.setOpacity80)

		action9 = window.createAction("setOpacity90","setOpacity90","tools/scripts") #unique id, name in tools menu, menu to place option in.
		action9.triggered.connect(self.setOpacity90)

		action10 = window.createAction("setOpacity100","setOpacity100","tools/scripts") #unique id, name in tools menu, menu to place option in.
		action10.triggered.connect(self.setOpacity100)



	def setOpacity10(self):
		Krita.instance().activeWindow().activeView().setPaintingOpacity(.1)

	def setOpacity20(self):
		Krita.instance().activeWindow().activeView().setPaintingOpacity(.2)

	def setOpacity30(self):
		Krita.instance().activeWindow().activeView().setPaintingOpacity(.3)

	def setOpacity40(self):
		Krita.instance().activeWindow().activeView().setPaintingOpacity(.4)

	def setOpacity50(self):
		Krita.instance().activeWindow().activeView().setPaintingOpacity(.5)

	def setOpacity60(self):
		Krita.instance().activeWindow().activeView().setPaintingOpacity(.6)

	def setOpacity70(self):
		Krita.instance().activeWindow().activeView().setPaintingOpacity(.7)

	def setOpacity80(self):
		Krita.instance().activeWindow().activeView().setPaintingOpacity(.8)

	def setOpacity90(self):
		Krita.instance().activeWindow().activeView().setPaintingOpacity(.9)

	def setOpacity100(self):
		Krita.instance().activeWindow().activeView().setPaintingOpacity(1)

# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(DirectShortcuts(Krita.instance()))