from django.shortcuts import render, redirect
from apps.base.models import Application, Main, Forms, Trips, Forms2, Forms3, Minilogo, Stuffs, Logo, Forms4
from apps.telegram_bot.views import get_text

# Create your views here.
def index(request):
    main_id = Main.objects.latest('id')
    forms = Forms.objects.all()
    trips = Trips.objects.all()
    forms2 = Forms2.objects.all()
    forms3 = Forms3.objects.all()
    minilogo = Minilogo.objects.all()
    stuffs = Stuffs.objects.all()
    logo = Logo.objects.latest('id')
    forms4 = Forms4.objects.all()
    return render(request, "base/index.html", locals())

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        cause = request.POST.get('cause')
        message = request.POST.get('message')
        Application.objects.create(name=name, number=number, email=email, cause=cause, message=message )
        get_text(f"""Поступила новая заявка
                 
                от пользователя: {name}
                {number}
                {email}
                {cause}
                {message}
""")
        return redirect("contact")
    return render(request, "base/contact.html")
