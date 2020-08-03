"""
七牛云上传CDN
"""

from qiniu import Auth, put_file, etag
from os import path
from config import config

q = Auth(config['access_key'], config['secret_key'])


def upload_cdn(filepath):
    filename = path.basename(filepath)
    token = q.upload_token(config['bucket_name'], filename, 3600)

    ret, info = put_file(token, filename, filepath)
    assert ret['key'] == filename
    assert ret['hash'] == etag(filepath)
