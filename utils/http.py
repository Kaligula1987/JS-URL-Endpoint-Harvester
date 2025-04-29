import requests

def validate_url(url, timeout=5):
    """Validate URL by making an HTTP GET request"""
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code
    except requests.exceptions.RequestException:
        return None
