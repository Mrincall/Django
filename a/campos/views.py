from django.shortcuts import render


def campos(request):
    return render(request, 'campos.html')


def rio(request):
    return render(request, 'rio.html')


def sao(request):
    return render(request, 'Sao.html')


def bp(request):
    return render(request, 'bp.html')


def rioreservcbp(request):
    if request.method == 'GET':
        return render(request, 'rioreservcbp.html')
    else:
        d3 = request.POST.get('d3')
        i3 = request.POST.get('i3')
        t3 = request.POST.get('t3')

        tt3 = (int(t3) - int(i3))
        p3 = (int(t3) - int(i3)) * 80
        context = {'data': d3, 'tempo': tt3, 'preco': p3}
        return render(request, "rioreservcbp.html", context)


def rioreservssf(request):
    if request.method == 'GET':
        return render(request, 'rioreservssf.html')
    else:
        d4 = request.POST.get('d4')
        i4 = request.POST.get('i4')
        t4 = request.POST.get('t4')

        tt4 = (int(t4) - int(i4))
        p4 = (int(t4) - int(i4)) * 60
        context = {'data': d4, 'tempo': tt4, 'preco': p4}
        return render(request, "rioreservssf.html", context)


def rioreservmdg(request):
    if request.method == 'GET':
        return render(request, 'rioreservmdg.html')
    else:
        d5 = request.POST.get('d5')
        i5 = request.POST.get('i5')
        t5 = request.POST.get('t5')

        tt5 = (int(t5) - int(i5))
        p5 = (int(t5) - int(i5)) * 50
        context = {'data': d5, 'tempo': tt5, 'preco': p5}
        return render(request, "rioreservmdg.html", context)


def spreservrb(request):
    if request.method == 'GET':
        return render(request, 'spreservrb.html')
    else:
        d6 = request.POST.get('dq')
        i6 = request.POST.get('i6')
        t6 = request.POST.get('t6')

        tt6 = (int(t6) - int(i6))
        p6 = (int(t6) - int(i6)) * 75
        context = {'data': d6, 'tempo': tt6, 'preco': p6}
        return render(request, "spreservrb.html", context)


def spreservasv(request):
    if request.method == 'GET':
        return render(request, 'spreservasv.html')
    else:
        d7 = request.POST.get('dg')
        i7 = request.POST.get('i7')
        t7 = request.POST.get('t7')

        tt7 = (int(t7) - int(i7))
        p7 = (int(t7) - int(i7)) * 60
        context = {'data': d7, 'tempo': tt7, 'preco': p7}
        return render(request, "spreservasv.html", context)


def spreservaf(request):
    if request.method == 'GET':
        return render(request, 'spreservaf.html')
    else:
        d8 = request.POST.get('d9')
        i8 = request.POST.get('i8')
        t8 = request.POST.get('t8')

        tt8 = (int(t8) - int(i8))
        p8 = (int(t8) - int(i8)) * 80
        context = {'data': d8, 'tempo': tt8, 'preco': p8}
        return render(request, "spreservaf.html", context)


def bpreservcsc(request):
    if request.method == 'GET':
        return render(request, 'bpreservcsc.html')
    else:
        data = request.POST.get('df')
        inicio = request.POST.get('if')
        termino = request.POST.get('tf')

        tempo = (int(termino) - int(inicio))
        preco = (int(termino) - int(inicio)) * 65
        context = {'data': data, 'tempo': tempo, 'preco': preco}
        return render(request, "bpreservcsc.html", context)


def bpreservbg(request):
    if request.method == 'GET':
        return render(request, 'bpreservbg.html')
    else:
        d1 = request.POST.get('de')
        i1 = request.POST.get('i1')
        t1 = request.POST.get('t1')

        tt1 = (int(t1) - int(i1))
        p1 = (int(t1) - int(i1)) * 40
        context = {'data': d1, 'tempo': tt1, 'preco': p1}
        return render(request, "bpreservbg.html", context)


def bpreservrsc(request):
    if request.method == 'GET':
        return render(request, 'bpreservrsc.html')
    else:
        d2 = request.POST.get('dd')
        i2 = request.POST.get('i2')
        t2 = request.POST.get('t2')

        tt2 = (int(t2) - int(i2))
        p2 = (int(t2) - int(i2)) * 80
        context = {'data': d2, 'tempo': tt2, 'preco': p2}
        return render(request, "bpreservrsc.html", context)


