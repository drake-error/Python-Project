# from skimage import data
# from skimage.feature import Cascade
# import matplotlib.pyplot as plt

# # load the trained file from the module
# trained_file = data.lbp_frontal_face_cascade_filename()

# # initialize the detector Cascade
# detector = Cascade(trained_file)

# # read the image
# rrr = plt.imread('rrr.png')

# # detect the faces in the image
# detected = detector.detect_multi_scale(
#     img=rrr,
#     scale_factor=1.2,
#     step_ratio=1,
#     min_size=(20,20),
#     max_size=(200,200)
# )

# # define show_detected_faces function
# def show_detected_faces(img, detected):
#     plt.imshow(img)
#     for x, y, width, height in detected:
#         plt.rectangle((x, y), width, height, fill=False, color='r')
#     plt.show()

# # show results    
# show_detected_faces(rrr, detected)

# import cv2
# import matplotlib.pyplot as plt

# # Load the pre-trained face cascade classifier
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # Read image
# img = cv2.imread('rrr.jpg')  # Make sure you have rrr.jpg in the same folder

# # Convert to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Detect faces
# faces = face_cascade.detectMultiScale(
#     gray,
#     scaleFactor=1.2,
#     minNeighbors=5,
#     minSize=(20, 20)
# )

# # Convert BGR to RGB for matplotlib
# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# # Draw rectangles around faces
# for (x, y, w, h) in faces:
#     cv2.rectangle(img_rgb, (x, y), (x+w, y+h), (255, 0, 0), 2)

# # Display result
# plt.figure(figsize=(12, 8))
# plt.imshow(img_rgb)
# plt.axis('off')
# plt.show()

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