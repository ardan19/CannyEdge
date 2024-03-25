import cv2

# Fungsi untuk melakukan pengenalan wajah menggunakan ekstraksi fitur tepi
def recognize_face(frame, face_cascade):
    # Ubah citra ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi wajah dalam citra
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:
        # Ekstraksi fitur tepi menggunakan metode Canny edge detection
        edges = cv2.Canny(gray[y:y+h, x:x+w], 100, 200)

        # Tampilkan hasil ekstraksi tepi tepi
        cv2.imshow('Edge Detection', edges)

        # Tampilkan kotak di sekitar wajah
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Tambahkan label pada wajah yang terdeteksi
        cv2.putText(frame, 'Human', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    
    return frame

# Mulai tangkap video dari webcam
cap = cv2.VideoCapture(0)

# Load Haar Cascade Classifier untuk deteksi wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Baca setiap frame dari video
    ret, frame = cap.read()
    
    # Lakukan pengenalan wajah
    recognized_frame = recognize_face(frame, face_cascade)
    
    # Tampilkan frame hasil pengenalan wajah
    cv2.imshow('Face Recognition', recognized_frame)
    
    # Cek jika pengguna menekan tombol 'q', jika ya, hentikan program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Hentikan tangkapan video dan tutup semua jendela
cap.release()
cv2.destroyAllWindows()
