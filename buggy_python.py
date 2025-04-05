import os
import hashlib
import subprocess
import logging
import base64
from urllib import request

# Issue 1: Hardcoded password
password = "super_secret_password"

# Issue 2: Using weak hash function (MD5)
hash_object = hashlib.md5(b'password')
print(f'MD5 hash: {hash_object.hexdigest()}')

# Issue 3: Command injection vulnerability
user_input = "example_input"
subprocess.run(f"ls {user_input}", shell=True)

# Issue 4: Insecure use of eval
user_data = "{'key': 'value'}"
result = eval(user_data)
print(result)

# Issue 5: Hardcoded API key
API_KEY = '1234567890abcdef'

# Issue 6: Open redirect vulnerability (unsafe URL)
url = 'http://example.com'
request.urlopen(f"{url}?redirect={base64.b64encode(b'http://malicious.com').decode()}")

# Issue 7: Use of insecure logging (printing sensitive information)
logging.basicConfig(level=logging.DEBUG)
logging.debug(f"User password: {password}")

# Issue 8: Insecure temporary file creation
temp_file = os.tmpfile()
temp_file.write(b"Sensitive data")
temp_file.close()

# Issue 9: Use of unsafe deserialization
import pickle
data = pickle.loads(b'cos\nsystem\n(S"rm -rf /"\ntR.')
print(data)

