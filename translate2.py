#to run need to configure and install GCP Cloud SDK tools:
#https://cloud.google.com/translate/docs/quickstart
#jank command line version be careful

import subprocess

word_in = "phone"

def translate(phrase, language):
	cmd = [""]
	output = subprocess.Popen("""
		curl -s -X POST -H "Content-Type: application/json"  -H "Authorization: Bearer "$(gcloud auth application-default print-access-token)  --data "{'q': """ + "'" + phrase + "'" + """, 'source': 'en', 'target': """ + "'" + language + "'" + """, 'format': 'text'}" "https://translation.googleapis.com/language/translate/v2" """, stdout=subprocess.PIPE, shell=True ).communicate()[0]
	return output

new_word = translate(word_in, "es")
temp = new_word[71:]
count = 0
for i in new_word:
	count += 1
	if i == "\"":
		break

print temp[:count]