import base64
from io import BytesIO
import json
import requests
from PIL import Image

from .captcha import Captcha
from ..config import BaseConfig
from .._internal import absp

class APIConfig(object):

    _DEFAULT_CONFIG_PATH = '../apikey.json'

    def __init__(self, path=_DEFAULT_CONFIG_PATH):
        with open(absp(path), 'r') as handle:
            self._apikey = json.load(handle)
        assert 'username' in self._apikey.keys() and 'password' in self._apikey.keys()

    @property
    def uname(self):
        return self._apikey['username']

    @property
    def pwd(self):
        return self._apikey['password']


class TTShituRecognizer(object):

    _RECOGNIZER_URL = "http://api.ttshitu.com/base64"

    def __init__(self):
        self._config = APIConfig()
        
    def recognize(self, raw):
        encode = TTShituRecognizer._to_b64(raw)
        data = {
            "username": self._config.uname, 
            "password": self._config.pwd,
            "image": encode
        }
        result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
        if result["success"]:
            return Captcha(result["data"]["result"], None, None, None, None)
        else: # fail
            return Captcha(-1, result["message"], None, None, None)

    def _to_b64(raw):
        im = Image.open(BytesIO(raw))
        if im.is_animated:
            oim = im
            oim.seek(oim.n_frames-1)
            im = Image.new('RGB', oim.size)
            im.paste(oim)
        buffer = BytesIO()
        im.save(buffer, format='JPEG')
        b64 = base64.b64encode(buffer.getvalue()).decode()
        return b64