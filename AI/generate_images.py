import json
import random
from PIL import Image, ImageDraw, ImageFont
import os
# load vocab.json into vocab_data
with open('vocab.json') as fin:
    vocab_data = json.load(fin)

fonts = ['fonts/CookieRunRegular.ttf']

for category in vocab_data:
    for word in vocab_data[category]:
        korean_word = word["Korean"]
        os.mkdir(f'images/{korean_word}')

        if(len(korean_word) == 1):
            font_size = 190
            y_pos = 20
        elif(len(korean_word) == 2):
            font_size = 120
            y_pos = 50
        elif(len(korean_word) == 3):
            font_size = 90
            y_pos = 70
        elif(len(korean_word) == 4):
            font_size = 50
            y_pos = 70
        elif(len(korean_word) == 5):
            font_size = 55
            y_pos = 95
        else:
            font_size = 45
            y_pos = 100
        
        for font in fonts: 
            #create image of korean word using fonts
            image = Image.new('RGB', (256, 256), "white")
            draw = ImageDraw.Draw(image)
            custom_font = ImageFont.truetype(font, font_size)
            draw.text((10, y_pos), korean_word, fill="black", font=custom_font)
            image.save(f'images/{korean_word}/{korean_word}.png')