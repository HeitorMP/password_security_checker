
# A python script that checks if a password has already been pwned!

Pwned Passwords are hundreds of millions of real world passwords previously exposed in data breaches. This exposure makes them unsuitable for ongoing use as they're at much greater risk of being used to take over other accounts. They're searchable online below as well as being downloadable for use in other online systems.

### How it works:
the script generates the sha1 hash of your password locally, requests from the api all hashes that start with the first 5 characters of your password hash.

This way you never send your full password to the api.

With the list stored locally, the script tests the complete password, using the local data and returns the number of times your password has been pwned!


### How to run:

#### You will need python3 and pip installed!

Install dependencies to run the gui version

```bash
  pip3 install tkinter
```

Usage:

```bash
  python3 pass-checker.py
  or
  python3 pass-checker-gui.py
```


