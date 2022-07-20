import hashlib

class Md5:
    def __init__(self):
        self.appid = "20220314001124419"
        self.q = ""
        self.salt = "123456"
        self.miyao = "erHgTdMxw2dUGAblCk05"

    def encry(self):
        self.text = self.appid + self.q + self.salt + self.miyao
        hl = hashlib.md5()
        hl.update(self.text.encode(encoding='utf8'))
        md5 = hl.hexdigest()
        return md5