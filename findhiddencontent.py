import requests

url = "https://weratepups.xyz"
hash_value=hash(requests.get(url,headers={'user-agent':'10000'}).text)
for i in range(10000,100000):
	a=str(i)
	headers = {'user-agent': a}
	r=requests.get(url,headers=headers)
	if(hash_value!=hash(r.text)):
		print(i)
