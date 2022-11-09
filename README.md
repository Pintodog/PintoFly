# Firefly Learning API
## Introduction
This is a library that provides an Python API for interacting with Firefly Learning servers.
This library handles authentication, downloading information such as timetable and tasks, marking tasks as done.

This API is designed for use by **students**, there isn't one for teachers currently.

Please see the documentation [here](https://fireflyapi.readthedocs.io/en/latest/).

## Example
See [examples](/examples) directory for more examples.
``` Python
import FireflyAPI

# Your school code is the word that you use to register your phone with Firefly.
school_code = "ABINGDON"
# This is your ASP.NET_SessionId cookie. See readme for guidance on this.
session_token = "hakqwhhekHHEKHhj3"
# You can name your integration if you want.
integration_name = "PintoFly"

# Create a new integration
integration = FireflyAPI.UserIntegration(school_code, session_token, integration_name)
authenticated_user = integration.create_integration()

# Now log in to Firefly and: Click your name on the top right -> Click Account Settings -> Click Apps.
# You should see your new integration in the list somewhere.
print(f"This is your Authentication Blob for '{integration_name}'. Keep it safe!")
print(authenticated_user.auth_blob)

# WARNING: If you run this script again, you will see another integration appear in your apps list!
# You only need to make an integration one, after that, you just need your Authentication Blob.

user_integration = FireflyAPI.AuthenticatedUser(integration.auth_blob)
print(f"My GUID is: {user_integration.guid}")

# !!! Remember to keep your authentication blob safe !!!. It can be used by anyone with access to it to log into your Firefly account.
``` 

