local_path = notebook_path + '/part2'
s3_path = 's3://airborne-obj-detection-challenge-training/part2/'
dataset.add(local_path, s3_path, prefix='part2')

# You can add multi-part dataset as well, using below..
local_path = notebook_path + '/part3'
s3_path = 's3://airborne-obj-detection-challenge-training/part3/'
dataset.add(local_path, s3_path, prefix='part3')