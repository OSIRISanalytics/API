import json
import betfair

from betfair import Betfair
client = Betfair('eTnX7n6jsiaoGA9g', ('C:/Users/ECALDOW/Dropbox/OSIRIS/cal_betfair_certs/client-2048.crt', 'C:/Users/ECALDOW/Dropbox/OSIRIS/cal_betfair_certs/client-2048.key'))
print 'Logging in'
client.login('calhamd@gmail.com', 'wyeslsc10')

print 'Keeping alive'
client.keep_alive()

account_details = client.get_account_details()
print account_details
a = account_details.currency_code
print a


from betfair.models import MarketFilter
event_types = client.list_event_types(MarketFilter(text_query='tennis'))
print event_types
print event_types[0]
print event_types[0].event_type

print(len(event_types))                 # 2
print(event_types[0].event_type.name)   # 'Tennis'

tennis_event_type = event_types[0]
markets = client.list_market_catalogue(MarketFilter(event_type_ids=[tennis_event_type.event_type.id]))
print markets[0].market_name                  # 'Djokovic Tournament Wins'

client.logout()