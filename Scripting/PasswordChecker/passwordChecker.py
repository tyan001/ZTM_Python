import os
import sys
import requests
import hashlib

if __name__ == "__main__":

    url = "https://api.pwnedpasswords.com/range/" + 'CBFDA'
    res = requests.get(url)
    print(res)