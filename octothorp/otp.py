from tokenize import Token
from appdirs import user_data_dir
import os

class TokenStore:
    @classmethod
    def createNew(path) -> TokenStore:
        pass

def create_or_load_token_store(path=user_data_dir("octothorp") + "/tokens.otp"):
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        return TokenStore(path)
    
    pass