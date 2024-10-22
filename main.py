from flask import Flask, request, render_template_string, jsonify
import random
import string

app = Flask(__name__)

# Global variable to store the server status
is_server_running = False

# HTML Template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Steven X shayan❤️</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background-image: url('https://iili.io/2K2zDZb.jpg');
      background-size: cover;
      color: white;
      position: relative;
      overflow-y: auto;
      height: 100vh;
    }
    .container {
      max-width: 300px;
      background-color: rgba(255, 255, 255, 0.8);
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
      margin: 0 auto;
      margin-top: 20px;
      position: relative;
      z-index: 1;
      border: 2px solid blue;
    }
    .header {
      text-align: center;
      padding-bottom: 10px;
    }
    .btn-submit, .btn-stop {
      width: 100%;
      margin-top: 10px;
    }
    .footer {
      text-align: center;
      margin-top: 10px;
      color: blue;
    }
    .key-display {
      display: none;
      margin-top: 10px;
      text-align: center;
    }
  </style>
</head>
<body>
  
  <div class="header mt-4">
    <h1 class="mb-3">Convo/Inbox Loader Tool</h1>
  </div>

  <div class="container">
    <form id="mainForm">
      <div class="mb-3">
        <label for="tokenType">Select Token Type:</label>
        <select class="form-control" id="tokenType" name="tokenType" required>
          <option value="single">Single Token</option>
          <option value="multi">Multi Token</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="accessToken">Enter Your Token:</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken" required>
      </div>
      <div class="mb-3">
        <label for="threadId">Enter Convo/Inbox ID:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">Enter Hater Name:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">Select Your Notepad File:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3" id="multiTokenFile" style="display: none;">
        <label for="tokenFile">Select Token File (for multi-token):</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile" accept=".txt">
      </div>
      <div class="mb-3">
        <label for="time">Speed in Seconds:</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Start Server</button>
      <button type="button" class="btn btn-danger btn-stop" id="stopButton" style="display:none;">Stop Server</button>
    </form>

    <div class="key-display" id="keyDisplay">
      <p>Your server start key: <span id="serverKey"></span></p>
    </div>
  </div>
  
  <footer class="footer">
    <p>&copy; Developed by  2024. All Rights Reserved.</p>
    <p>Keep enjoying!</p>
  </footer>

  <script>
    document.getElementById('mainForm').addEventListener('submit', function(event) {
      event.preventDefault();
      fetch('/start_server', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({}) // Send empty body
      }).then(response => response.json()).then(data => {
        if (data.status === "started") {
          document.getElementById('serverKey').textContent = data.key;
          document.getElementById('keyDisplay').style.display = 'block';
          document.getElementById('stopButton').style.display = 'block';
        } else {
          alert("Server is already running.");
        }
      });
    });

    document.getElementById('stopButton').addEventListener('click', function() {
      fetch('/stop_server', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({})
      }).then(response => response.json()).then(data => {
        if (data.status === "stopped") {
          alert("Server stopped successfully.");
          document.getElementById('serverKey').textContent = '';
          document.getElementById('keyDisplay').style.display = 'none';
          document.getElementById('stopButton').style.display = 'none';
        } else {
          alert("Server is not running.");
        }
      });
    });

    document.getElementById('tokenType').addEventListener('change', function() {
      var tokenType = this.value;
      document.getElementById('multiTokenFile').style.display = tokenType === 'multi' ? 'block' : 'none';
    });
  </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/start_server', methods=['POST'])
def start_server():
    global is_server_running
    if not is_server_running:
        is_server_running = True
        server_key = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        return jsonify({"status": "started", "key": server_key}), 200
    return jsonify({"status": "already running"}), 400

@app.route('/stop_server', methods=['POST'])
def stop_server():
    global is_server_running
    if is_server_running:
        is_server_running = False
        return jsonify({"status": "stopped"}), 200
    return jsonify({"status": "not running"}), 400

if __name__ == '__main__':
    app.run(debug=True)
