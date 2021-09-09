#generates a file, with the id of the flight as a title
# image_path, ratio of the object with respect to image size (area of obj / area of image) *100, 
# class of the object, width and height of the image, all after resizing
nb_frames = test_flight.num_frames
image_area =  (2448/4)*(2048/4)
frames_keys = []
bbs = []
file1 = open(test_flight.id+".txt", "a") 
for i in range(0,nb_frames):
  frames_keys = []
  bbs = []
  frame_objects = []
  key = choice(list(test_flight.frames.keys()))
  test_frame = test_flight.get_frame(key)

  if test_frame.num_detected_objects == 0:
    continue
  frames_keys.append(key)
  test_frame_img = test_frame.image()
  airborne_objects = test_flight.detected_objects
  # print(test_frame.num_detected_objects)
  for obj in airborne_objects:
    
    if obj in test_frame.detected_object_locations:
      # print(obj)
      frame_objects.append(obj)
      # print("The distance is" ,test_frame.detected_object_locations[obj].range_distance_m)
      # print("The bbox is",test_frame.detected_object_locations[obj].bb)
      bb = test_frame.detected_object_locations[obj].bb
      # print(bb)
      bbs.append(bb)

  #  writing XML file for each frame
  img_path = test_frame.image_path()
  path = "/content/airborne-detection-starter-kit/data/part1/"
  
  # print(path+ img_path)
  image = cv2.imread(path + img_path, cv2.IMREAD_GRAYSCALE)
  # print(image.shape)
  height = image.shape[0]
  width = image.shape[1]

  dst = cv2.resize(image, (int(width/4), int(height/4)))

  print(dst.shape)
  # cv2_imshow(dst)
  img_name = (os.path.splitext(test_frame.image_path())[0]).rsplit('/', 1)[-1]
  path = '/content/airborne-detection-starter-kit/data/images_xml'

# To implement a foor loop, itterates over all objects and append them to the XML file
  count = 0
  for obj in frame_objects:
    xmin = (bbs[count].left)/4
    ymin = (bbs[count].top)/4
    xmax = (bbs[count].left + bbs[count].width)/4
    ymax = (bbs[count].top + bbs[count].height)/4
    w = xmax - xmin
    h = ymax - ymin
    area_obj = w*h 
    file1.write(path + img_path + " , " +  str(((area_obj/image_area)*100)) +" , "+ obj + "," + str(width/4) + ","+ str(height/4) +"\n")
 
