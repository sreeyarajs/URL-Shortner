import requests

def shorten_url(api_key, url_to_shorten):
    """
    Shortens a URL using the Cutt.ly API.

    :param api_key: str - Your Cutt.ly API key.
    :param url_to_shorten: str - The URL you want to shorten.
    :return: str - The shortened URL or an error message.
    """
    # API URL for shortening
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url_to_shorten}"

    try:
        # Send a GET request
        response = requests.get(api_url)

        # Ensure the response is successful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Check if the response status indicates success
        if data.get("url", {}).get("status") == 7:
            return f"Shortened URL: {data['url']['shortLink']}"
        else:
            # Error from API
            return f"Error: {data['url'].get('title', 'Unknown error')}"
    except requests.exceptions.RequestException as e:
        # Handle HTTP errors
        return f"HTTP error occurred: {e}"
    except Exception as e:
        # Handle general errors
        return f"An error occurred: {e}"

# Replace with your actual API key from Cutt.ly
API_KEY = "2a687ce6a7cb606288d955bf59ec8827d8eee"

def main():
    print("=== URL Shortener ===")
    if API_KEY == "your_actual_cuttly_api_key":
        print("Error: Please replace 'your_actual_cuttly_api_key' with your actual API key.")
        return

    url = input("Enter the URL to shorten: ").strip()

    if not url:
        print("Error: No URL provided.")
        return

    # Call the shorten_url function
    result = shorten_url(API_KEY, url)
    print(result)

if __name__ == "__main__":
    main()
