from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Pipeline</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f6f9; }
            h1 { color: #232f3e; }
            .status { color: #46a758; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>🚀 DevOps CI/CD Pipeline Operational (Python)!</h1>
        <p>Application successfully running on AWS EC2 inside a Docker container.</p>
        <p class="status">Pipeline Status: SUCCESS</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    # Listening on port 8080
    app.run(host='0.0.0.0', port=8080)