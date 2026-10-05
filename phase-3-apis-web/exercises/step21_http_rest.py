"""
Step 21 - HTTP & REST API Concepts
Practice: Status code meanings, buildig a URL with query parameters,
and reading a JSON response. (No real request yet - that comes in Step 22.)
"""

import json
from urllib.parse import urlencode

def describe_status(code):
    """Return a short human-readablemeaning of an HTTP status code."""
    known_codes = {
        200: "Ok - request succeeded",
        201: "Created - a new resource was created",
        400: "Bad Request - the data we sent is invalid",
        401: "Unauthorized - API key is missing or wrong",
        404: "Not Found - wrong URL or endpoint",
        429: "Too Many Requests - slow down (rate limit)",
        500: "Internal Server Error - problem on the server",
        503: "Service Unavailable - server is busy or down",
    }

    if code in known_codes:
        return known_codes[code]
    #Fallbackto the first digit for codes we didn't list
    if 200 <= code < 300:
        return "Success (2xx)"
    if 400 <= code < 500:
        return "Client error (4xx) - fix our request"
    if 500 <= code <600:
        return "Server error (5xx) - wait and retry"
    return "Unknown status code"

def build_url(base_url, path, params):
    """Combine base URL, path, and query parameters into a full URL."""
    query_string = urlencode(params) # turns a dic into key=value&key=value
    return f"{base_url}{path}?{query_string}"

# 1. Status codes
print("=== Status codes ===")
for code in [200, 400, 401, 404, 429, 503, 418]:
    print(f"{code}: {describe_status(code)}")

# 2. Building a URL from parts
print("\n=== Building a URL ===")
weather_params = {
    "latitude": 23.81,
    "longitude": 90.41,
    "current_weather": "true",
    "timezone": "Asia/Dhaka",
}

url = build_url("https://api.open-meteo.com", "/v1/forecast", weather_params)
print(url)

# 3. Reading a JSOn response (copied from the real browser result)
print("\n=== Reading a JOSOn response ===")
response_text = '{"latitude": 23.81,"current_weather": {"temperature": 30.3}}'
data = json.loads(response_text) # JSOn text -> Python dictionary
temperature = data["current_weather"]["temperature"] # dict inside a dict
print(f"Current temperature in Dhaka: {temperature}°C")

