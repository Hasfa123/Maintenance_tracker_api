from flask import Flask



#config_name = os.getenv('APP_SETTINGS')  # config_name = "development"
#app = create_app(config_name)
app = Flask(__name__)

if __name__ == '__main__':
    app.run()
