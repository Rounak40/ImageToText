#Import all required modules
import sys
import os.path
try:
    from PIL import Image #Python 3 (pip install Pillow)
except ImportError:
    import Image #Python 2.7 (pip install Pillow)
  
import pytesseract #(pip install pytesseract)
#Set directory for Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'

#Load the image
def load_image(filename):
    if os.path.exists(filename):
        image = Image.open(filename)
        return image
    else:
        return False

#Grab text from the image by pytesseract
def grab_text(image_file):
    text = pytesseract.image_to_string(image_file)
    return text

#save the text in a text file
def save_text(filename, data):
    f = open(f"text_{filename}.txt","w+")
    f.write(data)
    f.close()
    

#Run the process
if __name__ == "__main__":
    filename = input("Please enter the file name: (Make sure its present in current directory)\n")
    image = load_image(filename)
    if image == False:
        print("File not exist in current directory!")
    else:
        data = grab_text(image)
        save_text(filename, data)
        print(f"Process Done & text has been saved in text file text_{filename}.txt")
