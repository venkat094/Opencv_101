# To Run
# python load_image_opencv.py --input-image input_file_name.png --output-image output_file_name.png

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input-image", required=True,
	help="path to input image")
ap.add_argument("-o", "--output-image", required=True,
	help="path to output image")
args = vars(ap.parse_args())

# load the image from disk via "cv2.imread" and then grab the spatial
# dimensions, including width, height, and number of channels
image = cv2.imread(args["input-image"])
(h, w, c) = image.shape[:3]

# display the image width, height, and number of channels to our
# terminal
print("width: {} pixels".format(w))
print("height: {}  pixels".format(h))
print("channels: {}".format(c))

# show the image and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)

# save the image back to disk (OpenCV handles converting image
# filetypes automatically)
# cv2.imwrite("newimage.jpg", image)
cv2.imwrite(args["output-image"],image)