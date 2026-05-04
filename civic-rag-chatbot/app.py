from flask import Flask, render_template, request, jsonify
from rag.pipeline import run_pipeline

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message", "")

        if not user_input.strip():
            return jsonify({"response": "Please enter a valid message."})

        response = run_pipeline(user_input)

        if not response:
            response = "I couldn’t generate a response. Please try again."

        return jsonify({"response": response})

    except Exception as e:
        print("ERROR:", e)

        return jsonify({
            "response": "⚠️ Sorry, I’m having trouble processing your request right now. Please try again in a moment."
        })

if __name__ == "__main__":
    app.run(debug=True)