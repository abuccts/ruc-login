import sys
import urllib2
import cookielib

def ruclogin(usrname, passwd):
	loginUrl = 'http://10.12.16.122'
	try:
		cookie = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
		opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
		postData = 'DDDDD=' + usrname + '&upass=' + passwd + '&0MKKey=123456&R6=1'
		op = opener.open(loginUrl, postData)
		data = op.read()
		#print data
	except Exception, e:
		print e

ruclogin(sys.argv[1], sys.argv[2])

