import argparse
import dlib
import cv2

# Use argparse so we can send the image path from the command line
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",
    help="Image to input image to detect faces")
args = vars(ap.parse_args())
f = args['image']

# 2. Get the dlib frontal face detector
detector = dlib.get_frontal_face_detector()

print("Processing file: {}".format(f))

# 3. Load the image using OpenCV
img = cv2.imread(f)

# 4. Pass de loaded image to the `detector`
dets = detector(img, 1)
print("Number of faces detected: {}".format(len(dets)))

# 5. Iterate over the found faces and draw a rectangle in the original image.
for i, d in enumerate(dets):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        i, d.left(), d.top(), d.right(), d.bottom()))
    cv2.rectangle(img, (d.left(), d.top()), (d.right(), d.bottom()),
                (0, 0, 255), 2)

# 6. Show image with detected faces
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()