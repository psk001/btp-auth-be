import math
import random
import uuid  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Otp, Image, Election, ElectionCandidate
from .serializers import ImageSerializer, OtpSerializer, ElectionSerializer, ElectionCandidateSerializer

from deepface import DeepFace


# from sms import send_sms

class ElectionListView(APIView):
    def get(self, request, *args, **kwargs):
        electionList= Election.objects.all()
        serializer=ElectionSerializer(electionList, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data= request.data
        data['id']= uuid.uuid1()
        serializer= ElectionSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ElectionCandidateListView(APIView):
    def get(self, request, *args, **kwargs):
        electionCandidateDetail= ""
        if request.query_params.get('id') :
            electionCandidateDetail= ElectionCandidate.objects.filter(id=request.query_params.get('id'))
        else:
            electionCandidateDetail= ElectionCandidate.objects.all()
        serializer=ElectionCandidateSerializer(electionCandidateDetail, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data= request.data
        data['id']= uuid.uuid1()
        serializer= ElectionCandidateSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OtpListApiView(APIView):

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        print('Get otp request for ', request.query_params.get('mobile'))
        otpData = Otp.objects.filter(mobile = request.query_params.get('mobile'))
        # print(otpData)
        serializer = OtpSerializer(otpData, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request, *args, **kwargs):
           
        data = {
            'mobile': request.data.get('mobile'), 
            'otp': math.ceil(random.random()*1000000)
        }
        serializer = OtpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            # send_sms(
            #     'Your OTP for login is: {}'.format(data['otp']),
            #     '9741574592',
            #     ['{}'.format(data['mobile'])],
            #     fail_silently=False
            # )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOtpView(APIView):

    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, *args, **kwargs):
        incomingOtp= request.data.get('otp')
        mobile= request.data.get('mobile')

        print(incomingOtp, mobile)

        storedOtpList= list(Otp.objects.filter(mobile = mobile, ).values_list('otp'))      
        storedOtpList.reverse()

        print('OTP list: ',storedOtpList)

        finalOtp= list(storedOtpList[0])[0]

        print(finalOtp)

        if str(incomingOtp)==str(finalOtp):
            Otp.objects.filter(mobile = mobile ).delete()
            data= {
                'msg': 'Successfully verified OTP'
            }

            return Response(data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        
        data= request.data
        data['uniqueId']=  uuid.uuid1()
        image_serializer = ImageSerializer(data=data)

        if image_serializer.is_valid():
            image_serializer.save()

            # IMAGE MATCHING
            # img1 is uploaded img
            # img2 is fetched from block chain
            # face_matching_data= DeepFace.verify(img1_path='', img2_path='')



            # EMOTION DETECTION

            imagePath= '/home/psk/Desktop/btp/django-auth/images/{}'.format(data['title'])
            # emotions = DeepFace.analyze(img_path = imagePath, 
            #             actions = ['emotion']
            #         )
            
            # dominant_emotion= emotions[0]['dominant_emotion']
            # dominant_emotion_value= emotions[0]['emotion']['{}'.format(dominant_emotion)]

            # # to be stored in block chain
            # emotion_Data= {
            #     'dominant_emotion': dominant_emotion,
            #     'dominant_emotion_value': dominant_emotion_value
            # }

            # if dominant_emotion== 'fear' and dominant_emotion_value>=80:
            #     response_Data= {
            #         'emotion': 'Not in right state'
            #     }
            #     return Response(response_Data, status=status.HTTP_400_BAD_REQUEST)        

            return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    