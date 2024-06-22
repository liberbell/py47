import configparser
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

try:
    config_ini = configparser.ConfigParser()
    config_ini.read('auth.ini', encoding='utf-8')

    endpoint = config_ini['DEFAULT']['Endpoint']
    subscription_key = config_ini['DEFAULT']['Auth_key']
except KeyError:
    print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
    exit()

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "img")
local_image_path = os.path.join (images_folder, "sample01.jpg")

def detect_objects(filepath):
    local_image = open(filepath, "rb")
    detect_objects = computervision_client.detect_objects_in_stream(local_image)

    return detect_objects

def get_tags(filepath):
    local_image = open(filepath, "rb")
    tags_result = computervision_client.tag_image_in_stream(local_image)
    tags = tags_result.tags

    tags_name = []
    for tag in tags:
        tags_name.append(tag.name)

    return tags_name