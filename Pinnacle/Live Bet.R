library(pinnacle.API)
library(dplyr)

#Setting Options
options(encoding = "UTF-8", stringsAsFactors = FALSE)

#Pinnacle accounts stuff
AcceptTermsAndConditions(TRUE)
SetCredentials("TB882982","Stanimal3#")


Sports = GetSports()


Leagues = GetLeagues("Soccer") 

Odds = showOddsDF(sportname = "Soccer", leagueIds =  5264) %>%
  filter(LiveStatus >= 1) %>% filter(PeriodNumber == 0)
