class Group:
    def __init__(self, name, status, all_members, members_in_game, members_online, members_in_chat, profile_picture):
        self.__name = name
        self.__status = status
        self.__all_members = all_members
        self.__members_in_game = members_in_game
        self.__members_online = members_online
        self.members_in_chat = members_in_chat
        self.__profile_picture = profile_picture
