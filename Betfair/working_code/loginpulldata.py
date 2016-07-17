import json
import betfair
import login
import pandas as pd
from betfair import utils
from betfair import models
from betfair import exceptions


#Tom
client = login.login('Np2HwoLYyAQk2X6s', 'tombish22','parksandrec19')
# Cal
#client = login('eTnX7n6jsiaoGA9g', 'calhamd@gmail.com','wyeslsc10')

client.keep_alive()

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

betting_markets = client.list_market_catalogue(MarketFilter(event_type_ids=[sport_event_type.event_type.id], market_type_codes=[MarketType]), market_projection =  ['COMPETITION','EVENT','EVENT_TYPE','RUNNER_DESCRIPTION','MARKET_START_TIME'])
print 'Markets on Sport: ' + str(len(betting_markets))

print vars(betting_markets[0])
print betting_markets[0].competition
print betting_markets[0].event.name
print betting_markets[0].runners[0]
print betting_markets[0].event_type
print "+++++++++++++++++++++++++"

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
print vars(marketbook_result[0])
print vars(marketbook_result[0].runners[0].ex)
print vars(marketbook_result[1].runners[0].ex.available_to_lay[0])

details = betting_markets["market_id" == marketbook_result[0].market_id]



print pd.DataFrame.from_dict(details.__dict__)



def convertDF(output):

    import pandas as pd

    for result in marketbook_result:

        for runner in result.runners:

            details = betting_markets["market_id" == result.market_id].serialize()

            game_id = details["event"]["id"]
            game_name = details["event"]["name"]
            game_start = details["event"]["openDate"]

            sport_id = details["eventType"]["id"]


            runner.selectionId

            for index in details["runners"]:
                if index.selectionId == runner.selectionId:
                    team_name = index.runnerName


            home_team = details["runners"][0]["runnerName"]
            home_id = details["runners"][0]["selectionId"]

            away_team = details["runners"][1]["runnerName"]
            away_id = details["runners"][1]["selectionId"]

            draw_team = details["runners"][2]["runnerName"]
            draw_id = details["runners"][2]["selectionId"]

            details.__dict__

            runner.ex.available_to_back[0]
            runner.ex.available_to_lay[0]

client.logout()