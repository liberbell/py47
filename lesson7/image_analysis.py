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
    # print(endpoint, key)
except KeyError:
    print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
    print("Set them before running this sample.")
    exit()

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")
remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"

print("===== Tag an image - remote =====")
# Call API with remote image
tags_result_remote = computervision_client.tag_image(remote_image_url)

remote_image_features = ["categories"]
categorize_results_remote = computervision_client.analyze_image(remote_image_url, remote_image_features)

detect_objects_result_remote = computervision_client.detect_objects(remote_image_url)

# Print results with confidence score
print("Tags in the remote image: ")
if (len(tags_result_remote.tags) == 0):
    print("No tags detected.")
else:
    for tag in tags_result_remote.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
print()

print("Detect categories in the remote image: ")
if (len(categorize_results_remote.categories) == 0):
    print("No categories detected.")
else:
    for category in categorize_results_remote.categories:
        print("'{}' with confidence {:.2f}%".format(category.name, category.score * 100))

print("Detect objects in the remote image: ")
if (len(detect_objects_result_remote.objects) == 0):
    print("No object detected.")
else:
    for object in detect_objects_result_remote.objects:
        print("object location {} {} {} {}".format( \
            object.rectangle.x, object.rectangle.x + object.rectangle.w, \
            object.rectangle.y, object.rectangle.y + object.rectangle.h
        ))

print("End of Computer Vision quickstart.")