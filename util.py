import os
import string
import random
from typing import Dict, Tuple
from dotenv import load_dotenv


def get_env_vars() -> Tuple[str, str]:
    """
    Function that gets environment variables from .env file
    """
    load_dotenv()
    
    return (
        os.getenv('API_KEY'),
        os.getenv('AUDIO_FILE')
    )


def generate_media_location(name: str) -> str:
    """
    Function that generates a random media location name
    """
    chars = string.ascii_lowercase + string.digits
    size = 6
    rand_str = ''.join(random.choice(chars) for _ in range(size))
    name = name.split('.')[0]
    return f"dlb://{name}-{rand_str}.wav"


def print_dict(d: Dict) -> None:
    """
    Function that prints keys and values in a dictionary
    """
    for k, v in d.items():
        print(f"    {k}: {v}")


def print_result(result: Dict) -> None:
    """
    Function that prints audio file analysis information in
    an easy to read format
    """
    print("media_info:")
    print("  container:")
    print_dict(result.get('media_info').get('container'))
    print("  audio:")
    print_dict(result.get('media_info').get('audio'))
    print("audio:")
    print("  clipping:")
    print_dict(result.get('audio').get('clipping'))
    print("  loudness:")
    print_dict(result.get('audio').get('loudness'))
    print("  noise:")
    print_dict(result.get('audio').get('noise'))
    print("  silence:")
    print_dict(result.get('audio').get('silence'))
