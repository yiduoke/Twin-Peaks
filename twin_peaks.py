from flask import Flask, request, render_template_string
from single_peak import parse_profile, check_single_peaked

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Single-Peaked Preference Checker</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: auto; padding-top: 30px; }
        textarea { width: 100%; height: 150px; font-family: monospace; }
        input[type=submit] { padding: 10px 20px; margin-top: 10px; }
        .result { margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <h2>Check if a Profile is Single-Peaked</h2>
    <form method="post">
        <label for="profile">Enter preference profile (one vote per line, comma-separated):</label><br>
        <textarea name="profile" id="profile" placeholder="a,b,c\nb,c,a\nc,a,b">{{ request.form.get('profile', '') }}</textarea><br>
        <input type="submit" value="Check">
    </form>
    {% if result %}
    <div class="result">Result: {{ result }}</div>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        csv_text = request.form['profile']
        try:
            profile = parse_profile(csv_text)
            result = check_single_peaked(profile)
        except Exception as e:
            result = f"Error: {e}"
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
