import os
from PIL import Image
import pytesseract
from art import text2art
from colorama import init, Fore, Style

# Initialize colorama
init()

# Print welcome message
if __name__ == "__main__":
    print(Fore.RED + text2art("OCR") + Style.RESET_ALL)
    print(Fore.GREEN + "OCR, optical character recognition, extract text from images" + Style.RESET_ALL)
    print(Fore.GREEN + "By: Mbale Prince aka eViL bRaTt" + Style.RESET_ALL + "\n")

    # Create output directory if it doesn't exist
    output_folder = 'output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through images in the input folder
    input_folder = 'input'
    for idx, filename in enumerate(os.listdir(input_folder)):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # Construct full file path
            image_path = os.path.join(input_folder, filename)
            # Open the image using Pillow
            img = Image.open(image_path)
            # Use pytesseract to extract text
            extracted_text = pytesseract.image_to_string(img)
            # Save the extracted text to a .txt file
            with open(os.path.join(output_folder, f"{idx + 1}.txt"), "w") as text_file:
                text_file.write(extracted_text)
            print(Fore.GREEN + f"Processed: {filename} -> {idx + 1}.txt" + Style.RESET_ALL)