from django.shortcuts import render

def home(request):
    bmi = None
    category = None

    if request.method == "POST":
        weight = float(request.POST.get("weight"))
        height = float(request.POST.get("height"))

        bmi = round(weight / (height * height), 2)

        if bmi < 18.5:
            category = "Ondergewicht"
        elif bmi < 25:
            category = "Gezond gewicht"
        elif bmi < 30:
            category = "Overgewicht"
        else:
            category = "Obesitas"

    return render(request, "scientific_app/index.html", {
        "bmi": bmi,
        "category": category
    })
