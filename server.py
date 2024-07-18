#import flask and flask modules
from flask import Flask, render_template, request

# Import the Maths package here
from Maths.mathematics import summation, subtraction, multiplication

#instantiate flask class
app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():

    #get values through the query parameter and add to get the result
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = summation(num1, num2)
    return str(result)

@app.route("/sub")
def sub_route():

    #get values through the query parameter and subtract to get the result
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = subtraction(num1, num2)
    return str(result)

@app.route("/mul")
def mul_route():

    #get values through the query parameter and multiply to get the result
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = multiplication(num1, num2)
    return str(result)

@app.route("/")
def render_index_page():

    # displays the homepage
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
