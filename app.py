from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from my CI/CD app! 🚀"

# ─────────────────────────────
# This block only runs locally
# NOT during testing
# ─────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)