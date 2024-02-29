# flask jwt starter
```
git clone https://github.com/imylomylo/flask_jwt_starter
cd flask_jwt_starter
docker-compose up
```
To see the jwt flow In another terminal
```
./login.curl
```

## without docker
```
git clone https://github.com/imylomylo/flask_jwt_starter
cd flask_jwt_starter
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

If there are pip errors, maybe your system doesn't have python-pip installed.

## How it (generally) works, as per ChatGPT

In a typical JWT-based authentication system with token refreshing, the refresh token itself doesn't get renewed. Instead, when a client uses a refresh token to obtain a new access token, a new refresh token may be issued along with the new access token.

Here's how the process generally works:

 - Initial login: When a user logs in, the server issues both an access token and a refresh token. These tokens are sent back to the client, usually in the response body.

 - Token expiration: The access token has a short expiration time, while the refresh token typically has a longer expiration time. When the access token expires, the client can use the refresh token to obtain a new access token.

 - Token refreshing: The client sends a request to a designated endpoint (often /refresh) with the refresh token included in the request, usually in the Authorization header. The server verifies the refresh token and issues a new access token.

 - Issuing a new refresh token: Depending on your security requirements and implementation, the server may also issue a new refresh token along with the new access token. This helps mitigate certain security risks, such as token replay attacks.

 - Updating the client: The client updates its stored tokens with the new access token and, optionally, the new refresh token.

 - Repeat: The client continues to use the access token to access protected resources until it expires. When the access token expires again, the process repeats, with the client using the refresh token to obtain a new access token.

It's important to note that the exact implementation details, including how and when refresh tokens are issued or updated, may vary depending on your specific requirements and the libraries or frameworks you're using for authentication. Make sure to consult the documentation for your authentication library or framework for specific guidance on token refreshing.
