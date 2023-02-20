import math
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Otp
from .serializers import OtpSerializer

from sms import send_sms

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

        storedOtp= list(Otp.objects.filter(mobile = mobile, ).values_list('otp')[0])[0]

        print(storedOtp)

        if incomingOtp==storedOtp:
            Otp.objects.filter(mobile = mobile ).delete()
            data= {
                'msg': 'Successfully verified OTP'
            }

            return Response(data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)