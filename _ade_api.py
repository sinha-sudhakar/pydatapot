from flask import Flask,request,app, make_response, render_template,json,g

app = Flask(__name__)


@app.route('/')
def home():
	return "Welcome to GeeksForGeeks !"


@app.route('/basic/', methods=['POST','GET','PUT']) 
def basic():
    if request.method == "POST":   
        print("POST")
        response = make_response()
        response.data = json.dumps({"data":"POST METHOD"})
        response.mimetype = 'application/json'
        return(response)	
    response = make_response()
    response.data = json.dumps({"data":"GET METHOD"})
    response.mimetype = 'application/json'
    return(response)

@app.route('/', subdomain ='practice')
def practice():
	return "Coding Practice Page"


@app.route('/courses/', subdomain ='practice')
def courses():
	return "Courses listed " \
		"under practice subdomain."


if __name__ == "__main__":
	app.run(host="0.0.0.0",port=1234, debug=False)
