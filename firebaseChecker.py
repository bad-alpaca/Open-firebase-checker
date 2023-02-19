import argparse
import sys
import requests

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--list", help="List of URLs to check", default="stdin")
args = parser.parse_args()

# Read URLs from standard input or file
if args.list == "stdin":
    urls = sys.stdin.read().splitlines()
else:
    with open(args.list, "r") as f:
        urls = f.read().splitlines()

# Add .json to the end of each URL
urls = [url.strip() + "/.json" for url in urls]

# Loop through the URLs and print the status code
try:
    for url in urls:
        response = requests.get(url)
        code = response.status_code
        print(f"{url} - {code}")
except requests.exceptions.RequestException as e:
    print(f"{url} - {e}")
except KeyboardInterrupt:
    print("Exiting...")
    sys.exit(0)
