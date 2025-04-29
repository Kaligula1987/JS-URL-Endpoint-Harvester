import re

def extract_urls(js_code):
    """Extract all URLs from the JS file's code"""
    # This regex captures both absolute and relative URLs
    pattern = r'["\']((?:https?:)?\/\/[^\s"\']+)["\']'
    return list(set(re.findall(pattern, js_code)))
