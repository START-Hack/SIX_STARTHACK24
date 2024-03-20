# This is a basic sample to use Azure OpenAI
# 3 configurations are available in the file openAI_config.json
#
# pre-requisites:
#   - pip install --upgrade openai

import os
from openai import AzureOpenAI
import json

# Load config values
with open(r'openAI_config.json') as config_file:
    openAI_config = json.load(config_file)

my_config = openAI_config['openAIConfigs'][2]

print(f"use openAI config {my_config['configName']}")

# Setting up the deployment name
chatgpt_model_name = my_config['model']

client = AzureOpenAI(
    api_key=my_config['apiKey'],
    api_version=my_config['apiVersion'],
    azure_endpoint=my_config['urlBase']
)
# Send a completion call to generate an answer
print('Sending a test completion job')
start_phrase = "Explain what are article 8 and 9, in the SFDR regulation."
response = client.chat.completions.create(
    model=chatgpt_model_name,
    messages=[{"role": "assistant", "content": start_phrase}])
print(f"{start_phrase}\n{response.choices[0].message.content}")