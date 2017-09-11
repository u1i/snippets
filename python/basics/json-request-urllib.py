import json
import urllib2

data = json.dumps({
    "name": "John"
})

req = urllib2.Request("https://hookb.in/Ekqpak7k")
req.add_header("Content-Type", "application/json")

response = urllib2.urlopen(req, data)
res = response.read()
response.close()

print res
