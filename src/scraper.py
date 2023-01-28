URL = 'https://googlecloudcertified.credential.net/'

import requests

x = requests.get(URL)

print(x.text)