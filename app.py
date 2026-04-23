from flask import Flask, render_template, request
from logic.scoring import calculate_productivity

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    message = ""

    if request.method == "POST":
        try:
            sleep = float(request.form["sleep"])
            work = float(request.form["work"])
            focus = int(request.form["focus"])

            # Validation
            if sleep < 0 or work < 0:
                message = "Sleep and work hours cannot be negative."
            elif sleep > 24 or work > 24:
                message = "Sleep/Work hours cannot exceed 24."
            elif focus < 1 or focus > 10:
                message = "Focus level must be between 1 and 10."
            else:
                score = calculate_productivity(sleep, work, focus)

        except ValueError:
            message = "Invalid input. Please enter valid numbers."

    return render_template("home.html", score=score, message=message)


if __name__ == "__main__":
    app.run()