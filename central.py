
from flask import Flask, render_template
 
app = Flask(__name__)
 
 
@app.route("/")
def p1():
    return render_template("page1.html")

@app.route("/2")
def p2():
    return render_template("page2.html")

@app.route("/3")
def p3():
    return render_template("page3.html")

@app.route("/4")
def p4():
    return render_template("page4.html")
 
@app.route("/5")
def p5():
    return render_template("page5.html")

@app.route("/7")
def p7():
    return render_template("page7.html")

@app.route("/8")
def p8():
    return render_template("page8.html")
    
if __name__ == "__main__":
    app.run()