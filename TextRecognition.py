# Assumes clearly written text
# Assumes good lighting
# Assumes correct rotation
# Assumes English

# C:\Users\Enkimesh\AppData\Local\Tesseract-OCR
# ImageMagick-6.9.3-1-Q16-x64-dll.exe
# C:\Program Files\ImageMagick-7.0.6-Q16

#from PIL import Image
#import pytesseract
#import cv2
#import numpy

#src_path = "resources/"

#def get_string(img_path):
#    img = cv2.imread(img_path)

#from wand.image import Image
from PIL import Image as PI
import pyocr.builders


class TextRecognition:
    def __init__(self):
        self.tool = pyocr.get_available_tools()[0]
        self.lang = self.tool.get_available_languages()[0]

    def set_language(self, lang):
        for tool_lang in self.tool.get_available_languages():
            if tool_lang == lang:
                self.lang = tool_lang
                return
        print("error: language '{}' not listed.  Defaulting to '{}'.".format(lang, self.lang))
        print("language options: {}".format(self.tool.get_available_languages()))

    def recognize_file(self, file):
        txt = self.tool.image_to_string(
            PI.open(file),
            lang=self.lang,
            builder=pyocr.builders.TextBuilder()
        )
        return txt

tr = TextRecognition()
tr.set_language('spa')
print(tr.recognize_file('resources/single_line_text.jpg'))
