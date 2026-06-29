import cv2
import os

image_path = "C:/Users/AsaGity/Downloads/pythonphoto.jpg"

print(f"is loading: {image_path}")

if not os.path.exists(image_path):
    print(f" Error ")
    print("File located is analized :", image_path)
    exit()

img = cv2.imread(image_path)

if img is None:
    print(" Unreadable!")
    print("may not be supported.")
    exit()

print(f" successfully uploaded!")
print(f"Dimensions: {img.shape[1]} x {img.shape[0]} ")

gray_image = None
is_gray = False

cv2.imshow("Image processing - look at the console for commands", img)

print("\n" + "="*50)
print("Commands (activate the image in the window and press the keys):")
print("   [g] → (Grayscale)")
print("   [s] → save image gray.jpeg")
print("   [ESC] یا [q] → Exit")
print("="*50)

while True:
    key = cv2.waitKey(0) & 0xFF
    
    if key == ord('g'):
        if not is_gray:
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Image path - look at the console for commands", gray_image)
            is_gray = True
            print(" The image has been converted to Grayscale! Now press [s] to save.")
        else:
            print(" The image is already Grayscale.")
    
    elif key == ord('s'):
        if is_gray and gray_image is not None:
            cv2.imwrite("gray.jpeg", gray_image)
            full_path = os.path.abspath("gray.jpeg")
            print(f"Saved: {full_path}")
        else:
            print(" First press the [g] key to turn the image gray!")
    
    elif key == 27 or key == ord('q'):  
        print("|| Exit ||")
        break

cv2.destroyAllWindows()
