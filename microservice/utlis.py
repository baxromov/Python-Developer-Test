import http.client
import json


def fetch_data(host, port):
    conn = http.client.HTTPConnection(host='app', port=8001)
    conn.request("GET", "/data")
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    conn.close()
    return json.loads(data)
