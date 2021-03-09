"""Configuration settings for running the Python auth samples locally.

In a production deployment, this information should be saved in a database or
other secure storage mechanism.
"""

# Copyright (c) Microsoft Corporation. All rights reserved. Licensed under the MIT license.
# See LICENSE in the project root for license information.

CLIENT_ID = 'd4d2031d-f2c8-484a-9a81-7adf56970cbd'
CLIENT_SECRET = '~zuQGoc-6-1JA1vE_x_1jsp9-EL8FJ7TgE'
# REDIRECT_URI = 'http://localhost:5000/login/authorized'
REDIRECT_URI = 'https://2533e9da4af9.ngrok.io'


WEBHOOK_DATA = {'changeType': 'updated',
                # 'notificationUrl': 'https://{ ENTER_YOUR_NGROK_URL }/listen',
                'notificationUrl': 'https://2533e9da4af9.ngrok.io/listen',
                'resource': 'security/alerts',
                'clientState': 'cLIENTsTATEfORvALIDATION'}

# AUTHORITY_URL ending determines type of account that can be authenticated:
# /organizations = organizational accounts only
# /consumers = MSAs only (Microsoft Accounts - Live.com, Hotmail.com, etc.)
# /common = allow both types of accounts
AUTHORITY_URL = 'https://login.microsoftonline.com/common'

AUTH_ENDPOINT = '/oauth2/v2.0/authorize'
TOKEN_ENDPOINT = '/oauth2/v2.0/token'

RESOURCE = 'https://graph.microsoft.com/'
API_VERSION = 'v1.0'
SECURITYAPI_VERSION = 'v1.0'
SECURESCORE_VERSION = 'v1.0'
SECURITYACTION_VERSION = 'beta'
SECURITYAPI_URL = RESOURCE + SECURITYAPI_VERSION + '/security/'
SCOPES = ['User.Read', 'SecurityEvents.ReadWrite.All']  # Add other scopes/permissions as needed.

# This code can be removed after configuring CLIENT_ID and CLIENT_SECRET above.
if 'ENTER_YOUR' in CLIENT_ID or 'ENTER_YOUR' in CLIENT_SECRET:
    print('ERROR: config.py does not contain valid CLIENT_ID and CLIENT_SECRET')
    import sys
    sys.exit(1)
