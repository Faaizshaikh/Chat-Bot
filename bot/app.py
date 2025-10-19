from flask import Flask, request, jsonify, abort
import os
import hmac
import hashlib
import time
from dotenv import load_dotenv
from handlers import handle_command


load_dotenv()


app = Flask(__name__)
SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET')


# Slack request verification


def verify_slack_request(req):
timestamp = req.headers.get('X-Slack-Request-Timestamp')
if not timestamp:
return False
# protect against replay attacks (5 minutes)
if abs(time.time() - int(timestamp)) > 60 * 5:
return False
sig_basestring = f"v0:{timestamp}:{req.get_data(as_text=True)}"
my_sig = 'v0=' + hmac.new(
SLACK_SIGNING_SECRET.encode(),
sig_basestring.encode(),
hashlib.sha256
).hexdigest()
slack_signature = req.headers.get('X-Slack-Signature')
return hmac.compare_digest(my_sig, slack_signature)




@app.route('/slack/commands', methods=['POST'])
def slack_commands():
if not verify_slack_request(request):
abort(400, 'Invalid request signature')
form = request.form
command = form.get('command')
text = form.get('text') or ''
user_id = form.get('user_id')
response = handle_command(command, text, user_id)
# immediate response to Slack
return jsonify(response)




if __name__ == '__main__':
app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
