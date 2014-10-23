import subprocess




class Loader:
	loaders = []
	@classmethod
	def register(cls):
		cls.loaders.append(cls)
	@classmethod
	def competent(self,url):
		'''return True if you feel competent for this url
		Must be implemented by every subclass.'''
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
	def check_out(self):
		'''do some stuff to retrieve the media file(s).
		Fill the "command"-variable and return True iff everything went good. Don't execute anything yet.
		Must be implemented by every subclass.'''
		pass
	def print_command(self):
		print("Calling: \"%s\"" % " ".join(self.command))
	def download(self):
		subprocess.call(self.command)







