import requests 

url = 'https://manning.com'
#url = 'https://api.github.com'
#url = 'https://httpbin.org/cookies'
#url = 'https://httpbin.org'

# send an http get request to the url
response = requests.get(url)

if response.status_code == 200 :
    print(response.text)    
    #print(response.headers['content-type'])
    #print(response.encoding)
    #print(response.text)
    #print(response.json())

else : 
    print(f"Failed to retrieve the website. Status code: {response.status_code}")




