import requests

url = "https://www.ibm.com"

r = requests.get(url)

#Obtain status for get request
print(r.status_code)

print(r.encoding)   #returns UTF-8
print(r.request.body)
#print(r.request.headers[:20])

header = r.headers
print(header[:20])

print(r.text[0:100])
