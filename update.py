#!/usr/bin/python3
import subprocess
import requests
from requests.auth import HTTPBasicAuth
import os
import sys

PDF_URL = "https://gho.berlin/wp-content/frei_stunden/VPS.pdf"
PDF_FILE_NAME = "vertretungsplan.pdf"

# download url to given file name; if no name given use name from URL
# chunk size defaults to 1 KiB
def downloadFile(url, auth, fname = None, chunkSize = 1024):
    if not fname:
        fname = url.split('/')[-1]

    response = requests.get(url, auth=auth, stream=True)

    # download each chunk and save to file
    with open(fname, 'wb') as f:
        for chunk in response.iter_content(chunk_size=chunkSize):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    # return the file name (only useful, if name was get from url)
    return fname

def main(username, password):
    # download Vertretungsplan pdf
    downloadFile(PDF_URL, HTTPBasicAuth(username, password), fname = PDF_FILE_NAME)

    print("Extracting HTML ...")
    subprocess.call(["bash", "extract-html.sh"], shell=False)

    print("Extracting JSON ...")
    subprocess.call(["python3", "extract-json.py"])

    # delete pdf file
    os.remove(PDF_FILE_NAME)


if __name__ == "__main__":
    # arguments
    if len(sys.argv) < 3:
        print("No username or password given!")
        print("Usage: " + sys.argv[0] + " USERNAME PASSWORD")
        exit(1)

main(sys.argv[1], sys.argv[2])
