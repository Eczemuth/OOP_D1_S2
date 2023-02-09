import time
class Review:
    def __init__(self,user,comment_description,recommendation):
        self.__name = user.name
        self.__profile = user.profile_picture
        self.__comment_description = comment_description
        self.__recommendation = recommendation
        self.__review_score = 0
        self.__create_date = time.time()
