#!/usr/bin/env python
 
import requests
 
#openssl x509 -x509toreq -in certificate.crt -out CSR.csr -signkey privateKey.key
#app key = eTnX7n6jsiaoGA9g
 
payload = 'username=calhamd@gmail.com&password=wyeslsc10'
headers = {'X-Application': 'SomeKey', 'Content-Type': 'application/x-www-form-urlencoded'}
 
resp = requests.post('https://identitysso.betfair.com/api/certlogin', data=payload, cert=('certs/client-2048.crt', 'certs/client-2048.key'), headers=headers)
 
if resp.status_code == 200:
  resp_json = resp.json()
  print resp_json['loginStatus']
  print resp_json['sessionToken']
else:
  print "Request failed."