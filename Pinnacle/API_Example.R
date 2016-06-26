library(pinnacle.API)

#Setting Options
options(encoding = "UTF-8", stringsAsFactors = FALSE)

#Pinnacle accounts stuff
AcceptTermsAndConditions(TRUE)
SetCredentials("TB882982","Stanimal3#")

#NBA Details
Sport_ID = 4
League_ID = 487

#Query pinnacle
logThis = showOddsDF(sportname = "Basketball", leagueIds = League_ID)
