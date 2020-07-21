# canny_edge_detection_openCV

## openCV

openCV is a library of programming functions mainly aimed at computer vision. It has many applications(motion detection, object detection, face recognition, edge detection etc.). It is mainly the best library to play with images. Here is the edge detction application.

###### installation

[openCV_installation](https://docs.opencv.org/master/d5/de5/tutorial_py_setup_in_windows.html)

**The Canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images**

###### GRAYSCALE CONVERSION

*RGB image are converted to gray because grayscale image consists only shades of gray on a bit size ranging from 0 to 255 which is less information for each pixel than the usual RGB image which makes it easier to process.*

***gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)***

###### GAUSSIAN FILTER

*Image blurring is achieved by convolving the image with a low-pass filter kernel. It is useful for removing noise. It actually removes high frequency content (eg: noise, edges) from the image. So edges are blurred a little bit in this operation. One of the method is **GaussianBlur function**. We should specify the width and height of the kernel which should be positive and odd. We also should specify the standard deviation in the X and Y directions, sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is taken as the same as sigmaX. If both are given as zeros, they are calculated from the kernel size. Gaussian blurring is highly effective in removing Gaussian noise from an image.*

***blur = cv.GaussianBlur(img,(5,5),0)***

###### DETERMINE THE INTENSITY GRADIENTS

*Smoothened image is then filtered with a Sobel kernel in both horizontal and vertical direction to get first derivative in horizontal direction ( Gx) and vertical direction ( Gy). From these two images, we can find edge gradient and direction for each pixel.*

***edge_gradient(G) = ((Gx)^2 + (Gy)^2)^1/2***

***Angle(θ) = tan−1(Gy/Gx)***

*Gradient direction is always perpendicular to edges. It is rounded to one of four angles representing vertical, horizontal and two diagonal directions(0°, 45°, 90° and 135°)*

###### NON MAXIMUM SUPPRESSION

*Non-maximum suppression is an **edge thinning** technique. 

*Non-maximum suppression is applied to find "the largest" edge. After applying gradient calculation, the edge extracted from the gradient value is still quite blurred. With respect to criterion 3, there should only be one accurate response to the edge. Thus non-maximum suppression can help to suppress all the gradient values (by setting them to 0) except the local maxima, which indicate locations with the sharpest change of intensity value.*

*Main points the algorithm does is*

**Compare the edge strength of the current pixel with the edge strength of the pixel in the positive and negative gradient directions.**

**If the edge strength of the current pixel is the largest compared to the other pixels in the mask with the same direction (e.g., a pixel that is pointing in the y-direction will be compared to the pixel above and below it in the vertical axis), the value will be preserved. Otherwise, the value will be suppressed.**

*In more accurate implementations, linear interpolation is used between the two neighbouring pixels that straddle the gradient direction. For example, if the gradient angle is between 89° and 180°, interpolation between gradients at the north and north east pixels will give one interpolated value, and interpolation between the south and south west pixels will give the other (using the conventions of the last paragraph). The gradient magnitude at the central pixel must be greater than both of these for it to be marked as an edge.*

###### DOUBLE THRESHOLD

*Result from non maximum suppression is not perfect, some edges may not actually be edges and there is some noise in the image.*

*Double threshold sets the high threshold and low threshold, if the edges fall to the high threshold region, it is taken as strong edge, if it is below low threshold, it is taken as no edge. Between the low threshold and high threshold, edges are taken as weak edge.  For example, we might choose the high threshold to be 0.7, this means that all pixels with a value larger than 0.7 will be a strong edge. You might also choose a low threshold of 0.3, this means that all pixels less than it is not an edge and you would set it to 0. The values in between 0.3 and 0.7 would be weak edges, in other words, we do not know if these are actual edges or not edges at all.

**This threshold is different for every image so we have to set according to our own observation**

###### EDGE TRACKING BY HYSTERISIS

*The weak edges stated by double thresholding is actually determined here, if that weak edge is an actual edge or not.*

**Weak edges that are connected to strong edges will be actual/real edges. Weak edges that are not connected to strong edges will be removed.**

*So, this way with Edge Tracking algorithm and Double Thresholding technique, we are able to determine these weak edges.*

*This stage also removes small pixels noises on the assumption that edges are long lines.*

**cv2.Canny(frame, min_threshold, max_threshold)** *The first argument is the input image, second and third argument is the minimum threshold value and the maximum threshold value*
