from flask import Flask, render_template, request

app = Flask(__name__)

def get_response(user_input):
    user_input = user_input.lower()

    if "course" in user_input:
        return "You can explore AI, Data Science, or Web Development based on your interest."
    elif "career" in user_input:
        return "You can pursue careers in Software Development, AI/ML Engineering, or Cloud Computing."
    elif "internship" in user_input:
        return "Start building projects, practice DSA, and apply through LinkedIn and company portals."
    else:
        return "Please ask about courses, career, or internships."

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = get_response(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)