# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'warren__manuel'
insta_password = 'eURocUP201212345'

comments = [
        'Terrific picture! @{} Truly in love with your feed :green_heart:',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        ':fire: :fire:',
        ':ok-hand:',
        'Awesome shot :thumbsup:'
        ':clap: :clap:',
        'This is an amazing capture! :open_mouth:',
        'This is just :raised_hands:',
        ':fire: :clap:',
        'Wow! Just amazing @{}'
        ':raised_hands: Yes!']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username = insta_username,
                  password = insta_password,
                  headless_browser =True)

with smart_run(session):
  """ Activity flow """		
  # general settings		
  # session.set_dont_include(["friend1", "friend2", "friend3"])		
  
  # activity		
  session.like_by_tags(['natgeo','skyporn','sunset'], amount=50)

  # Joining Engagement Pods
  session.set_do_comment(enabled=True, percentage=35)
  session.set_comments(comments, media = 'Photo')
  session.join_pods(topic='travel', engagement_mode='light')
