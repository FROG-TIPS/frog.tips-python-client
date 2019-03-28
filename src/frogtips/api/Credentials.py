import requests
from uuid import UUID, uuid4
from pathlib import Path
from frogtips import constants
import os
import sys
import json
import base64


class Credentials:
    """A class for your FROG TIPS API Credentials."""

    username = ''
    uuid = ''
    phrase = ''

    def __init__(self, username = ''):
        """Loads credentials from disk.

        Adds a name if one is provided and none exists currently. Generates a
        new key if none exists."""

        self.load_credentials()

        if (self.get_username() == '') & (username != ''):
            self.set_username(username)
            self.register(True)
            print("You have added \"" + username +
                  "\" as your API key username. You may now submit tips.")

        if self.get_phrase() == '':
            self.register()

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_phrase(self):
        return self.phrase

    def set_phrase(self, phrase):
        self.phrase = phrase

    def get_http_basic_auth(self):
        """Encodes uuid and phrase into the HTTP Basic auth string"""
        credential_string = self.get_uuid() + ':' + self.get_phrase()
        credential_bytes = credential_string.encode("utf-8")
        return base64.standard_b64encode(credential_bytes).decode('utf-8')

    def get_uuid(self):
        return str(self.uuid)

    def set_uuid(self, uuid):
        self.uuid = uuid

    def gen_random_uuid(self):
        """Populates self.uuid with a random uuid (uuid version 4)"""
        self.uuid = uuid4()

    def validate_uuid4(self, uuid_string):
        """Takes a uuid version 4 string and attempts to validate it"""
        try:
            value = UUID(uuid_string, version=4)
        except ValueError:
            return False

        if str(value).lower() == uuid_string.lower():
            return True
        else:
            return False

    def init_credentials_dir(self):
        if Path(constants.FROG_TIPS_DIR).is_dir():
            return
        try:
            os.mkdir(constants.FROG_TIPS_DIR)
        except OSError:
            sys.exit("Couldn't create directory %s" %
                     constants.FROG_TIPS_DIR)

    def load_credentials(self):
        """Loads credentials from disk.

        Creates the credentials file if it does not already exist, and
        populates self.username, self.uuid, and self.phrase"""

        # Create file if it does not already exist
        if not Path(constants.CREDENTIALS_FILE).is_file():
            if not Path(constants.FROG_TIPS_DIR).is_dir():
                self.init_credentials_dir()
            self.init_credentials_file()

        # Attempt to open file
        try:
            file = open(constants.CREDENTIALS_FILE)
        except OSError:
            sys.exit("Couldn't open credentials file %s" %
                     constants.CREDENTIALS_FILE)

        # Read and close file
        credentials = file.read().split(':')
        file.close()

        username = credentials[0]
        uuid = credentials[1]
        phrase = credentials[2]

        if uuid == '':
            self.gen_random_uuid()
            self.save_credentials()
        else:
            if self.validate_uuid4(uuid):
                self.set_username(username)
                self.set_uuid(uuid)
                self.set_phrase(phrase)
            else:
                self.init_credentials_file()
                self.load_credentials()

    def init_credentials_file(self):
        """Create credentials file and/or wipe the existing one clean."""
        try:
            file = open(constants.CREDENTIALS_FILE, 'w')
        except OSError:
            sys.exit("Couldn't create file %s" % constants.CREDENTIALS_FILE)
        file.write('::')
        file.close()

    def save_credentials(self):
        """Save credentials to disk."""
        credentials = self.get_username() + ':' + \
                      self.get_uuid() + ':' + \
                      self.get_phrase()

        try:
            file = open(constants.CREDENTIALS_FILE, 'w')
        except OSError:
            sys.exit("Couldn't open credentials file %s for writing" %
                     constants.CREDENTIALS_FILE)

        file.write(credentials)
        file.close()

    def serialize(self):
        """Export uuid, comment, and name for registration with API server."""
        temp_credentials = {}
        temp_credentials['uuid'] = self.get_uuid()
        temp_credentials['comment'] = constants.APPLICATION_NAME + ' ' + \
            constants.VERSION
        if not self.get_username() == '':
            temp_credentials['name'] = self.get_username()
        return json.dumps(temp_credentials)

    def register(self, force_registration = False):
        """Register with the API server in order to create an API key.

        Registers the uuid and user name with the API server in order to
        create an API key. Unless force_registration is set to True, will
        return immediately if there's already a secret phrase populated in
        self.phrase (indicating a complete API key),  Saves the key to disk
        upon successful completion."""

        # If there's already an API key on disk, refuse to go any further
        # unless force_registration is set to True.
        if not force_registration:
            if not self.get_phrase() == '':
                return

        # Prepare request
        url = 'https://' + constants.FROG_TIPS_DOMAIN + '/api/3/auth'
        http_headers = {'Content-type': 'application/json',
                        'Accept': 'application/json'}

        # Post request
        response = requests.post(url=url,
                          data=self.serialize(),
                          headers=http_headers)

        # Decode and save API key
        self.set_phrase(response.json()['phrase'])
        self.save_credentials()

    def get_permissions(self):
        """Gets current permissions from the API server. Returns list of
        permissions as an array."""
        credentials = Credentials()

        url = 'https://' + constants.FROG_TIPS_DOMAIN + '/api/3/auth/view'
        http_headers = {'Content-type': 'application/json',
                        'Accept': 'application/json',
                        'Authorization': 'Basic ' +
                                         credentials.get_http_basic_auth()}
        response = requests.get(url=url,
                          headers=http_headers)

        permissions = response.json()['perms']
        return permissions

    def get_key_id(self):
        """Gets your API key ID from the API server. Returns as an int."""
        credentials = Credentials()

        url = 'https://' + constants.FROG_TIPS_DOMAIN + '/api/3/auth/view'
        http_headers = {'Content-type': 'application/json',
                        'Accept': 'application/json',
                        'Authorization': 'Basic ' +
                                         credentials.get_http_basic_auth()}
        response = requests.get(url=url,
                          headers=http_headers)

        id = response.json()['id']
        return id