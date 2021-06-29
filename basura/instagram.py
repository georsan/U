from instapy import InstaPy

session=InstaPy(username="georsan27",password="3Mv8425MMFc")
session.login()
session.set_relationship_bounds(enabled=True,max_followers=200)
session.set_do_follow(True,percentage=100)
session.like_by_tags(["bmw","steam","luffy","nike","ferrari"],amount=3)
session.set_dont_like(["nsfw"])
session.end
