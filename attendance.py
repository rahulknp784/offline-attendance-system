import os
import cv2
import face_recognition
from numpy import argmin

def take_attendance(attendence_image):
    knownFaces = [[i, i[0:-4]] for i in os.listdir(f'{os.getcwd()}/knownFaces') if i.endswith('.jpg')]

    for i in knownFaces:
        img = face_recognition.load_image_file(f'knownFaces/{i[0]}')
        faceloc = face_recognition.face_locations(img)
        i.append(face_recognition.face_encodings(img, faceloc)[0])
    name =[]

    students = cv2.imread(f'check/{attendence_image}')
    faceloc = face_recognition.face_locations(students)
    for(x, y, w, h) in faceloc:
        students = cv2.rectangle(students, (h, x), (y, w), (255, 0, 0), 2)
    encodedface = face_recognition.face_encodings(students, faceloc)

    for face in knownFaces:
        result = face_recognition.face_distance(encodedface, face[2])
        result1 = face_recognition.compare_faces(encodedface, face[2],  tolerance=0.5)
        index = argmin(result)

        if result1[index]:
            cv2.putText(students, face[1], (faceloc[index][3], faceloc[index][0]), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            name.append(face[1])
    cv2.imshow('students', students)
    cv2.waitKey(0)
    return name


if __name__ == '__main__':
    print(take_attendance('test.jpg'))
