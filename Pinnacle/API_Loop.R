library(pinnacle.API)
library(dplyr)

#Setting Options
options(encoding = "UTF-8", stringsAsFactors = FALSE)

#Pinnacle accounts stuff
AcceptTermsAndConditions(TRUE)
SetCredentials("TB882982","Stanimal3#")

League_ID = 5264

#Create an empty dataframe to populate with odds logs
headers = c("Logged_At",names(showOddsDF(sportname = "Soccer", leagueIds = League_ID)))
width = length(headers)
Log = as.data.frame(matrix(0,nrow=100000,ncol = width))
names(Log) = headers

counter = 1

#Running until early morning on Tuesday the 28th of June
while (Sys.time() < '2016-06-28 08:00:00') {
  tryCatch({
  #Query pinnacle
  logThis = showOddsDF(sportname = "Soccer", leagueIds = League_ID) %>%
    filter(PeriodNumber == 0, !grepl("next round",HomeTeamName))
  #Add on the system time
  logThis = cbind(Logged_At=Sys.time(),logThis)
  #Log the record in the dataframe
  Log[counter,] = logThis
  #Incremement your counter by 1
  counter = counter + 1
  },
  error = function(e) {
    print("Something went astray here bishdog")
  })
}

