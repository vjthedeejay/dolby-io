# Overview

This simple proof of concept uses the dolby.io media processing APIs to analyze and enhance an audio file.

More information can be found here: https://dolby.io/developers/media-processing/introduction/overview

# Prerequisites

Get an API key by signing up at https://dolby.io/

Save the following as environment variables either on your system or in a `.env` file

- `API_KEY`: Dolby.io API key
- `AUDIO_FILE`: Name of file in current directory to be analyzed

Create a Python virtual environment

        python3 -m venv venv

Activate the virtual environment

        source venv/bin/activate

Install necessary Python packages

        pip install -r requirements.txt

# Analyze audio

Use the dolby.io Media Processing APIs to analyze the `AUDIO_FILE` signal, run the following command

        python analyze.py

# Analyze and enhance degraded audio (TODO)

First add random noise to the `AUDIO_FILE` signal by running the following command

        python add_noise.py

Then use the dolby.io Media Processing APIs to analyze and enhance the degraded audio file.

        python analyze_and_enhance.py
