from deepface import DeepFace

backends = [
  'opencv', 
  'ssd', 
  'dlib', 
  'mtcnn', 
  'retinaface', 
  'mediapipe'
]

# result = DeepFace.verify(img1_path = "3.jpg", img2_path = "2.jpg")
# print(result)


#face detection and alignment
# face_objs = DeepFace.extract_faces(img_path = "1.jpg", 
#         target_size = (224, 224), 
#         detector_backend = backends[4]
# )
# print(face_objs)

emotions = DeepFace.analyze(img_path = "22.jpeg", 
        actions = ['emotion']
)

dominant_emotion= emotions[0]['dominant_emotion']
dominant_emotion_value= emotions[0]['emotion']['{}'.format(dominant_emotion)]

print(dominant_emotion, dominant_emotion_value)