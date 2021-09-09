image_area =  (2448/4)*(2048/4)

file1 = open("dataset.txt", "a") 
for id in flights_ids:
  print(id)
  test_flight = dataset.get_flight_by_id(id)
  final_flight_keys = []
  flight_keys = test_flight.frames.keys()
  airborne_objects = test_flight.detected_objects
  final_flight_keys = []
  for key in flight_keys:
    test_frame = test_flight.get_frame(key)
    if test_frame.num_detected_objects == 0:
      continue
    bbs = []
    frame_objects = []
    final_flight_keys.append(key)
    for obj in airborne_objects:
      
      if obj in test_frame.detected_object_locations:
        frame_objects.append(obj)
        bb = test_frame.detected_object_locations[obj].bb
        bbs.append(bb)

    #  writing XML file for each frame
    img_path = test_frame.image_path()
    path = "/content/airborne-detection-starter-kit/data/part1/"
    img_name = (os.path.splitext(test_frame.image_path())[0]).rsplit('/', 1)[-1]
    path = '/content/airborne-detection-starter-kit/data/images_xml'

  # To implement a foor loop, itterates over all objects and append them to the XML file
    count = 0
    for obj in frame_objects:
      w = (bbs[count].width)//4
      h = (bbs[count].height)//4
      area_obj = w*h 
      count +=1
      str_key = str(key)
      obje = re.sub("\d", "", obj)
      # print(obje)
      file1.write(test_flight.id + " , " + str_key + " , " + path + img_path + " , " +  str(((area_obj/image_area)*100)) +" , "+ obje + "," + str(2448/4) + ","+ str(2048/4) +"\n")