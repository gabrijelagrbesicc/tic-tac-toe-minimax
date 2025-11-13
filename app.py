from flask import Flask, request, jsonify
from solution import ispisi, ima_pobjednika, puna, najbolji_potez

app = Flask(__name__)
ploca = [[" " for _ in range(3)] for _ in range(3)]

@app.route("/potez", methods=["POST"])
def potez():
    global ploca
    data = request.get_json()
    r, s = data["r"], data["s"]

    if ploca[r][s] != " ":
        return jsonify({"error": "Zauzeto!"}), 400
    ploca[r][s] = "X"

    if ima_pobjednika(ploca, "X"):
        return jsonify({"ploca": ploca, "rezultat": "pobjeda"})

    if puna(ploca):
        return jsonify({"ploca": ploca, "rezultat": "nerijeseno"})

    i, j = najbolji_potez(ploca)
    ploca[i][j] = "O"

    if ima_pobjednika(ploca, "O"):
        return jsonify({"ploca": ploca, "rezultat": "poraz"})

    if puna(ploca):
        return jsonify({"ploca": ploca, "rezultat": "nerijeseno"})

    return jsonify({"ploca": ploca, "rezultat": None})

@app.route("/reset", methods=["POST"])
def reset():
    global ploca
    ploca = [[" " for _ in range(3)] for _ in range(3)]
    return jsonify({"ploca": ploca})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

