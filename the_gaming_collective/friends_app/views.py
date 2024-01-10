from django.shortcuts import render, redirect
from django.contrib import messages
from account.models import Users

def display_friends(request):
    if 'user_id' not in request.session:
        # Redirect to login page or handle unauthorized access
        return redirect('login')  # You can replace 'login' with your login URL

    user = Users.objects.get(id=request.session['user_id'])
    friends = user.friends.all()  # Get the user's friends

    context = {
        'user': user,
        'friends': friends,
    }
    return render(request, "friends_main.html", context)

def add_friend(request):
    if 'user_id' not in request.session:
        # Redirect to login page or handle unauthorized access
        return redirect('login')  # You can replace 'login' with your login URL

    if request.method == 'POST':
        friend_username = request.POST['friend_username']

        try:
            friend = Users.objects.get(Q(username=friend_username) | Q(email=friend_username))
        except Users.DoesNotExist:
            messages.error(request, "User not found.")  # Display an error message
            return redirect('display_friends')  # Redirect back to the friends page

        user = Users.objects.get(id=request.session['user_id'])

        if friend == user:
            messages.error(request, "You can't add yourself as a friend.")
        else:
            user.friends.add(friend)
            messages.success(request, f"{friend.username} has been added to your friends.")

    return redirect('display_friends')  # Redirect back to the friends page
