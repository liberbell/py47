import configparser
import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

url = "https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png"

try:
    config_ini = configparser.ConfigParser()
    config_ini.read('auth.ini', encoding='utf-8')

    endpoint = config_ini['DEFAULT']['Endpoint']
    key = config_ini['DEFAULT']['Auth_key']
    print(endpoint, key)
except KeyError:
    print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
    print("Set them before running this sample.")
    exit()

client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

result = client.analyze_from_url(
    image_url=url,
    visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ],
    gender_neutral_caption=True,
)

# print(" Caption:")
# if result.caption is not None:
#     print(f"   '{result.caption.text}', Confidence {result.caption.confidence:.4f}")

# print(" Read:")
# if result.read is not None:
#     for line in result.read.blocks[0].lines:
#         print(f"   Line: '{line.text}', Bounding box {line.bounding_polygon}")
#         for word in line.words:
#             print(f"     Word: '{word.text}', Bounding polygon {word.bounding_polygon}, Confidence {word.confidence:.4f}")