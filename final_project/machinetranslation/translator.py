# translator.py

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    #write the code here
    """
    Function translates english to french using ibm language translator
    """
    translation = language_translator.translate(
        englishText, model_id = 'en-fr'
    ).get_result()

    output = json.dumps(translation, indent = 2, ensure_ascii = False)
    data = json.loads(output)
    text = data['translations'][0]

    frenchText = text['translation']

    return frenchText


def frenchToEnglish(frenchText):
    #write the code here
    """
    Function translates french to english using ibm language translator
    """
    translation = language_translator.translate(
        frenchText, model_id = 'fr-en'
    ).get_result()

    output = json.dumps(translation, indent = 2, ensure_ascii = False)
    data = json.loads(output)
    text = data['translations'][0]

    englishText = text['translation']
    return englishText

# print(englishToFrench('Good morning my love'))
# print(frenchToEnglish('Bonjour mon amour'))
