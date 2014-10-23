import subprocess




class Loader:
	loaders = []
	@classmethod
	def register(cls):
		cls.loaders.append(cls)
	@classmethod
	def competent(self,url):
		pass
	@classmethod
	def find_loader(cls,url):
		for i in cls.loaders:
			if i.competent(url): return i
		return None
	def __init__(self, url, file):
		self.url = url
		self.file = file
		self.command = None
	def check_out(self): #return True iff everything went good
		pass
	def print_command(self):
		print("Calling: \"%s\"" % " ".join(self.command))
	def download(self):
		subprocess.call(self.command)







