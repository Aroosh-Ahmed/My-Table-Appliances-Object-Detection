import cv2

im_path = "1.jpg"
file_pth = "1.txt"
def make_bounding_box(file_path,image_path):
  file = open(file_path, 'r')
  lines = file.readlines()
  image = cv2.imread(image_path)
  ih,iw,_ = image.shape
  for i in lines:
    label,x,y,w,h = map(float, i.split(' '))
    l = int((x - w / 2) * iw)
    r = int((x + w / 2) * iw)
    t = int((y - h / 2) * ih)
    b = int((y + h / 2) * ih)
    cv2.rectangle(image, (l, t), (r, b), (0, 0, 255), 1)
    cv2.imshow("Image",image)
    cv2.waitKey(0)

make_bounding_box(file_pth,im_path)

print("hi")