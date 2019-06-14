import face_recognition

from PIL import Image
from PIL import ImageDraw

import os

cwd = os.getcwd()

image = face_recognition.load_image_file(cwd + "/images/friends.jpg")
person1 = face_recognition.load_image_file(cwd + "/images/person1.jpg")
person2 = face_recognition.load_image_file(cwd + "/images/person2.jpg")
person3 = face_recognition.load_image_file(cwd + "/images/person3.jpg")
person4 = face_recognition.load_image_file(cwd + "/images/person4.jpg")

anton_encoding = face_recognition.face_encodings(person1)[0]
ali_encoding = face_recognition.face_encodings(person2)[0]
karl_encoding = face_recognition.face_encodings(person3)[0]
kendrick_encoding = face_recognition.face_encodings(person4)[0]

known_face_encodings = [anton_encoding, ali_encoding, karl_encoding, kendrick_encoding]


face_loc = face_recognition.face_locations(image)

face_enc = face_recognition.face_encodings(image, known_face_locations = face_loc)

results = []

for i in range(4):
    rec = face_recognition.compare_faces(known_face_encodings, face_enc[i])
    results.append(rec)
    
    if rec[0]:
        print("Anton detected")
    
    if rec[1]:
        print("Ali detected")
        
    if rec[2]:
        print("Karl detected")
        
    if rec[3]:
        print("Kendrick detected")
        
    if not any(rec):
        print("Unknown Face")

if not results:
    print("No Faces Were Found")
    
print(len(face_enc), "faces were found")

image_ar = Image.fromarray(image)

#in order to specify width, I had to use this function
def drawrect(drawcontext, xy, outline=None, width=0):
    (x1, y1), (x2, y2) = xy
    points = (x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1, y1)
    drawcontext.line(points, fill=outline, width=width)


for i in face_loc:
    top, right, bottom, left = i
    
    pen = ImageDraw.Draw(image_ar)

    drawrect(pen, ((right, bottom), (left, top)), outline = "green", width = 3)

image_ar.show()






























