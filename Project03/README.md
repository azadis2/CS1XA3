# CS1XA3 Project 03 - MacId : azadis2

## Contents

1. Requirements
2. Usage
3. Objectives

## **Requirements**

* A working computer 
* Wi-fi 
* A web browser of your choice

## **Usage**

Install conda environment with:

``` 
conda activate djangoenv
```

* If you want to run locally: Go to the project root folder (the one with *manage.py* inside) and type:

```
python manage.py runserver localhost:8000
```

* If you want to run on mac1xa3 server:

```
python manage.py runserver localhost:10008 &
```
Access the website at: **mac1xa3.ca/e/azadis2/**

## **Objectives**

### Objective 1: Signup and Login

#### Description:
When you go to *mac1xa3.ca/3/azadis2/* , you will see 2 options:

* **Create an account**: When you click on this, you will be redirected to the signup page which is handled by **singup_view** in **Project03/login/views.py** and **Project03/login/templates/signup.djhtml.**
Creating an account will create a *UserInfo* object and when you do so, you will be directed to the messages page.

* **Login**: The login page is handled by **login_view** in **Project03/login/views.py** and **Project03/login/templates/login.djhtml.**

#### Exceptions:

Logging in or creating a user with an invalid Username or Password will require the user to input them again.

### Objective 2: Adding User Profile and Interests

#### Description:

Provides the information of the logged in user on the left hand column of the page. This is handled by **messages.djhtml**, **people.djhtml**, **account.djhtml** and  **social_base.djhtml** in **Project03/social/templates/**.

#### Exceptions: 

No exceptions.

### Objective 3: Account Settings Page

#### Description:

 This will enable the user to change their password, add information regarding employment, location, birthday and interests and also to update this info.
 Changing the password and user information is handled by **account_view** in **Project03/social/views.py** and **Project03/social/templates/account.djhtml.**

 #### Exceptions:
 
 If the user inputs the birthday in wrong format(i.e not YYYY-MM-DD), a ValidationError will be thrown.

### Objective 4: Displaying list of people

#### Description:

Enables the user to see other user's profiles.
This page is handled by **people_view** in **Project03/social/views, Project03/social/templates/people.djhtml, and Project03/social/static/people.js.**
**people_view** creates a list of **UserInfo** objects that the user is not friends with that is sent to **people.djhtml** to be rendered.
Clicking the more button at the bottom of the page is handled by **people.js**.

#### Exception:

The number of people that are displayed returns to 1 when the user logs out.

### Objective 5: Sending Friend Requests

#### Description:
Allows the user to send friend requests to user who they are not friends with. The friend request button is handled by **Project03/social/static/people.js.**
In **people.js**, the ID of the friend request button which contains the username of the other user is sent in a POST request to **friend_request_view** in **Project03/social/views.py.**
Friend requests are rendered by **people_view** in **Project03/social/views.py and Project03/social/templates/people.djhtml**, and contain accept and decline buttons.
#### Exception:

Users who are already friends with the user cannot be sent friend requests. Once a user has been sent a friend request, clicking the button more will not create more **FriendRequest** objects.

### Objective 6: Accepting/ Declining friend requests

#### Description

Enables the user to accept or decline friend requests from other users, this feature is handled by **accept_decline_view** in **Project3/social/templates/people.djhtml** and **Project3/social/static/people.js**. If the decline button is pushed **accept_decline_view** removes the friend request and updates both users' **UserInfo** object.

#### Exceptions

* If User_1 and User_2 send requests to each other and User_2 declines the friend request, (i.e *only*  that friend request will be removed and User_1 has still a friend request which was sent by User_2).

* If both users send requests to each other and and User_2 accepts the friend, both requests will be removed.

### Objective 7: Displaying Friends

#### Description:

Displays the current users friend list on the messages page, which is handled by **messages_view** in **Project03/social/views.py** and **Project03/social/templates/messages.djhtml**.
**messages.djhtml** displays a list of all of the users friends along the right side of the page.

### Objective 8: Submitting Posts

#### Description

Allows users to submit posts.
This is handled by **post_submit_view** in **Project03/social/views.py, Project03/social/templates/messages.djhtml, and Project03/social/static/messages.js.**

### Objective 9: Displaying Post Lists

#### Description

Displays a list of posts in order of newest to oldest from every user on the messages page.
This is handled by **messages_view** in **Project03/social/views.py, Project03/social/templates/messages.djhtml, and Project03/social/static/messages.js.**

### Objective 10: Liking Posts and Displaying Like Count

#### Description

Displays a list of posts in order of newest to oldest from every user on the messages page.
This is handled by **messages_view in Project03/social/views.py, Project03/social/templates/messages.djhtml, and Project03/social/static/messages.js.**

### Objective 11: Test Database

#### Description

A test database has been created. Their User names and passwords are listed below.

UserName | Password
-------- | --------
TestUser | 1234
TestUser_2| wadfu7-sycpec-nomWyp
MichaelScott | mic@mic@m
Hi1 | ryjbic-5qyqMo-jintof
Sparx | 1234abcde
HarryPotter | hogwartsissonotlame&boring
