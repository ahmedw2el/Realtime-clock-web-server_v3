from flask import Flask,render_template,request 
import time
app = Flask(__name__)

@app.route("/")
def anaSayfa():
    return render_template("index.html")


@app.route("/time", methods=['POST','GET'])
def hesapla():
    if request.method == 'POST':
        time_now = time.ctime()
        return str(time_now)
    else:
        return "Not Found"


if __name__ == "__main__":
    app.run(debug=True)
