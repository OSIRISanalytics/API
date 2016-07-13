# API
API definitions and call functions for each betting API


#Tom's Notes

* Use python module rpy2 to run r script, return R dataframe, and convert to pandas dataframe
* Don't use command line base to integrate the two languages
* Optional argument in script (Archive = True) to control logging of data to database
* Database will be sqlite db which has integration with python (sqlite3) and R (RSQLite)
* Db connection will only be opened at archive point.

#Cals's Notes

*Use the working code directory, you will need to download your own certs and create your own login file (with your account details)
*ATM it just logs in, sends a keepalive, gets account details, gets some market data
