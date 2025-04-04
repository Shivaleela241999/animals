#!/usr/bin/env python3

import re
import sys
 
# Define the allowed API version range
MIN_VERSION = 1.0
MAX_VERSION = 2.0
API_FILE = "main.yml"

# File where API version is defined
def get_api_version():
    try:
        with open(API_FILE, "r") as file:
            for line in file:
                match = re.search(r'api_version:\s*"?(\d+\.\d+)"?', line)
                if match:
                    return float(match.group(1))
    except FileNotFoundError:
        print(f"Error: {API_FILE} not found!")
        sys.exit(1)
    return None

api_version = get_api_version()

if api_version is None:
    print("Error: API version not found in the file!")
    sys.exit(1)

if api_version is None or not (MIN_VERSION <= api_version <= MAX_VERSION):
    print("Error: API version {api_version} is out of range! Allowed: {MIN_VERSION} - {MAX_VERSION}")
    sys.exit(1)

print(f"API version {api_version} is valid.")
   
