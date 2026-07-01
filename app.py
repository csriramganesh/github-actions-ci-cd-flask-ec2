from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>GitHub Actions CI/CD Project</h1>
    <p>Flask app deployed automatically to EC2 using Docker and GitHub Actions.</p>
    <p>Version: v1</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
