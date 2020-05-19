import os
import requests
import time
import util
from pprint import pprint

def main():
    
    # define any environment variables
    API_KEY, AUDIO_FILE = util.get_env_vars()

    # define endpoints to post to
    media_input_url = 'https://api.dolby.com/media/input'
    analyze_url = 'https://api.dolby.com/media/analyze'

    # define media location to upload file to
    media_location = util.generate_media_location(AUDIO_FILE)

    # define header that will always be used
    headers = {
        'x-api-key': API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    # get pre-signed url for uploading file
    body = {
        'url': media_location,
    }

    try:
        response = requests.post(
            media_input_url, 
            json=body, 
            headers=headers,
        )
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    # upload file
    try:
        response = requests.put(
            response.json().get('url'),
            data=open(AUDIO_FILE, 'rb'),
        )
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    # request file analysis
    body = {
        'input' : media_location,
    }

    try:
        response = requests.post(
            analyze_url, 
            json=body, 
            headers=headers,
        )
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    # get and print analysis
    # retry after 5 seconds if analysis is not yet complete
    job_id_url = f"{analyze_url}?job_id={response.json().get('job_id')}"

    while True:
        try:
            response = requests.get(
                job_id_url,
                headers=headers,
            )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        if response.json().get('status') == 'Success':
            util.print_result(
                response.json().get('result')
            )
            break
        else:
            time.sleep(5)

if __name__ == "__main__":
    main()