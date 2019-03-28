from frogtips import constants
from frogtips.api import Tip, Credentials
import requests
import json
from io import StringIO
import sys
from pathlib import Path
import os


class Tips:
    """This class holds random FROG tips as downloaded from the API server."""
    tips = []

    def get_next_tip(self):
        """Load tips from disk, return the next tip, and save the remainder.

        If there are no tips left on disk (or if this is a new tip file),
        download more tips from frog.tips"""
        self.load_tips()
        if self.tips == []:
            self.download_random_tips()
            self.load_tips()

        next_tip = self.tips.pop()
        self.save_tips()
        return next_tip

    def save_tips(self):
        """Save tips from memory (self.tips) to disk."""
        try:
            file = open(constants.TIPS_FILE, 'w')
        except OSError:
            sys.exit("Couldn't open tips file %s for writing" %
                     constants.TIPS_FILE)

        tips_string = ''
        for tip in self.tips:
            tips_string += tip.serialize() + "\n"

        file.write(tips_string)
        file.close()

    def load_tips(self):
        """Load tips from disk into memory. If there are no tips on disk,
        download more tips from the API server."""

        # Create file if it does not already exist
        if not Path(constants.CREDENTIALS_FILE).is_file():
            if not Path(constants.FROG_TIPS_DIR).is_dir():
                self.init_tips_dir()
            self.init_tips_file()

        # Create file if it does not already exist
        if not Path(constants.TIPS_FILE).is_file():
            self.init_tips_file()
        try:
            file = open(constants.TIPS_FILE)
        except OSError:
            sys.exit("Couldn't open tips file %s" %
                     constants.TIPS_FILE)

        temp_tips = file.read().split("\n")
        file.close()

        # Decode tips and load them into self.tips, skipping any blank lines to
        # avoid JSON decode errors.
        self.tips = []

        for tip in temp_tips:
            if tip == '':
                break
            decoded_tip = json.loads(tip)
            temp_tip = Tip(decoded_tip['id'],decoded_tip['tip'])
            self.tips.append(temp_tip)

        # if self.tips is still empty, it means the file was out of tips.
        if self.tips == []:
            self.download_random_tips()
            self.load_tips()

    def init_tips_file(self):
        """Create a blank file at [constants.TIPS_FILE]"""
        try:
            file = open(constants.TIPS_FILE, 'w')
        except OSError:
            sys.exit("Couldn't create file %s" % constants.TIPS_FILE)
        file.write('')
        file.close()

    def init_tips_dir(self):
        """Create a directory at [constants.FROG_TIPS_DIR]."""
        if Path(constants.FROG_TIPS_DIR).is_dir():
            return
        try:
            os.mkdir(constants.FROG_TIPS_DIR)
        except OSError:
            sys.exit("Couldn't create directory %s" %
                     constants.FROG_TIPS_DIR)

    def download_random_tips(self):
        """Download random tips from the API server and save them to disk."""
        credentials = Credentials()
        url = 'https://' + constants.FROG_TIPS_DOMAIN + '/api/3/tips'
        headers = {'Content-type': 'application/json',
                   'Accept': 'application/json',
                   'Authorization': 'Basic ' +
                                    credentials.get_http_basic_auth()}
        response = requests.get(url=url,
                                headers=headers)

        # Just look at this nonsense!
        temp_tips = json.load(StringIO(str(response.content.decode('utf-8'))))

        for tip in temp_tips:
            temp_tip = Tip(tip['id'],tip['tip'])
            self.tips.append(temp_tip)

        self.save_tips()