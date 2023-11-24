from bardapi import BardCookies



class BardAi:
    # Hardcoded values are BS, shorlty i will buy a server and host it
    def __init__(self) -> None:
        self.secure_1psid = "bwhg95kJQg3u5FmDLJdMbeiFy_yy9PmZL-9IBCAhqLR7Liq2caMX11pWwTo9vF87WkHfnA."



    def get_response(self, query):
        cookie_dict = {
            "__Secure-1PSID": self.secure_1psid,
        }


        try:
            bard = BardCookies(cookie_dict=cookie_dict)
            return bard.get_answer(query)['content']
            
        except:
            print("Unable to work with Bard at this time. Please try again letter or contact support team.")
        

class GptAi:
    def __init__(self) -> None:
        pass