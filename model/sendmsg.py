from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sms.v20190711 import sms_client, models
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
import random
import json


class Send:
    def __init__(self):
        self.phone_number = ""

    def random(self):
        number = random.randint(1000, 9999)
        return str(number)

    def sendMessage(self):
        try:
            # 这部分做修改，自己的appid和appkey
            cred = credential.Credential("appid", "appkey")
            client = sms_client.SmsClient(cred, "ap-guangzhou")
            req = models.SendSmsRequest()
            req.SmsSdkAppid = "1400653965"
            req.Sign = "找Bug"
            req.PhoneNumberSet = ["+86"+self.phone_number]
            req.TemplateID = "1459276"
            self.check_code = self.random()
            req.TemplateParamSet = [self.check_code, "2"]
            resp = client.SendSms(req)
            self.code = json.loads(resp.to_json_string(indent=2))["SendStatusSet"][0]["Code"]
            print(json.loads(resp.to_json_string(indent=2))["SendStatusSet"][0]["Code"])
        except TencentCloudSDKException as err:
            print(err)


if __name__ == '__main__':
    send = Send()
    send.sendMessage()
