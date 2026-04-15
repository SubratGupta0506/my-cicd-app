from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})

# API: Add two numbers
@app.route("/add", methods=["GET"])
def add():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({
            "operation": "addition",
            "a": a,
            "b": b,
            "result": a + b
        })
    except Exception:
        return jsonify({"error": "Invalid input"}), 400

# API: Multiply numbers
@app.route("/multiply", methods=["GET"])
def multiply():
    try:
        a = int(request.args.get("a", 1))
        b = int(request.args.get("b", 1))
        return jsonify({
            "operation": "multiplication",
            "result": a * b
        })
    except Exception:
        return jsonify({"error": "Invalid input"}), 400


if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))