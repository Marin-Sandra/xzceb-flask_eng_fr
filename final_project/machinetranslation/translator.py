"""import json"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(englishText):
    """ english to french """
    ftranslation = language_translator.translate(englishText,model_id='en-fr').get_result()
    frenchText = ftranslation['translations'][0]['translation']
    return frenchText

def french_to_english(frenchText):
    """ french to english """
    etranslation = language_translator.translate(frenchText,model_id='fr-en').get_result()
    englishText = etranslation['translations'][0]['translation']
    return englishText
