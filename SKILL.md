---
name: tembo-sdk-python-sdk
description: "Python SDK for Tembo SDK API. Use when writing Python code that calls Tembo SDK API with the tembo-sdk-python package: installing it, constructing and authenticating the client, and calling API operations."
---

# Tembo SDK Python SDK

Generated Python client for Tembo SDK API, published as `tembo-sdk-python`. Use the generated client instead of hand-writing HTTP requests.

## Install

```sh
pip install tembo-sdk-python
```

## Client setup and authentication

```python
import os

from tembo import Tembo

client = Tembo(
    api_key=os.environ.get("TEMBO_API_KEY"),
)
```

Provide credentials using the options below. Environment variables are read automatically when the target runtime supports them:

- `api_key` (env: `TEMBO_API_KEY`) — Credential for the apiKey scheme.

## Calling operations

```python
import os

from tembo import Tembo

client = Tembo(
    api_key=os.environ.get("TEMBO_API_KEY"),
)

api_key = client.api_keys.list(
    limit=50,
)

print(api_key)
```

Method names, parameter shapes, and response types are generated from the API description — do not guess them. Look up the exact call signature in [api.md](./api.md) before writing a call.

## WebSockets

WebSocket endpoints open a persistent connection you can send messages to and receive messages from.

```python
with client.live.connect() as connection:
    message = connection.recv()
    print(message)
```

## Error handling

Non-success responses throw generated API errors. Error objects expose status, headers, response body, and request metadata where the target runtime supports it.

```python
from tembo import APIStatusError

try:
    api_key = client.api_keys.list(
        limit=50,
    )
except APIStatusError as err:
    print(err.status_code, err.message)
    raise
```

## Requirements

- Python 3.9 or newer

## Reference files

- [README.md](./README.md) — full feature tour: client options, retries and timeouts, logging.
- [api.md](./api.md) — complete catalogue of every operation with request and response types.
