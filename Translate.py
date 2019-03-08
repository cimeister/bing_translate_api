# -*- coding: utf-8 -*-

# This simple app uses the '/translate' resource to translate text from
# one language to another.

# This sample runs on Python 2.7.x and Python 3.x.
# You may need to install requests and uuid.
# Run: pip install requests uuid

import os, requests, uuid, json
import argparse

def translate(api_key, text, language_from, language_to):
	# If you encounter any issues with the base_url or path, make sure
	# that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-translate
	base_url = 'https://api.cognitive.microsofttranslator.com'
	path = '/translate?api-version=3.0'
	params = '&language='+ language_from +'&to=' + language_to
	constructed_url = base_url + path + params

	headers = {
	    'Ocp-Apim-Subscription-Key': api_key,
	    'Content-type': 'application/json',
	    'X-ClientTraceId': str(uuid.uuid4())
	}
	if type(text) is str:
		text = [text]

	body = [{'text': x} for x in text]
	# You can pass more than one object in body.
	
	request = requests.post(constructed_url, headers=headers, json=body)
	response = request.json()

	return [i["translations"][0]["text"] for i in response]


if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	    ## Required parameters
	parser.add_argument("--api_key",
	                        default=None,
	                        type=str,
	                        required=True,
	                        help="Api key for Microsoft azure translation service")

	parser.add_argument("--language_from",
						default='en',
						type=str,
						help="Check here for language code options https://docs.microsoft.com/en-us/azure/cognitive-services/translator/language-support")
	parser.add_argument("--language_to",
						default=None,
						type=str,
						required=True,
						help="Check here for language code options https://docs.microsoft.com/en-us/azure/cognitive-services/translator/language-support")

	args = parser.parse_args()
	while True:
		sen = input("Enter sentence to translate: ")
		translation = translate(args.api_key,sen, args.language_from, args.language_to)
		for i in translation:
			print(i)


