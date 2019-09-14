#to run need to configure and install GCP Cloud SDK tools:
#https://cloud.google.com/translate/docs/quickstart
#pip install --upgrade google-cloud-translate

from google.cloud import translate

def change_lang(phrase, language):

	client = translate.Client(target_language = language)
	new_word = client.translate(phrase, source_language = 'en')

	return new_word["translatedText"]