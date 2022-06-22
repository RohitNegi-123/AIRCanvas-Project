# AIRCanvas-Project : 

We will see the working of this computer vision project in four major points :

Understanding the HSV (Hue, Saturation, Value) color space for Color Tracking. And tracking the small colored object at finger tip.
Detecting the Position of Colored object at finger top and forming a circle over it. That is Contour Detection.
Tracking the fingertip and drawing points at each position for air canvas effect. That is Frame Processing.
Fixing the Minor Details of the code to function the program smoothly. Algorithmic Optimization.

Algorithm: 
 

Start reading the frames and convert the captured frames to HSV color space (Easy for color detection). 
 
Prepare the canvas frame and put the respective ink buttons on it. 
 
Adjust the track bar values for finding the mask of the colored marker. 
 
Preprocess the mask with morphological operations (Eroding and dilation). 
 
Detect the contours, find the center coordinates of largest contour and keep storing them in the array for successive frames (Arrays for drawing points on canvas). 
 
Finally draw the points stored in an array on the frames and canvas.
![HElloIIITM](https://user-images.githubusercontent.com/77240570/174952971-424ab7e1-b4ac-4691-8e58-6c5213e91cb3.png)


![hi](https://user-images.githubusercontent.com/77240570/174952886-af0d033f-e28d-4c09-b5b5-d109db465674.png)
