def classify_url(url):
    """Classify the URL based on predefined keywords"""
    keywords = {
        "auth": ["auth", "token", "login", "logout"],
        "upload": ["upload", "file", "media"],
        "payment": ["payment", "checkout", "billing"],
    }

    for category, keys in keywords.items():
        if any(k in url.lower() for k in keys):
            return category
    return "unknown"
