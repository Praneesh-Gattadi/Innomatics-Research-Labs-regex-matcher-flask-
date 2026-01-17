from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    matches = []
    error = None

    if request.method == "POST":
        test_string = request.form.get("test_string")
        regex_pattern = request.form.get("regex_pattern")

        try:
            pattern = re.compile(regex_pattern)
            matches = [(m.group(), m.start(), m.end()) for m in pattern.finditer(test_string)]
        except re.error as e:
            error = f"Invalid Regex: {e}"

    return render_template("index.html", matches=matches, error=error)

if __name__ == "__main__":
    app.run(debug=True)