from django.shortcuts import render
from rest_framework.views import APIView
from .models import Notice as NoticeModel
from .serializers import NoticeListSerializer, NoticeSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class NoticeListView(APIView):
    def get(self, request):
        notices = NoticeModel.objects.get(id=1)
        return Response(NoticeListSerializer(notices).data, status=status.HTTP_200_OK)

class NoticeView(APIView):
    def post(self, request):
        notice_serializer = NoticeSerializer(data=request.data)
        print(notice_serializer)
        if notice_serializer.is_valid():
            notice_serializer.save()
            return Response({"message": "공지사항 작성에 성공했다북"}, status=status.HTTP_200_OK)
        else:
            print(notice_serializer.errors)
            return Response({"message": "공지사항 작성에 실패했다북"}, status=status.HTTP_400_BAD_REQUEST)
