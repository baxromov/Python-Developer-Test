# Python-Developer-Test

```docker
docker-compose up --build -d
```

# Python Developer Test

You will need to write a simple network application. This task should not take more than a few days of relaxed research and
development. Most likely less than 4 hours overall, to be more precise.
The problem is synthetic and primitive. The solution is concrete enough to give all the information and hints. Yet adequately
vague to provide you all the creative and engineering space to solve it.
The ultimate goal is to render your thought and decision-making process, considering your level of expertise.

# Problem

On one side, there is a set of three 3rd-party API endpoints that provide similar data in JSON. The data is a sequence of 8-
byte-long UTF8 strings. Those endpoints update data in different periods: 15, 30, and 60 seconds. Also, data can be
identical across multiple endpoints.
On another side, there are 3rd-party clients who must be able to request the most up-to-date and unique data from a single
endpoint at any time. There can be multiple requests at the very same time. Yet the number of clients is limited.
In both cases, only GET requests are supported. Nothing more than HTTP/1.1 is required.

# Solution

Create an intermediate API microservice that will behave like a quasi-cache gateway. It must serve only one GET-endpoint
that will respond with accumulated data in JSON. The response data must have the same structure as the source data. The
resulting application must contain two components: client and server.
The client component must periodically request new data from those three 3rd-party endpoints by sending GET requests.
The periods must be the same: 15, 30, and 60 seconds. On a successful response, the client must safely store the results in
memory. On a failure, the client must log the errors. The client must get the endpoint URLs by accepting the value from an
argument or environment variable.
The server component must respond with the data from memory as fast as possible to as many clients as possible. Yet the
server must limit the number of clients by accepting the limit value from an argument or environment variable. Any client
request beyond the limit must get an appropriate HTTP error response.
Either the server or the client must deduplicate the data.
The final application must be a container with a compact runtime image. A complete Git repo with all the commits is a plus.
Test coverage is a plus as well.

# Limitations

You may use only the Python standard library. No 3rd-party modules or libraries are allowed. The only exception is a JSON
library. Also, you may not use 3rd-party databases or key-values storage. StackOverflow-copy-paste-fu and ChatGPT-do
techniques are prohibited as well.

# Examples

The 3rd-party API endpoint response looks like the following:

HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 23
Connection: close

["630e1244","5f4a8990"]

The server response must look (nearly) the same, considering all the accumulated and deduplicated data and optional extra
headers.
