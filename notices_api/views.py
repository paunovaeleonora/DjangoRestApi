from rest_framework.generics import ListAPIView
from rest_framework.mixins import ListModelMixin


from .models import Notices
from rest_framework import filters

from .pagination import MyPagination
from .serializers import NoticeSerializer


# Create your views here.

class ListNoticesView(ListAPIView, ListModelMixin):

    queryset = Notices.objects.all()
    serializer_class = NoticeSerializer
    pagination_class = MyPagination

    def get(self, request):
        return self.list(request)


class SearchByNoticeId(ListAPIView):
    queryset = Notices.objects.all()
    serializer_class = NoticeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['notice_number']
    pagination_class = MyPagination


class SearchByDate(SearchByNoticeId):
    queryset = Notices.objects.all()
    serializer_class = NoticeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['notice_date']

