#!/usr/bin/env python3

import argparse
import requests
from parser.extractor import extract_urls
from utils.http import validate_url
from utils.classify import classify_url

def fetch_js(url):
    """Fetch the JS content from a URL"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for non-200 responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="JS Endpoint Harvester & Validator")
    parser.add_argument("js_url", help="URL to JavaScript file")
    args = parser.parse_args()

    js_code = fetch_js(args.js_url)
    if not js_code:
        return

    # Extract URLs from the JavaScript code
    endpoints = extract_urls(js_code)

    print(f"\nFound {len(endpoints)} potential endpoints:\n")
    for endpoint in endpoints:
        status = validate_url(endpoint)
        category = classify_url(endpoint)
        print(f"[{status or 'ERR'}] {endpoint}  --> {category}")

if __name__ == "__main__":
    main()
