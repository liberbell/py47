import configparser
import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

try:
    config_ini = configparser.ConfigParser()
    config_ini.read('auth.ini', encoding='utf-8')

    endpoint = config_ini['DEFAULT']['Endpoint']
    key = config_ini['DEFAULT']['Auth_key']
except KeyError:
    print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
    print("Set them before running this sample.")
    exit()

client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)