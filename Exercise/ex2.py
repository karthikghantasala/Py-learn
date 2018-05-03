user = { 'admin': True, 'active': False, 'name':'sai' }

if user['admin']:
    print ("(ADMIN) %s" % (user['name']))
elif user['active']:
    print ("ACTIVE %s" % (user['name']))
elif user['active'] and user['admin']:
    print ("ACTIVE -(ADMIN) %s" % (user['name']))
elif not user['active'] or not user['admin']:
    print ("%s" % (user['name']))
else:
	print(user['name'])