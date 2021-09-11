import cv2
from google.colab.patches import cv2_imshow

def get_image_with_bb(path, xmin, ymin, xmax, ymax):

  """
  path: image path
  xmin: top most x value for the bb
  ymin: top most y value for the bb
  xmax: bottom most x value for the bb
  ymax: bottom most y value for the bb
    
  """
  image2 = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
  start_point = (xmin, ymin) 
  end_point = (xmax, ymax) 
  
  # Blue color in BGR 
  color = (255, 0, 0) 
  
  # Line thickness of 2 px 
  thickness = 2
  
  # Using cv2.rectangle() method 
  # Draw a rectangle with blue line borders of thickness of 2 px 
  image2 = cv2.rectangle(image2, start_point, end_point, color, thickness) 
  

  cv2_imshow(image2)

