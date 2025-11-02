
import cv2
import matplotlib.pyplot as plt
import os

# Check if image exists
image_path = 'rrr.jpg'
if not os.path.exists(image_path):
    print(f"Error: Image file '{image_path}' not found")
    print(f"Current working directory: {os.getcwd()}")
    exit()

# Load the pre-trained face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read image with error checking
img = cv2.imread(image_path)
if img is None:
    print(f"Error: Could not load image '{image_path}'")
    print("Make sure the image is a valid JPG file")
    exit()

# Print image information
print(f"Successfully loaded image with shape: {img.shape}")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,  # Reduced for better detection
    minNeighbors=4,   # Reduced for better detection
    minSize=(30, 30)
)

print(f"Found {len(faces)} faces!")

# Convert BGR to RGB for matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img_rgb, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display result
plt.figure(figsize=(12, 8))
plt.imshow(img_rgb)
plt.axis('off')
plt.show()