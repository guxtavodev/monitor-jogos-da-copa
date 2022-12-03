import requests
from datetime import datetime
from time import sleep

@app.route("/api/v1/nrt", methods=["GET"])
def narracao():
  		print(joguin())
		if joguin()[0] == "None":
			return jsonify({
			"att": "No"
		})
		else:
			return jsonify({
			"moment": joguin()[0],
			"text": joguin()[1]
			})

def get_match_data():
	return requests.get(
		url="https://temporeal.lance.com.br/storage/matches/copa-do-mundo-2022-28-11-2022-brasilxsuica.json"
	).json()

last_update = None

while True:
	match_data = get_match_data()
	narrations = match_data["match"]["narrations"]
	last_narration = narrations[len(narrations)-1]
	last_narration_time = datetime.strptime(last_narration["created_at"], "%Y-%m-%dT%H:%M:%S.000000Z")

	if (not last_update) or (last_narration_time > last_update):
		last_update = last_narration_time
		last_narration_moment = narrations[len(narrations)-1]["moment"]
		last_narration_text = narrations[len(narrations)-1]["text"]
		print(f".\n {last_narration_moment}' - {last_narration_text}")

sleep(30) 
