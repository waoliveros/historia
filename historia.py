from eve import Eve
from eve_swagger import swagger
from eve.auth import BasicAuth
from config import *
from hashlib import md5

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        accounts = app.data.driver.db['accounts']
        account = accounts.find_one({'username': username})
        return account and md5(password).hexdigest() == account['password']

app = Eve(auth=MyBasicAuth)

app.register_blueprint(swagger)
app.config['SWAGGER_INFO'] = SWAGGER_INFO
app.config['SWAGGER_HOST'] = SWAGGER_HOST

if __name__ == '__main__':
    app.run(host=LISTEN_IP, port=LISTEN_PORT)
