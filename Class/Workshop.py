from Post import Post
class Workshop(Post):
    def __init__(self,id,media_link,poster,name,from_game,sub_date="",last_update="",is_recommend=None,is_favorite=None,is_subscribe=None):
        super().__init__(id,media_link,poster)
        self.__name = name
        self.__from_game = from_game
        self.__sub_date = sub_date
        self.__last_update = last_update
        self.__is_recommend = is_recommend
        self.__is_favorite = is_favorite
        self.__is_subscribe = is_subscribe