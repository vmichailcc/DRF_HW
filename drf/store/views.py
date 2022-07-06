from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime
from store.models import Store
from store.serializers import StoreSerializer
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

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
    action = params["action"]
    result = ""
    try:
        number1 = int(params["number1"])
        number2 = int(params["number2"])
    except ValueError:
        print("jib,rf")

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
