from flask import Flask
import socket

app = Flask(__name__)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

@app.route('/')
def hello_cloud():
    return 'Welcome to Siddharth's Final Test API Server!'

@app.route('/host')
def host_name():
    return hostname

@app.route('/ip')
def host_ip():
    return ip_address

@app.route('/health')
def health():
    return 'Healthy', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
