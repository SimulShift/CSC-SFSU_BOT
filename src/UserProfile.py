
# user profile is a datastructure that contains
# all the data we need to have on every person in the server
class UserProfile:
    
    def __init__(self):
        
        #  idea: we can have like a 3 strike system, strikes can be automatically added if bot detects potty language or something
        self.strikes = 0