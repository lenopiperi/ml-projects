from flask import Flask
import os
import cloudstorage
from google.appengine.api import app_identity

#get default bucket name
def get(self):
    bucket_name = os.environ.get(
        'BUCKET_NAME', app_identity.get_default_gcs_bucket_name())

    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write(
        'Demo GCS Application running from Version: {}\n'.format(
            os.environ['CURRENT_VERSION_ID']))
    self.response.write('Using bucket name: {}\n\n'.format(bucket_name))


UPLOAD_FOLDER = 'C:/Users/lpiperi/Desktop'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024