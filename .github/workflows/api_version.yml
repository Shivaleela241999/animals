#!/usr/bin/env python3

import re
import sys
 
# Define the allowed API version range
MIN_VERSION = "1.0"
MAX_VERSION = "2.0"
API_FILE = "get_api_version.yml"    

# File where API version is defined
def get_api_version():
    with open(API_FILE, "r") as file:
        for line in file:
            match = re.search(r"api_version:\s*(\d+\.\d+)", line)
            if match:
                return match.group(1)
    return None
 
api_version = get_api_version()
if not api_version:
    print("API version not found!")
    sys.exit(1)
 
if not (MIN_VERSION <= api_version <= MAX_VERSION):
    print(f" API version {api_version} is out of range! Allowed: {MIN_VERSION} - {MAX_VERSION}")
    sys.exit(1)
 
print(f"API version {api_version} is valid.")
sys.exit(0)
 
