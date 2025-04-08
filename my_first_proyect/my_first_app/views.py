from django.shortcuts import render  # type: ignore

# Create your views here.
def my_view(request):
    car_list = [
        {"title": "BMW"},
        {"title": "Mazda"},
    ]  # type: ignore
    context = {
        "car_list": car_list
    }
    return render(request, "my_first_app/car_list.html", context)
