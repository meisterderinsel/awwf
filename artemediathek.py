from loader import Loader
import urllib.request
import json


class ArteMediathekLoader(Loader):
	@classmethod
	def competent(cls,url):
		return "www.arte.tv/guide" in url
	def check_out(self):
		videoid = self.url.split("/guide/de/")[1].split("/")[0]
		config = "http://org-www.arte.tv/papi/tvguide/videos/stream/player/D/%s_PLUS7-D/ALL/ALL.json" % videoid
		with urllib.request.urlopen(config) as stream:
			text = stream.read().decode()
		j = json.loads(text)
		j = j["videoJsonPlayer"]["VSR"]
		if "RTMP_SQ" in j:
			j = j["RTMP_SQ"]
		elif "RTMP_SQ_1" in j:
			j = j["RTMP_SQ_1"]
		else:
			return False
		
		r = j["streamer"]
		y = "mp4:" + j["url"]
		self.command = ("rtmpdump", "-o", self.file, "-r", r, "-y", y)
		
		return True

ArteMediathekLoader.register()


