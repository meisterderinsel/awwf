from loader import Loader
import urllib.request
import re


class DreisatLoader(Loader):
	@classmethod
	def competent(cls,url):
		return "3sat.de/mediathek/" in url
	def check_out(self):
		regex = re.compile("<url>(.*?)</url>")
		id = [i for i in self.url.rsplit("/", 1)[1].split("&") if i.startswith("obj=")][0].split("=")[1]
		with urllib.request.urlopen("http://www.3sat.de/mediathek/xmlservice/web/beitragsDetails?ak=web&id=%s" % id) as stream:
			conf = stream.read().decode()
		find = conf.split('formitaet basetype="vp8_vorbis_webm_http_na_na"', 1)[1]
		find = find.split("<quality>veryhigh</quality>")[1]
		url = regex.search(find).group(1)
		
		self.command = ("wget", "-q", "-O", self.file, url)
		
		return True




DreisatLoader.register()


