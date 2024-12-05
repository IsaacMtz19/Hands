import cv2
import mediapipe as mp
import os

nombre = 'una_mano'
direccion = "C:\\Users\\isaac\\OneDrive\\Documentos\\Python\\Ia_proyecto\\Fotos\\Entrenamiento"
carpeta = os.path.join(direccion, nombre)

if not os.path.exists(carpeta):
    print('Carpeta creada:', carpeta)
    os.makedirs(carpeta)

# Asignamos un contador para el nombre de las fotos
cont = 0
cap = cv2.VideoCapture(0)



while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo acceder a la cámara")
        break

    # Convertir la imagen a RGB
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


    # Guardar la imagen completa de la cámara
    cv2.imwrite(os.path.join(carpeta, f"Foto_{cont}.jpg"), frame)
    cont += 1

    # Mostrar la imagen en tiempo real
    cv2.imshow("Video", frame)

    k = cv2.waitKey(1)
    if k == 27 or cont >= 150:  # Esc para salir o 300 fotos tomadas
        break

cap.release()
cv2.destroyAllWindows()
