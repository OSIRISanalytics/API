def login(appid, login, pword):

	import json
	import betfair

	from betfair import Betfair

	client = Betfair(appid, ('../../../../Certs/client-2048.crt', '../../../../Certs/client-2048.key'))
	print 'Logging in'
	client.login(login, pword)

	return client
