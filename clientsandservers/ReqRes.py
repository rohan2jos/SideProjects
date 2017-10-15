import requests

resp = requests.get("http://www.google.com")

print "this is the response object"
print resp

print "status code: " + str(resp.status_code)
print "response ok: " + str(resp.ok)

print "this is the text in the get request"
print resp.text