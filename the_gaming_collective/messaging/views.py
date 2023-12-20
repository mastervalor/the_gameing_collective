from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Chat, Message

# Create your views here.

@login_required
def chat_list(request):
    chats = Chat.objects.filter(participants=request.user)
    if not chats:
        messages.warning(request, "You have no messages yet!")
        chats = None
    context = {'chats': chats}
    return render(request, 'chat/list.html', context)

@login_required
def chat_detail(request, chat_id):
    try:
        chat = Chat.objects.get(id=chat_id, participants=request.user)
    except Chat.DoesNotExist:
        messages.error(request, "Chat not found.")
        return redirect('name-of-some-error-page')
    
    messages = Message.objects.filter(chat=chat).order_by('-timestamp')
    context = {'chat': chat, 'messages': messages}
    return render(request, 'chat/detail.html', context)