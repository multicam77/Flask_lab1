from flask import Flask,render_template, request        # import flask framework
app = Flask(__name__)             # create an app instance

@app.route("/index")                   # use the home url
def hello():                      # method called hello
    return render_template("index.html")         # returns "hello world"

@app.route("/about")                   # use the home url
def about():                      # method called hello
     name = request.arg.get('name') if request.args.get('name') else "Hello World!" 
     return render_template("about.html", aboutName=name) 

@app.route("/templates/about.html")              # route with URL variable /<name>
def hello_name(name):              # call method hello_name
    return "Hello "+ name          # which returns "hello + name      
if __name__ == "__main__":        # when running python app.py
    app.run(debug=True)                     # run the flask app 