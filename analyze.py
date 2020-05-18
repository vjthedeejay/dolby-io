import os
import requests
import time
import util

def main():
    
    # define any environment variables
    env_vars = util.get_env_vars()
    API_KEY = env_vars.get('api_key')

    # define endpoints to post to
    media_input_url = 'https://api.dolby.com/media/input'
    analyze_url = 'https://api.dolby.com/media/analyze'

    # define file to upload
    my_file = 'HBOIntoTheStorm.wav'

    # define media location to upload file to
    media_location = util.generate_media_location(my_file)

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
            data=open(my_file, 'rb'),
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

    # get analysis
    job_id_url = f"{analyze_url}?job_id={response.json().get('job_id')}"

    try:
        response = requests.get(
            job_id_url,
            headers=headers,
        )
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


    while 1:
        if response.json().get('status') == 'Success':
            # print analysis
            print(response.json().get('result'))
            break
        else:
            # wait for 5 seconds
            time.sleep(5)

            # try getting analysis again
            try:
                response = requests.get(
                    job_id_url,
                    headers=headers,
                )
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)


if __name__ == "__main__":
    main()