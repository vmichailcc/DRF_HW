from rest_framework.decorators import api_view, action
from rest_framework.response import Response
import datetime
from store.models import Store
from store.serializers import StoreSerializer
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser

dt_today = datetime.datetime.now()


@api_view()
def hello_world(request):
    return_dict = {"msg": "Hello, world!"}
    return Response(return_dict)


@api_view()
def today(request):
    return_dict = {
        "date": dt_today.strftime('%d/%m/%Y'),
        "year": dt_today.strftime('%Y'),
        "month": dt_today.strftime('%m'),
        "day": dt_today.strftime('%d'),
    }
    return Response(return_dict)


@api_view()
def my_name(request, name_of_hacker):
    return_dict = {"name": f"{name_of_hacker.title()}"}
    return Response(return_dict)


@api_view(http_method_names=["POST"])
def calculator(request):
    params = request.data
    result = ""
    try:
        action = params["action"]
        number1 = int(params["number1"])
        number2 = int(params["number2"])
    except ValueError:
        raise ValueError("Input error")

    if action in ("minus", "plus", "divide", "multiply"):
        if action == "plus":
            result = number1 + number2
        if action == "minus":
            result = number1 - number2
        if action == "multiply":
            result = number1 * number2
        if action == "divide":
            if number2 != 0:
                result = number1 / number2
            else:
                raise ZeroDivisionError("Сannot be divided by 0")
        return Response(result)
    else:
        raise ValueError("Input error")


'''
Для проверки калькулятора:
{
"action": "minus",
"number1": 10,
"number2": 5
}
'''


class StoreApiView(APIView):
    def get(self, request):
        stores = Store.objects.all()
        serializers = StoreSerializer(stores, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = StoreSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(status=HTTP_201_CREATED, data=serializers.data)


class StoreViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class MyStoreModelView(ModelViewSet):
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(**{'owner': self.request.user})

    def get_queryset(self):
        user = self.request.user
        return Store.objects.filter(owner=user.pk)

    @action(detail=True, methods=['post'])
    def mark_as_active(self, request, pk=None):
        mark = self.get_object()
        if mark.status == "deactivated":
            mark.status = "active"
            mark.save()
        serializer = self.get_serializer(mark)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def mark_as_deactivated(self, request, pk=None):
        mark = self.get_object()
        if mark.status == "active":
            mark.status = "deactivated"
            mark.save()
        serializer = self.get_serializer(mark)
        return Response(serializer.data)


class AdminStories(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ['get', 'post']

    @action(detail=True, methods=['post'])
    def mark_as_active(self, request, pk=None):
        mark = self.get_object()
        if mark.status == "in_review":
            mark.status = "active"
            mark.save()
        serializer = self.get_serializer(mark)
        return Response(serializer.data)
