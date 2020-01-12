# import
from flask import Flask
from controller import home

# initial
app = Flask(__name__, static_url_path="", static_folder="assets", template_folder="views")

@app.route("/")
def index():
    home_controller = home.HomeController()
    return home_controller.index()

@app.route('/login', methods=['POST'])
def login():
    return "hello world"

if __name__ == "__main__":  
    app.run(debug=True)