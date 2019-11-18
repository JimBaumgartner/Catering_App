from flask import Flask

app = Flask(__name__)



@app.route("/")
def hello():
  return "Hello World"


@app.route("/login", methods=['POST'])
def auth_login():
  return "login page"


@app.route("/register", methods=['POST'])
def auth_register():
  return "register page"


@app.route("/logout", methods=['POST'])
def auth_logout():
  return "logout route hit"


@app.route("/new", methods=['POST'])
def event_new():
  return "event_new route hit"


@app.route("/all", methods=['GET'])
def event_all():
  return "a list of all events list hit"

if __name__ == "__main__":
  app.run(debug = True)

