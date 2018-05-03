#user1 = { 'admin': True, 'active': False, 'name':'sai' }
#user2 = { 'admin': False, 'active': False, 'name':'karthik' }
#user3 = { 'admin': True, 'active': True, 'name':'vivaan' }
#user4 = { 'admin': False, 'active': True, 'name':'arti' }

#users = ['user1','user2','user3','user4']

users={ 'admin': True, 'active': False, 'name':'sai' },{ 'admin': False, 'active': False, 'name':'karthik' },{ 'admin': True, 'active': True, 'name':'vivaan' },{ 'admin': False, 'active': True, 'name':'arti' }
i=1
for user in users:
    print ("Line no %d" % (i))
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
    i += 1