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

emotions = DeepFace.analyze(img_path = "/home/psk/Desktop/btp/django-auth/images/32.jpeg", 
        actions = ['age', 'gender', 'race','emotion']
)[0]

print('Facial Features: ')
print('\tAge: ', emotions['age'])
print('\n\tGender: ', emotions['gender'])
print('\n\tRace: ', emotions['race'])
print('\n\tEmotion: ', emotions['emotion'])
dominant_emotion= emotions['dominant_emotion']
dominant_emotion_value= emotions['emotion']['{}'.format(dominant_emotion)]

print('\nDominant emotion: ', dominant_emotion)
print('\nDominant emotion value: ', dominant_emotion_value)