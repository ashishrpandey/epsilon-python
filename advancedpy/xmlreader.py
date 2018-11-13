
import xmltodict
def getloglevel():
	with open ("server.xml", 'r') as fileobj:
		a=xmltodict.parse(fileobj.read())
		print(a["server"]["log"]["log-level"])
		print(a["server"]["thread-pool"]["max-threads"])


getloglevel()
