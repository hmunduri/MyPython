#! /bin/python

user = { 'active': True, 'admin': True, 'name': 'admin' }

if user['admin'] and user['active']:
   print("ACTIVE - (ADMIN) %s" % user['name'])
elif user['admin']:
   print("(ADMIN) %s" % user['name'])
elif user['active']:
   print("ACTIVE - %s" % user['name'])
else:
   print(user['name'])
