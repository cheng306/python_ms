from flask import Flask, jsonify
import werkzeug

if not hasattr(werkzeug, "__version__"):
    werkzeug.__version__ = "3.0.0"

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "hello Johnny"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/testing')
def testing():
    return jsonify({"message": "testing"})


@app.route('/johnnycheng')
def johnnycheng():
    return jsonify({"message": "Hello Johnny Cheng"})

if __name__ == '__main__':
    print("Starting microservice...")
    print("hello Johnny")
    app.run(host='0.0.0.0', port=5000, debug=True)
