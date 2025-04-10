from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "hello Johnny"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/testing')
def hello():
    return jsonify({"message": "testing"})

if __name__ == '__main__':
    print("Starting microservice...")
    print("hello Johnny")
    app.run(host='0.0.0.0', port=5000, debug=True)
