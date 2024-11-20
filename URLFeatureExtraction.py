from urllib.parse import urlparse
import ipaddress
import re
import whois
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# 1. IP Address in the URL
def havingIP(url):
    try:
        ipaddress.ip_address(url)
        return 1
    except:
        return 0

# 2. "@" Symbol in URL
def haveAtSign(url):
    return 1 if "@" in url else 0

# 3. Length of URL
def getLength(url):
    return 0 if len(url) < 54 else 1

# 4. Depth of URL
def getDepth(url):
    return len([segment for segment in urlparse(url).path.split('/') if segment])

# 5. Redirection "//" in URL
def redirection(url):
    pos = url.rfind('//')
    return 1 if pos > 7 else 0

# 6. "http/https" in Domain name
def httpDomain(url):
    domain = urlparse(url).netloc
    return 1 if 'https' in domain else 0

# 7. Using URL Shortening Services
def tinyURL(url):
    shorteners = [
        "bit.ly", "goo.gl", "shorte.st", "tinyurl.com", "ow.ly", "t.co", 
        "bitly.com", "is.gd", "buff.ly", "adf.ly", "tr.im", "tiny.cc"
    ]
    domain = urlparse(url).netloc
    return 1 if domain in shorteners else 0

# 8. Prefix or Suffix "-" in Domain
def prefixSuffix(url):
    return 1 if '-' in urlparse(url).netloc else 0

# 9. DNS Record availability
def dnsRecord(url):
    try:
        requests.get("http://" + url, timeout=5)
        return 0
    except:
        return 1

# 10. Web Traffic (Placeholder for testing purposes)
def web_traffic(url):
    try:
        return 1
    except:
        return 1

# 11. Age of Domain
def domainAge(url):
    try:
        domain_info = whois.whois(urlparse(url).netloc)
        creation_date = domain_info.creation_date
        expiration_date = domain_info.expiration_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]
        age = (expiration_date - creation_date).days if creation_date and expiration_date else 0
        return 0 if age > 365 else 1
    except:
        return 1

# 12. End Period of Domain
def domainEnd(url):
    try:
        domain_info = whois.whois(urlparse(url).netloc)
        expiration_date = domain_info.expiration_date
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]
        end_period = (expiration_date - datetime.now()).days if expiration_date else 0
        return 0 if end_period > 180 else 1
    except:
        return 1

# 13. Suspicious Keywords in Domain
def suspiciousKeywords(url):
    # Keywords often used in phishing URLs
    suspicious_words = ['secure', 'account', 'login', 'verify', 'signin', 'update', 'support']
    return 1 if any(word in urlparse(url).netloc.lower() for word in suspicious_words) else 0

# 14. IFrame Redirection
def iframe(response):
    if response is None or response.text == "":
        return 1
    return 0 if re.findall(r"[<iframe>|<frameBorder>]", response.text) else 1

# 15. Status Bar Customization (onMouseOver)
def mouseOver(response):
    if response is None or response.text == "":
        return 1
    return 1 if re.findall("<script>.+onmouseover.+</script>", response.text) else 0

# 16. Disabling Right Click
def rightClick(response):
    if response is None or response.text == "":
        return 1
    return 0 if re.findall(r"event.button ?== ?2", response.text) else 1

# 17. Website Forwarding
def forwarding(response):
    if response is None:
        return 1
    return 0 if len(response.history) <= 2 else 1

# Function to fetch HTTP response with error handling
def get_http_response(url):
    try:
        response = requests.get(url, timeout=5)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error in get_http_response: {e}")
        return None

# Main feature extraction function
def featureExtraction(url):
    features = [
        havingIP(url),
        haveAtSign(url),
        getLength(url),
        getDepth(url),
        redirection(url),
        tinyURL(url),
        prefixSuffix(url),
        dnsRecord(url),
        web_traffic(url),
        domainAge(url),
        domainEnd(url),
        suspiciousKeywords(url)
    ]
    
    response = get_http_response(url)
    
    # HTML & JavaScript based features
    html_js_features = [
        iframe(response),
        mouseOver(response),
        rightClick(response),
        forwarding(response),
    ]
    
    return features + html_js_features
