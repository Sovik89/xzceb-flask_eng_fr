#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-08-03',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text=None):
    """
    English Text to French
    """
    if english_text is None:
        return None
    resultant_text= language_translator.translate(text=english_text,
    model_id='en-fr').get_result()
    french_text=resultant_text["translations"][0].get("translation")
    
    return french_text


def french_to_english(french_text=None):
    """
    French to English
    """
    if french_text is None:
        return None
    resultant_text= language_translator.translate(text=french_text,
    model_id='fr-en').get_result()
    english_text=resultant_text["translations"][0].get("translation")
    return english_text







