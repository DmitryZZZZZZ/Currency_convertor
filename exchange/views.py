from django.shortcuts import render
import requests


def exchange_page(request):
    response = requests.get(url='https://v6.exchangerate-api.com/v6/d754506a3c5bcc0c9c3d36a6/latest/USD').json()
    currencies = response.get('conversion_rates')
    if request.method == 'GET':
        context = {
            'currencies': currencies,
        }
        return render(request=request, template_name='exchange/index.html', context=context)

    if request.method == 'POST':
        try:
            from_amount = float(request.POST.get('from_amount'))
            from_curr = request.POST.get('from_curr')
            to_curr = request.POST.get('to_curr')
            converted_amount = round((currencies[to_curr] / currencies[from_curr]) * float(from_amount), 2)
            context = {
                'from_amount': from_amount,
                'from_curr': from_curr,
                'to_curr': to_curr,
                'currencies': currencies,
                'converted_amount': converted_amount,
            }
        except(ValueError, TypeError):
            raise ValueError('Введите корректную валюту для конвертации!')
        return render(request=request, template_name='exchange/index.html', context=context)