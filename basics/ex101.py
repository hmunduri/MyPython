#Python program to access and print a URL's content to the console.
from http import HTTPConnection
conn = HTTPSConnection("google.com")
conn.request("GET", "/")
result = conn.getresponse()
contents = result.read()
print(contents)
