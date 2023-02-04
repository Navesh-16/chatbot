from flask import Flask, render_template, request, jsonify
import long_responses as long

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("navesh.html")

@app.route("/get", methods=['POST'])
def get_bot_response():
    user_text = request.get_json()['msg']
    bot = long.get_response(user_text)
    return jsonify(response=bot)

if __name__ == '__main__':
    app.run(debug=Flase,host='0.0.0.0')
