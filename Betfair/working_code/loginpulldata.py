import login
import pandas as pd
from betfair import utils
from betfair import models
from betfair import exceptions

#Tom
#client = login.login('Np2HwoLYyAQk2X6s', 'tombish22','parksandrec19')
# Cal
client = login.login('eTnX7n6jsiaoGA9g', 'calhamd@gmail.com','wyeslsc10')

from betfair.models import MarketFilter
from betfair.models import PriceProjection
from betfair.models import ExBestOffersOverrides
from betfair.models import MarketData

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

#Fetch all the betting markets
betting_markets = client.list_market_catalogue(MarketFilter(event_type_ids=[sport_event_type.event_type.id], market_type_codes=[MarketType]), market_projection =  ['COMPETITION','EVENT','EVENT_TYPE','RUNNER_DESCRIPTION','MARKET_START_TIME'])
print 'Markets on Sport: ' + str(len(betting_markets))

print betting_markets[0].serialize()

#find out how many are non zero
key = 0
for eachMarket in betting_markets:
    if eachMarket.total_matched > 0:
	    key = key+1                 
print 'Non-Zero Markets on Sport: ' + str(key)

#Gets the list of market IDs in the Betting Market
sports_market_ids = []
for eachMarket in betting_markets:
    sports_market_ids = sports_market_ids + [eachMarket.market_id]

#Get the MarketBookResults
maxpullsize = 100
index=0
print len(sports_market_ids)
marketbook_result = []
while index+maxpullsize < len(sports_market_ids):
	marketbook_result = marketbook_result + client.list_market_book([sports_market_ids[index:index+maxpullsize]],PriceProjection(price_data=['EX_BEST_OFFERS'],exBestOffersOverrides=ExBestOffersOverrides(best_prices_depth=1)))
	index=index+maxpullsize
marketbook_result = marketbook_result + client.list_market_book([sports_market_ids[index:len(sports_market_ids)]],PriceProjection(price_data=['EX_BEST_OFFERS'],exBestOffersOverrides=ExBestOffersOverrides(best_prices_depth=1)))	

print 'Compiling Dataset'
market_data = []
for market in betting_markets:
    next_market_data = MarketData(market,next((x for x in marketbook_result if x.market_id == market.market_id), None))
    market_data.append(next_market_data)


print 'Creating individual runner data'
runner_data = []
for mindex, market in enumerate(market_data):
    print mindex
    for rindex, runner in enumerate(market.runners):
        runner_to_add = {'Market ID': market.market_id, 
                            'Market Name': market.market_name, 
                            'Market Start Time': market.market_start_time,
                            'Total_Matched':market.total_matched,
                            'Active Runners':market.number_of_active_runners,
                            'Status':market.status,
                            'Total Available':market.total_available,
                            'Total Matched':market.total_matched,
                            'Selection ID':market.runner_catalog[rindex].selection_id,
                            'Runner Name':market.runner_catalog[rindex].runner_name,
                            'Price Selection ID':runner.selection_id,
                            'Runner status':runner.status
                            }
        
        if len(runner.ex.available_to_back)>0:
            runner_to_add.update({                         
                            'available_to_back_price':runner.ex.available_to_back[0].price,
                            'available_to_back_market':runner.ex.available_to_back[0].size
                            })
        if len(runner.ex.available_to_lay)>0:
            runner_to_add.update({                         
                            'available_to_lay_price':runner.ex.available_to_lay[0].price,
                            'available_to_lay_market':runner.ex.available_to_lay[0].size
                            })
        runner_data.append(runner_to_add)


MarketDf = pd.DataFrame(runner_data)
print MarketDf


#def convertDF(input):
    #for market in input:
        #Create Game Columns
        
#client.logout()