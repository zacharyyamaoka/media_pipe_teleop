from flask import Flask, render_template

app = Flask(__name__)
ip = "127.0.0.1"
ip = "192.168.0.61"

# if app.debug == True:
#     print("DEVELOPMENT IP IN USE")
#     ip = "192.168.0.90"
# else:
#     ip = "50.68.110.225"

@app.route("/hello-world")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template('teleop.html', ip=ip)
   
if __name__ == '__main__':
    app.run()