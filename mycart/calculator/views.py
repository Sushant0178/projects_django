from django.shortcuts import render

def index(request):
    result = None  # always define this at the top

    if request.method == "POST":
        num1 = request.POST.get("num1", "")
        num2 = request.POST.get("num2", "")
        operation = request.POST.get("operation", "")

        try:
            n1 = float(num1)
            n2 = float(num2)

            if operation == "add":
                result = n1 + n2
            elif operation == "subtract":
                result = n1 - n2
            elif operation == "multiply":
                result = n1 * n2
            elif operation == "divide":
                if n2 != 0:
                    result = n1 / n2
                else:
                    result = "Cannot divide by zero!"
        except:
            result = "Invalid input!"

    # return render(request, "calulator/cal.html", {"result": result})
    return render(request, "calculator/cal.html", {"result": result})


# Create your views here.