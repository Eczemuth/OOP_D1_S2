class Publisher:
    def __init__(self, name, publisher_id, profile_picture = '', about = '', products = [], followers = [], links_to_other_site = ''):
        self.__name = name
        self.__publisher_id = publisher_id
        self.__profile_picture = profile_picture
        self.__about = about
        self.__products = products
        self.__followers = followers
        self.__links_to_other_site = links_to_other_site
