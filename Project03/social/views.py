from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from . import models

def messages_view(request):
    """Private Page Only an Authorized User Can View, renders messages page
       Displays all posts and friends, also allows user to make new posts and like posts
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render private.djhtml
    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)

        posts = []
        numposts = request.session.get('count',1)
        allposts = []
        for post in models.Post.objects.all().order_by('-timestamp'):
            allposts += [post]
        for num in range(numposts):
            if len(allposts) <= num:
                pass
            else:
                posts += [allposts[num]]
        context = { 'user_info' : user_info
                  , 'posts' : posts }
        return render(request,'messages.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def account_view(request):
    """Private Page Only an Authorized User Can View, allows user to update
       their account information (i.e UserInfo fields), including changing
       their password
    Parameters
    ---------
      request: (HttpRequest) should be either a GET or POST
    Returns
    --------
      out: (HttpResponse)
                 GET - if user is authenticated, will render account.djhtml
                 POST - handle form submissions for changing password, or User Info
                        (if handled in this view)
    """
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_info = models.UserInfo.objects.get(user=request.user)
            passchangeform = PasswordChangeForm(request.user,request.POST)
            if passchangeform.is_valid():
                user = passchangeform.save()
                update_session_auth_hash(request,user)
                return redirect('social:account_view')
            oldemployment = user_info.employment
            newemployment = request.POST['employment']
            if oldemployment != newemployment:
                user_info.employment = newemployment
            oldlocation = user_info.location
            newlocation = request.POST['location']
            if oldlocation != newlocation:
                user_info.location = newlocation
            oldbirthday = user_info.birthday
            newbirthday = request.POST['birthday']
            if oldbirthday != newbirthday:
                user_info.birthday = newbirthday
            interestChecker = 0
            newinterest = request.POST['interest']
            if newinterest == "":
                pass
            else:
                for interest in user_info.interests.all():
                    if interest.label == newinterest:
                        interestChecker = 1
                if interestChecker == 0:
                    checkInterest = 0
                    for interest in models.Interest.objects.all():
                        if interest.label == newinterest:
                            checkInterest = 1
                    if checkInterest == 0:
                        models.Interest.objects.create(label=newinterest)
                        user_info.interests.add(newinterest)
                    else:
                        user_info.interests.add(newinterest)
            user_info.save()
        else:
            user_info = models.UserInfo.objects.get(user=request.user)
            passchangeform = PasswordChangeForm(request.user)

        context = { 'user_info' : user_info,
                    'passchangeform' : passchangeform }
        return render(request,'account.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def people_view(request):
    """Private Page Only an Authorized User Can View, renders people page
       Displays all users who are not friends of the current user and friend requests
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render people.djhtml
    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)
        numppl = request.session.get('counter',1)
        people = []
        all_people = []
        for person in models.UserInfo.objects.all():
            if person not in user_info.friends.all() and person.user != user_info.user:
                people += [person]
        for num in range(numppl):
            if len(people) <= num:
                pass
            else:
                all_people += [people[num]]
        friend_requests = []
        for fr in models.FriendRequest.objects.all():
            if fr.to_user == user_info:
                friend_requests += [fr]

        context = { 'user_info' : user_info,
                    'all_people' : all_people,
                    'friend_requests' : friend_requests }

        return render(request,'people.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def like_view(request):
    '''Handles POST Request recieved from clicking Like button in messages.djhtml,
       sent by messages.js, by updating the corrresponding entry in the Post Model
       by adding user to its likes field
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postID,
                                a string of format post-n where n is an id in the
                                Post model

	Returns
	-------
   	  out : (HttpResponse) - queries the Post model for the corresponding postID, and
                             adds the current user to the likes attribute, then returns
                             an empty HttpResponse, 404 if any error occurs
    '''
    postIDReq = request.POST.get('postID')
    if postIDReq is not None:
        postID = int(postIDReq[5:])
        if request.user.is_authenticated:
            user_info = models.UserInfo.objects.get(user=request.user)
            count = 0
            for checkpost in models.Post.objects.all().order_by('-timestamp'):
                if count == postID:
                    post = checkpost
                count += 1
            alreadythere = 0
            for like in post.likes.all():
                if like.user == user_info:
                    alreadythere = 1
            if alreadythere == 0:
                post.likes.add(user_info)
                post.save()
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('like_view called without postID in POST')

def post_submit_view(request):
    '''Handles POST Request recieved from submitting a post in messages.djhtml by adding an entry
       to the Post Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postContent, a string of content

	Returns
	-------
   	  out : (HttpResponse) - after adding a new entry to the POST model, returns an empty HttpResponse,
                             or 404 if any error occurs
    '''
    postContent = request.POST.get('postContent')
    if postContent is not None:
        if request.user.is_authenticated:

            user_info = models.UserInfo.objects.get(user=request.user)
            post = models.Post.objects.create(owner=user_info,content=postContent)
            post.save()
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('post_submit_view called without postContent in POST')

def more_post_view(request):
    '''Handles POST Request requesting to increase the amount of Post's displayed in messages.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating hte num_posts sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of posts dispalyed

        i = request.session.get('count',1)
        request.session['count'] = i + 1
        return HttpResponse()

    return redirect('login:login_view')

def more_ppl_view(request):
    '''Handles POST Request requesting to increase the amount of People displayed in people.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating the num ppl sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of people dispalyed

        i = request.session.get('counter',1)
        request.session['counter'] = i + 1
        return HttpResponse()

    return redirect('login:login_view')

def friend_request_view(request):
    '''Handles POST Request recieved from clicking Friend Request button in people.djhtml,
       sent by people.js, by adding an entry to the FriendRequest Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute frID,
                                a string of format fr-name where name is a valid username

	Returns
	-------
   	  out : (HttpResponse) - adds an etnry to the FriendRequest Model, then returns
                             an empty HttpResponse, 404 if POST data doesn't contain frID
    '''
    frID = request.POST.get('frID')
    if frID is not None:
        username = frID[3:]

        if request.user.is_authenticated:
            user_info = models.UserInfo.objects.get(user=request.user)
            people = []
            for person in models.UserInfo.objects.all():
                if str(person.user) == username:
                    people += [person]
            touser = people[0]
            alreadyThere = 0
            for request in models.FriendRequest.objects.all():
                if request.to_user == touser and request.from_user == user_info:
                    alreadyThere = 1
            if alreadyThere == 0:
                fr = models.FriendRequest(to_user=touser,from_user=user_info)
                fr.save()
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('friend_request_view called without frID in POST')

def accept_decline_view(request):
    '''Handles POST Request recieved from accepting or declining a friend request in people.djhtml,
       sent by people.js, deletes corresponding FriendRequest entry and adds to users friends relation
       if accepted
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute decision,
                                a string of format A-name or D-name where name is
                                a valid username (the user who sent the request)

	Returns
	-------
   	  out : (HttpResponse) - deletes entry to FriendRequest table, appends friends in UserInfo Models,
                             then returns an empty HttpResponse, 404 if POST data doesn't contain decision
    '''
    data = request.POST.get('decision')
    if data is not None:
        aORd = data[0]
        username = data[2:]
        if request.user.is_authenticated:

            user_info = models.UserInfo.objects.get(user=request.user)
            people = []
            for person in models.UserInfo.objects.all():
                if str(person.user) == username:
                    people += [person]
            fromuser = people[0]
            if aORd == "A":
                user_info.friends.add(fromuser)
                fromuser.friends.add(user_info)
                for fr in models.FriendRequest.objects.all():
                    if fr.to_user == user_info and fr.from_user == fromuser:
                        fr.delete()
                    elif fr.to_user == fromuser and fr.from_user == user_info:
                        fr.delete()
            elif aORd == "D":
                fr = models.FriendRequest.objects.get(to_user=user_info,from_user=fromuser)
                fr.delete()
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('accept-decline-view called without decision in POST')













