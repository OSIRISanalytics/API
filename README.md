# API
API definitions and call functions for each betting API


#Tom's Notes

* Use python module rpy2 to run r script, return R dataframe, and convert to pandas dataframe
* Don't use command line base to integrate the two languages
* Optional argument in script (Archive = True) to control logging of data to database
* Database will be sqlite db which has integration with python (sqlite3) and R (RSQLite)
* Db connection will only be opened at archive point.

