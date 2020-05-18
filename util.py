import os
import string
import random
from typing import Tuple
from dotenv import load_dotenv

def get_env_vars() -> Tuple[str, str]:
    """
    Function to get environment variables from .env file
    """
    load_dotenv()
    
    return (
        os.getenv('API_KEY'),
        os.getenv('AUDIO_FILE')
    )
    
def generate_media_location(name: str) -> str:
    """
    Function to generate a random media location name
    """
    chars = string.ascii_lowercase + string.digits
    size = 6
    rand_str = ''.join(random.choice(chars) for _ in range(size))
    name = name.split('.')[0]
    return f"dlb://{name}-{rand_str}.wav"