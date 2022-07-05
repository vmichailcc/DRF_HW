from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime

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


@api_view()
def calculator(request):
    params = request.query_params
    result = ''
    action = params["action"]
    try:
        number1 = int(params["number1"])
        number2 = int(params["number2"])
    except ValueError:
        raise ValueError("Ошибка ввода. Введите число")

    if action in ("minus", "plus", "divide", "multiply"):
        if action == "plus":
            result = number1 + number2
        if action == "minus":
            result = number1 - number2
        if action == "multiply":
            result = number1 * number2
        try:
            if action == "divide" and number2 != 0:
                result = number1 / number2
        except ValueError:
            raise ValueError("number2 не может быть равен 0")
    else:
        raise ValueError("Ошибка ввода. Введен не корректное знаяение action")
    return Response(result)

# ?action=plus&number1=2&number2=3
