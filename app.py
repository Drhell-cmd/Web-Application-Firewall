from flask import Flask, request, render_template
from markupsafe import escape
from waf import waf_filter  # Your custom filtering logic
import datetime

app = Flask(__name__)

def generate_block_message(payload):
    return f"""🛑 <b>Threat Neutralized!</b><br>
🚷 <code>{escape(payload)}</code><br>
🧠 Detected & blocked by Cyber Sentinel AI Defense Grid<br>
🕒 Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br>
🔍 Threat Type: Malicious Input Pattern<br>
📂 Logged for forensic analysis...
"""

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()

        if not user_input:
            response = "⚠️ Input cannot be empty! Submit a threat string."
        elif waf_filter(user_input):
            response = generate_block_message(user_input)
        else:
            safe_input = escape(user_input)
            response = f"✅ Input received and passed WAF scan: <code>{safe_input}</code>"

    return render_template("index.html", result=response)

if __name__ == "__main__":
    app.run(debug=True)
