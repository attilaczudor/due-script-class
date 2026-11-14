from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/uzenet", methods=["GET"])
def uzenet():
    return jsonify({"uzenet": "ok", "statusz": "Szerver elérhető"})

if __name__ == "__main__":
    app.run(port=5000)
