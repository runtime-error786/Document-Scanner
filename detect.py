import cv2
import pytesseract
from pytesseract import Output

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    edged = cv2.Canny(blurred, 75, 200)
    
    return edged, img

def extract_text_from_image(image_path):
    edged, img = preprocess_image(image_path)
    
    text = pytesseract.image_to_string(edged, output_type=Output.STRING)
    return text

def save_text_to_file(text, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        print(f"Text saved to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving the text: {e}")

if __name__ == "__main__":
    image_path = r'C:\Users\musta\OneDrive\Desktop\Document Scanner\img1.png'  
    
    text_file_path = 'extracted_text.txt' 

    text = extract_text_from_image(image_path)

    print("Extracted Text:")
    print(text)

    save_text_to_file(text, text_file_path)
