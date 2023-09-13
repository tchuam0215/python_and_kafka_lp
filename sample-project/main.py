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

# start the ssh agent
# eval "$(ssh-agent -s)"

# kill an agent
# ssh-agent -k

# test the ssh connections 
# ssh -T git@github.com

# list all ssh agents
# ls -al ~/.ssh

# add ssh key to ssh agent
# ssh-add ~/.ssh/id_rsa



