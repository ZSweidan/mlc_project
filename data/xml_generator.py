import xml.etree.ElementTree as gfg 
nb_frames = test_flight.num_frames
image_area =  (2448/4)*(2048/4)
print("img area", image_area)
frames_keys = []
bbs = []
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
  # display(test_frame_img)
  # extracting the bbox info for each frame 
  airborne_objects = test_flight.detected_objects
  print(test_frame.num_detected_objects)
  for obj in airborne_objects:
    
    if obj in test_frame.detected_object_locations:
      # print(obj)
      frame_objects.append(obj)
      # print("The distance is" ,test_frame.detected_object_locations[obj].range_distance_m)
      print("The bbox is",test_frame.detected_object_locations[obj].bb)
      bb = test_frame.detected_object_locations[obj].bb
      print(bb)
      bbs.append(bb)

  #  writing XML file for each frame
  img_path = test_frame.image_path()
  path = "/content/airborne-detection-starter-kit/data/part1/"
  
  print(path+ img_path)
  image = cv2.imread(path + img_path, cv2.IMREAD_GRAYSCALE)
  print(image.shape)
  height = image.shape[0]
  width = image.shape[1]

  dst = cv2.resize(image, (int(width/4), int(height/4)))

  print(dst.shape)
  # cv2_imshow(dst)
  img_name = (os.path.splitext(test_frame.image_path())[0]).rsplit('/', 1)[-1]
  path = '/content/airborne-detection-starter-kit/data/images_xml'
  cv2.imwrite(os.path.join(path , img_name+ ".png"), dst)
  # cv2.waitKey(0)

# img_name = os.path.splitext(test_frame.image_path())[0]
  img_name = (os.path.splitext(test_frame.image_path())[0]).rsplit('/', 1)[-1]

  root = gfg.Element("annotation")

  s1= gfg.SubElement(root, "folder")
  s1.text = "trainfolder"  

  s2= gfg.SubElement(root, "filename")
  s2.text = os.path.basename(test_frame.image_path())

  s3= gfg.SubElement(root, "path")
  s3.text = img_path 

  e2 = gfg.Element("source")
  root.append (e2)
  s1_2 = gfg.SubElement(e2, "database")
  s1_2.text = "unknown"

  e3 = gfg.Element("size")
  root.append (e3)
  s1_3 = gfg.SubElement(e3, "width")
  s1_3.text = str(2448/4)
  s2_3 = gfg.SubElement(e3, "height")
  s2_3.text = str(2048/4)
  s3_3 = gfg.SubElement(e3, "depth")
  s3_3.text = "img depth"
  
  s4= gfg.SubElement(root, "segmented")
  s4.text = "0"  

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
    
    
    e4 = gfg.Element("object")
    root.append (e4)
    s1_4 = gfg.SubElement(e4, "name")
    s1_4.text = re.sub("\d", "", obj)
    s2_4 = gfg.SubElement(e4, "ratio_with_respect_to_the_whole_image")
    s2_4.text = str((area_obj/image_area)*100)
    s3_4 = gfg.SubElement(e4, "difficult")
    s3_4.text = "0"
  
    s4_4 = gfg.SubElement(e4, "bndbox")
    s1_4_4 = gfg.SubElement(s4_4, "xmin")
    s1_4_4.text = str(xmin)
    s2_4_4 = gfg.SubElement(s4_4, "ymin")
    s2_4_4.text = str(ymin)
    s3_4_4 = gfg.SubElement(s4_4, "xmax")
    s3_4_4.text = str(xmax)
    s4_4_4 = gfg.SubElement(s4_4, "ymax")
    s4_4_4.text = str(ymax)
    count +=1
  
    tree = gfg.ElementTree(root)
      
    with open ("images_xml/"+img_name + ".xml", "wb") as files :
        tree.write(files)   
