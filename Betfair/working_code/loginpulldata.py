import json
import betfair
from betfair import utils
from betfair import models
from betfair import exceptions

from betfair import Betfair
client = Betfair('eTnX7n6jsiaoGA9g', ('C:/Users/ECALDOW/Dropbox/OSIRIS/cal_betfair_certs/client-2048.crt', 'C:/Users/ECALDOW/Dropbox/OSIRIS/cal_betfair_certs/client-2048.key'))
print 'Logging in'
client.login('calhamd@gmail.com', 'wyeslsc10')


from betfair.models import MarketFilter
from betfair.models import PriceProjection
from betfair.models import ExBestOffersOverrides

MarketSearch = raw_input('Enter Sports String to search: ')

event_types = client.list_event_types(MarketFilter(text_query=MarketSearch))

print 'Sports That Match: ' + str(len(event_types))
key = 0
for events in event_types:
    print 'Key : ' + str(key) + ' Sport: ' + events.event_type.name
    key = key+1

SportSearch = raw_input('Enter Key of Sport:')

sport_event_type = event_types[int(SportSearch)]
print 'Sport Selected: ' + event_types[int(SportSearch)].event_type.name + 'Sport ID: ' + str(sport_event_type.event_type.id)
market_types = client.list_market_types(MarketFilter(event_type_ids=[sport_event_type.event_type.id]))

key = 0
for markets in market_types:
    print 'Key : ' + str(key) + ' Market Types: ' + markets.market_type
    key = key+1

MarketTypeSearch = raw_input('Enter Key of MarketType:')
MarketType = market_types[int(MarketTypeSearch)].market_type

print 'Market Type Selected: ' + MarketType

betting_markets = client.list_market_catalogue(MarketFilter(event_type_ids=[sport_event_type.event_type.id], market_type_codes=[MarketType]))
print 'Markets on Sport: ' + str(len(betting_markets))

key = 0
for eachMarket in betting_markets:
    if eachMarket.total_matched > 0:
	    key = key+1                 
print 'Non-Zero Markets on Sport: ' + str(key)

sports_market_ids = []
for eachMarket in betting_markets:
    sports_market_ids = sports_market_ids + [eachMarket.market_id]
	
maxpullsize = 100
index=0
print len(sports_market_ids)
marketbook_result = []
while index+maxpullsize < len(sports_market_ids):
	marketbook_result = marketbook_result + client.list_market_book([sports_market_ids[index:index+maxpullsize]],PriceProjection(price_data=['EX_BEST_OFFERS'],exBestOffersOverrides=ExBestOffersOverrides(best_prices_depth=1)))
	index=index+maxpullsize
marketbook_result = marketbook_result + client.list_market_book([sports_market_ids[index:len(sports_market_ids)]],PriceProjection(price_data=['EX_BEST_OFFERS'],exBestOffersOverrides=ExBestOffersOverrides(best_prices_depth=1)))	
print len(marketbook_result)
print vars(marketbook_result[0].runners[0].ex)
print vars(marketbook_result[1].runners[0].ex.available_to_lay[0])


client.logout()