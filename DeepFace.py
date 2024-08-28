1. Setting Up the Environment
You’ll need to install some essential libraries:
pip install deepface
pip install opencv-python

2. Importing Required Libraries

from deepface import DeepFace
import cv2
img_path = "path_to_image.jpg"
image = cv2.imread(img_path)

3. Loading and Preprocessing the Image
You can use OpenCV to load and preprocess images:
# Convert the image to RGB (if needed)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

4. Facial Recognition with DeepFace
Using the DeepFace library to recognize faces:
# Analyze the image to find the facial attributes and embeddings
analysis = DeepFace.analyze(image_rgb, actions=['age', 'gender', 'emotion', 'race'])

# Display the results
print("Facial Attributes: ", analysis)

5. Face Verification
To verify if two images are of the same person:
img1_path = "path_to_first_image.jpg"
img2_path = "path_to_second_image.jpg"

result = DeepFace.verify(img1_path, img2_path)

if result["verified"]:
    print("The faces are of the same person.")
else:
    print("The faces are of different people.")

6. Face Recognition
To recognize a face against a database of known faces:
# Assuming you have a database of faces

db_path = "path_to_your_database/"
image_to_recognize = "path_to_image_to_recognize.jpg"

result = DeepFace.find(img_path=image_to_recognize, db_path=db_path)
print("Found faces: ", result)

