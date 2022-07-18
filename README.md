# facebook-django

## Description
in this we have created facebook app clone which is having the following designs 

you can view this app in the link
[facebookCloneapp-django](https://facebook-django-akhil.herokuapp.com/)

to view the code for github tou can view in this [github link](https://github.com/abai118/facebook-django)

### user stories

As a user Facebook clone app have following features:
- As a logged in user, i should be able to create a post.
- As a logged in user, i should be able to like a post.
- As a logged in user, i should be able to create a comment on a post.
- As a logged in user, i should be able to edit my profile.
- As a logged in user, i should be able to send a friend request.
- As a logged in user, i should be able to accept a friend request.
- As a logged in user, i should be able to like a post.
- As a logged in user, i should be able to see my friends.
- As a logged in user, i should be able to edit my friend requests.
- As a logged in user, i should be able to search for friends.

### Database Schema Design

1. Userauth table

   - Userid (primary key)
   - Username
   - Password
   - First name
   - Last name
   - E mail

2. profile model
   - user
   - bio
   - profile pic
   - friends
  
3. post table
   - user
   - postimage(we would leave it as a blank)
   - post text
   - likes
   - time

4. comment
   - user
   - post id
   - comment text


### user persona
Person 1

1. User details
   - Name : Akhil
   - Age: 28
   - Work: Software Developper
   - Family: Single
   - Location: Bengalore

2. user hobies
   - Travelling to new places
   - Adopting new skills that are required

3. Motivations
   - Socialise with people
   - Knowing about people intrestes
   - Updating according to trends

4. frequently used apps
   - Instagram
   - Youtube
   - Pintrest
   - Twitter


Person2

1. User details
   - Name : Satya
   - Age: 28
   - Work: Season Business
   - Family: Single
   - Location: Vijayawada

2. user hobies
   - Travelling to temples
   - spending time with friends

3. Motivations
   - Finding new people with same interests
   - Knowing about people interests
  
4. frequently used apps
   - Instagram
   - Youtube