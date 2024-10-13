from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to pizzeria!"



if __name__ == "__main__":
    app.run(port=5050)

#static for css and image
    #tempaltes for html