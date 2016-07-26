from eve import Eve
from eve_swagger import swagger
from config import *

app = Eve()
app.register_blueprint(swagger)

app.config['SWAGGER_INFO'] = SWAGGER_INFO
app.config['SWAGGER_HOST'] = SWAGGER_HOST

if __name__ == '__main__':
    app.run(host=LISTEN_IP, port=LISTEN_PORT)
