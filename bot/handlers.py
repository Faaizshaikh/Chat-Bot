from slack_client import ephemeral_response, public_response, post_message
from deployer import Deployer
import os


D = Deployer()
DEFAULT_CHANNEL = os.environ.get('SLACK_DEFAULT_CHANNEL', None)




def handle_command(command, text, user_id):
cmd = command.strip().lower()
# slash commands come as '/deploy', '/status', etc. remove leading '/'
if cmd.startswith('/'):
cmd = cmd[1:]


if cmd == 'deploy':
# trigger deploy in background (here we respond immediately)
deploy_user = f'<@{user_id}>'
# Option: notify in channel then run
if DEFAULT_CHANNEL:
post_message(DEFAULT_CHANNEL, f":rocket: {deploy_user} requested deploy. Starting...")
result = D.deploy(branch=(text.strip() or 'main'))
return public_response(f"Deploy started: {result}")


if cmd == 'status':
status = D.status()
return ephemeral_response(None, user_id, f"App status: {status}")


if cmd == 'logs':
logs = D.logs()
# For long logs, consider returning a gist or uploading file — placeholder below.
return ephemeral_response(None, user_id, f"Recent logs:\n```
{logs[:1500]}
```")


if cmd == 'restart':
res = D.restart()
return public_response(f"Restart requested: {res}")


return ephemeral_response(None, user_id, "Unknown command")
