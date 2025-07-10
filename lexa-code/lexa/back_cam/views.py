from django.shortcuts import render
import cv2
from django.http import StreamingHttpResponse
from .navigasyon_ve_serial import gen_frames
from .serit_takip import main
from .models import MainModel
from .serializer import MainModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import numpy as np
from tensorflow.keras.models import load_model
from skimage import transform, exposure
import tensorflow as tf

def serit_takip_stream(request):
    return StreamingHttpResponse(main(), content_type='multipart/x-mixed-replace; boundary=frame')

def photo_stream(request):
    return StreamingHttpResponse(gen_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

def back_cam(request):
    return render(request,"back_cam.html")

def back_cam_stream(request):
    def start_stream():
        frameWidth = 960
        frameHeight = 480
        cap = cv2.VideoCapture(1)
        cap.set(3, frameWidth)
        cap.set(4, frameHeight)
        while True:
            ret, image = cap.read()
            image = cv2.flip(image, 1)
            ret, buffer = cv2.imencode('.jpg',image)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        cap.release()
        cv2.destroyAllWindows()

    return StreamingHttpResponse(start_stream(), content_type='multipart/x-mixed-replace; boundary=frame')


@api_view(['GET'])
def get_request(request):
    if request.method == 'GET':
        hiz = MainModel.objects.all().filter(id=3).first()
        sabitonoff = MainModel.objects.all().filter(id=4).first()
        far = MainModel.objects.all().filter(id=5).first()
        gerivites = MainModel.objects.all().filter(id=6).first()
        tur = MainModel.objects.all().filter(id=7).first()
        engelsolbir = MainModel.objects.all().filter(id=8).first()
        engelsoliki = MainModel.objects.all().filter(id=9).first()
        engelsoluc = MainModel.objects.all().filter(id=10).first()
        engelsagbir = MainModel.objects.all().filter(id=11).first()
        engelsagiki = MainModel.objects.all().filter(id=12).first()
        engelsaguc = MainModel.objects.all().filter(id=13).first()
        all_data = hiz, sabitonoff, far, gerivites, tur, engelsolbir, engelsoliki, engelsoluc, engelsagbir, engelsagiki, engelsaguc
        serializer = MainModelSerializer(all_data,many=True)
        return Response(serializer.data)

@api_view(['POST'])
def post_request(request):
    if request.method == 'POST':
        received_hiz_data = {"value":request.data["hiz"]}
        
        received_sabitonoff_data = {"value":request.data["sabitonoff"]}
        
        received_far_data = {"value":request.data["far"]}

        received_gerivites_data = {"value":request.data["gerivites"]}
        
        received_tur_data = {"value":request.data["tur"]}

        received_engelsolbir_data = {"value":request.data["engelsolbir"]}

        received_engelsoliki_data = {"value":request.data["engelsoliki"]}

        received_engelsoluc_data = {"value":request.data["engelsoluc"]}

        received_engelsagbir_data = {"value":request.data["engelsagbir"]}

        received_engelsagiki_data = {"value":request.data["engelsagiki"]}

        received_engelsaguc_data = {"value":request.data["engelsaguc"]}
        
        serializer_hiz = MainModelSerializer(data=received_hiz_data)
        
        serializer_sabitonoff = MainModelSerializer(data=received_sabitonoff_data)
        
        serializer_far = MainModelSerializer(data=received_far_data)
        
        serializer_gerivites = MainModelSerializer(data=received_gerivites_data)
        
        serializer_tur = MainModelSerializer(data=received_tur_data)

        serializer_engelsolbir = MainModelSerializer(data=received_engelsolbir_data)

        serializer_engelsoliki = MainModelSerializer(data=received_engelsoliki_data)

        serializer_engelsoluc = MainModelSerializer(data=received_engelsoluc_data)

        serializer_engelsagbir = MainModelSerializer(data=received_engelsagbir_data)

        serializer_engelsagiki = MainModelSerializer(data=received_engelsagiki_data)

        serializer_engelsaguc = MainModelSerializer(data=received_engelsaguc_data)
        
        if serializer_engelsaguc.is_valid() and serializer_engelsagiki.is_valid() and serializer_engelsagbir.is_valid() and serializer_engelsolbir.is_valid() and serializer_engelsoliki.is_valid() and serializer_engelsoluc.is_valid() and serializer_hiz.is_valid() and serializer_sabitonoff.is_valid() and serializer_far.is_valid() and serializer_gerivites.is_valid() and serializer_tur.is_valid():
            existing_data3 = MainModel.objects.filter(id=3).first()
            existing_data4 = MainModel.objects.filter(id=4).first()
            existing_data5 = MainModel.objects.filter(id=5).first()
            existing_data6 = MainModel.objects.filter(id=6).first()
            existing_data7 = MainModel.objects.filter(id=7).first()
            existing_data8 = MainModel.objects.filter(id=8).first()
            existing_data9 = MainModel.objects.filter(id=9).first()
            existing_data10 = MainModel.objects.filter(id=10).first()
            existing_data11 = MainModel.objects.filter(id=11).first()
            existing_data12 = MainModel.objects.filter(id=12).first()
            existing_data13 = MainModel.objects.filter(id=13).first()
            if existing_data13 and existing_data11 and existing_data12 and  existing_data10 and existing_data3 and existing_data4 and existing_data5 and existing_data6 and existing_data7 and existing_data8 and existing_data9:                
                serializer_hiz.update(existing_data3, serializer_hiz.validated_data)
                
                serializer_sabitonoff.update(existing_data4, serializer_sabitonoff.validated_data)
                
                serializer_far.update(existing_data5, serializer_far.validated_data)

                serializer_gerivites.update(existing_data6, serializer_gerivites.validated_data)
                
                serializer_tur.update(existing_data7, serializer_tur.validated_data)

                serializer_engelsolbir.update(existing_data8, serializer_engelsolbir.validated_data)

                serializer_engelsoliki.update(existing_data9, serializer_engelsoliki.validated_data)

                serializer_engelsoluc.update(existing_data10, serializer_engelsoluc.validated_data)

                serializer_engelsagbir.update(existing_data11, serializer_engelsagbir.validated_data)

                serializer_engelsagiki.update(existing_data12, serializer_engelsagiki.validated_data)

                serializer_engelsaguc.update(existing_data13, serializer_engelsaguc.validated_data)
                
                return Response(status=status.HTTP_200_OK)
            else:
                serializer_hiz.save()
                serializer_sabitonoff.save()
                serializer_far.save()
                serializer_gerivites.save()
                serializer_tur.save()
                serializer_engelsolbir.save()
                serializer_engelsoliki.save()
                serializer_engelsoluc.save()
                serializer_engelsagbir.save()
                serializer_engelsagiki.save()
                serializer_engelsaguc.save()
                return Response(status=status.HTTP_200_OK)

def tr_stream(request):
    def tr():
        wanted_classes_names = [
            'Speed limit (20km/h)', 
            'Speed limit (30km/h)',  
            'Speed limit (50km/h)',  
            'Speed limit (60km/h)',  
            'Speed limit (70km/h)',  
            'Stop',                  
            'Road Work',             
            'Turn Right Ahead',      
            'Turn Left Ahead'        
        ]

        def preprocess(image):
            image = transform.resize(image, (32, 32), anti_aliasing=True)
            image = image.astype('float32')
            return image.reshape(1, 32, 32, 3)

        tflite_model_path = "C:\\Users\\Lenovo\\Desktop\\lexa-code\\lexa\\back_cam\\lexa_team_tf_test_v4.tflite" #PATH
        
        interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
        interpreter.allocate_tensors()
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        cap = cv2.VideoCapture(0)
        print("Kamera açıldı. Çıkmak için 'q' tuşuna basın.")

        while True:
            ret, frame = cap.read(0)
            if not ret:
                print("Kamera okunamadı.")
                break
            
            h, w, _ = frame.shape
            cx, cy = w // 2, h // 2
            x1, x2 = cx - 100, cx + 100
            y1, y2 = 0, cy + 100

            roi = frame[y1:y2, x1:x2]

            try:
                input_img = preprocess(roi).astype(np.float32)

                interpreter.set_tensor(input_details[0]['index'], input_img)
                interpreter.invoke()
                pred = interpreter.get_tensor(output_details[0]['index'])[0]

                class_index = np.argmax(pred)
                probability = np.max(pred)

                #print(f"Tahmin olasılıkları: {pred}")
                #print(f"Tahmin edilen sınıf: {wanted_classes_names[class_index]} - Olasılık: {probability:.3f}")

                if probability > 0.7:
                    text = f"{wanted_classes_names[class_index]} - %{round(probability * 100, 1)}"
                    frame_h, frame_w, _ = frame.shape

                    font_scale = 1.2  # Küçük ekran için uygun
                    thickness = 2
                    text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)

                    text_x = 0
                    text_y = 30

                    cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX,
                                font_scale, (0, 0, 255), thickness)

            except Exception as e:
                print("Hata:", e)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        cap.release()
        cv2.destroyAllWindows()

    return StreamingHttpResponse(tr(), content_type='multipart/x-mixed-replace; boundary=frame')
