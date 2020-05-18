# Overview

This simple proof of concept uses the dolby.io media processing APIs to analyze and enhance an audio file.

More information can be found here: https://dolby.io/developers/media-processing/introduction/overview

# Prerequisites

Get an API key by signing up at https://dolby.io/, and save the key as an environment variable named `API_KEY` either on your system or in a `.env` file

Create a Python virtual environment

        python3 -m venv venv

Activate the virtual environment

        source venv/bin/activate

Install necessary Python packages

        pip install -r requirements.txt

# Analyze audio

Use the dolby.io Media Processing APIs to analyze the `HBOIntoTheStorm.wav` signal in this directory, run the following command

        python analyze.py

# Analyze and enhance degraded audio (TODO)

First add random noise to the `HBOIntoTheStorm.wav` file by running the following command

        python add_noise.py

Then use the dolby.io Media Processing APIs to analyze and enhance the degraded audio file.

        python analyze_and_enhance.py