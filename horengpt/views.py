from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
import openai
from django.utils import timezone
from horen.models import ChatGPT
from decouple import config

openai_api_key =config('api_key')
openai.api_key = openai_api_key



def ask_openai(message):
    reply = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
        # prompt = message,
        # max_tokens = 1000,
        # n=1,
        # stop=None,
        # temperature = 0.7,
        messages =[
            {"role": "system", "content": "You are an helpful assistant"},
            {"role": "user", "content": message},
        ]
    )
    # print(reply)
    answer = reply.choices[0].message.content.strip()
    return answer

# @login_required(login_url = 'login')
def index(request):
    if request.user.is_authenticated:
        chats = ChatGPT.objects.filter(user=request.user)
        
    else:
        return render(request, 'index.html')
    context ={
        'chats': chats,
    }
    
    if request.method =='POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        chat = ChatGPT(user=request.user, message=message, response=response, created_date=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'index.html', context)











def current_year(request):
    year = datetime.now().year
    return render(request, 'index.html', {'current_year': current_year})