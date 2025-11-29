import re
import requests

request = requests.get("https://www.digikala.com")

print(request.status_code)
