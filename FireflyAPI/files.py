from FireflyAPI import utils
from FireflyAPI.authentication import *
import os
import requests
import json


class File:
    def __init__(self, file_data, portal):
        self.resource_id = file_data["resourceId"]
        self.fileName = file_data["fileName"]
        self.fileType = file_data["fileType"]
        self.etag = file_data["etag"]
        self.date_created = utils.firefly_timestamp_to_date_time(file_data["dateCreated"])
        self.portal = portal

    @property
    def interactive_download_url(self):
        return f"https://{self.portal}/resource-download.aspx?id={self.resource_id}"

    @property
    def download_url(self):
        return f"https://{self.portal}/resource.aspx?id={self.resource_id}"


class FileUpload:
    def __init__(self, file_path, file_name=None):
        self.file_path = file_path
        if file_name is None:
            self.file_name = os.path.basename(file_path)


class FileFolder(DiscretelyAuthenticatedObject):
    """
    The FileFolder object is used to start a file submission for a task.
    Args:
        auth_blob (str): This is generated by the UserIntegration class, and is used to authenticate as a user.
    """
    def __init__(self, auth_blob):
        DiscretelyAuthenticatedObject.__init__(self, auth_blob)
        params = {"ffauth_device_id": self._DiscretelyAuthenticatedObject__device_id,
                  "ffauth_secret": self._DiscretelyAuthenticatedObject__device_token}
        response = requests.post(self._DiscretelyAuthenticatedObject__portal + "/createTempFolder",
                                 params=params)
        response = json.loads(response.text)
        self.folder_id = response["id"]
        self.email = response["emailUpload"]

    def upload_file(self, file, file_name=None):
        if(file_name == None):
            file_name = os.path.basename(file.name)
        params = {"ffauth_device_id": self._DiscretelyAuthenticatedObject__device_id,
                  "ffauth_secret": self._DiscretelyAuthenticatedObject__device_token}
        response = requests.post(self._DiscretelyAuthenticatedObject__portal + f"/folders/{self.folder_id}/files",
                                 params=params, files={'file': (file_name, file, 'application/octet-stream')})
        response = json.loads(response.text)
        print(response)
