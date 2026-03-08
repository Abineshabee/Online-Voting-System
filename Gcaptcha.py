

TrueC = "Valid Captcha : Congratulations! Your captcha has been successfully verified. You may proceed with the intended action."

FalseC = "Invalid Captcha: Sorry, the captcha you entered is invalid. Please try again with the correct characters to proceed."

import string
import random
from captcha.image import ImageCaptcha

def generate_captcha():
    # Define the characters to be used in the CAPTCHA
    characters = string.digits
    
    # Generate a random string of characters for the CAPTCHA
    captcha_text = ''.join(random.choices(characters, k=6))  # Change 6 to adjust the length of the CAPTCHA
    
    # Create an ImageCaptcha instance
    captcha = ImageCaptcha(width=200, height=60)  # Adjust width, height, and fonts for clearer image
    
    # Generate the CAPTCHA image
    captcha_image = captcha.generate(captcha_text)

    # Save the image to a file
    captcha_image_file = "static/images/captcha_image.png"  # Change the filename as needed
    captcha.write(captcha_text, captcha_image_file)

    return captcha_text
    

#generate_captcha();
