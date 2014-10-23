from loader import Loader


class ExampleLoader(Loader):
	@classmethod
	def competent(cls,url):
		return True or False
	def check_out(self):
		self.command = ("echo", "-n", "Hallo", "Welt")
		return True

ExampleLoader.register()


