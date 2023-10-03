import requests


def fetch_and_display_status(url):
    """
    Fetches the content of the given URL and displays it with tabulation.

    Args:
    url (str): The URL to fetch the content from.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP error status codes

        print("Status code:", response.status_code)
        print("Response body:")
        print("\t-", "\n\t- ".join(response.text.splitlines()))

    except requests.exceptions.RequestException as e:
        print("An error occurred while making the request:", e)


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    fetch_and_display_status(url)
