from django.shortcuts import render

def rectangle_area(request):
    l = b = area = ''

    if request.method == 'POST':
        try:
            l = float(request.POST.get('length', 0))
            b = float(request.POST.get('breadth', 0))
            area = l * b
        except ValueError:
            area = "Invalid input"

    context = {
        'l': l,
        'b': b,
        'area': area
    }

    return render(request, 'priya/math.html', context)