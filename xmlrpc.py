from xmlrpclib import ServerProxy

SERVER = 'http://localhost:8069'
DATABASE = 'demo'
USERNAME = 'admin'
PASSWORD = 'shivam'
#info = xmlrpclib.ServerProxy('http://localhost:8069').start()
url, db, username, password = 'http://localhost:8069',DATABASE,USERNAME,PASSWORD

common = ServerProxy('{}/xmlrpc/2/common'.format(url))
print common.version()

#returns uid if True else returns False
uid = common.authenticate(db, username, password, {})
print "uid",uid

models = ServerProxy('{}/xmlrpc/2/object'.format(url))
states = models.execute_kw('demo', uid, password,
    'res.country.state', 'search_read',
    [ [],],
    {'fields': ['name', 'id'], 'limit': False})
    
print "==================states",states
