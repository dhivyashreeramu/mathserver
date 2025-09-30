from django.shortcuts import render

def lamp_power(request):
    I = R = P = ''
    
    if request.method == 'POST':
        try:
            I = float(request.POST.get('intensity', 0))
            R = float(request.POST.get('resistance', 0))
            P = I ** 2 * R
        except ValueError:
            P = "Invalid input"

    context = {
        'I': I,
        'R': R,
        'P': P
    }

    return render(request, 'priya/math.html', context)