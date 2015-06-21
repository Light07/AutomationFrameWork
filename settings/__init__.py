__author__ = 'kevin'

from settings.test_config import  Environment
from settings.data_source import B2S

environment = Environment.LIVE

if environment == Environment.UAT:
    key = "UAT"
elif environment == Environment.QA:
    key = "QA"
elif environment == Environment.STG:
    key = "STG"
else:
    key = "LIVE"

BAI_DU_HOME = "http://%s.baidu.com" % environment
B2S_URL = "http://%s.englishtown.cn/partner/elab/?lng=en" % environment

invalid_user = B2S.login_verification_accounts[key]['invalid_user']
invalid_password = B2S.login_verification_accounts[key]['invalid_password']

blank_user = B2S.login_verification_accounts[key]['blank_user']
blank_password = B2S.login_verification_accounts[key]['blank_password']

expired_user = B2S.login_verification_accounts[key]['expired_user']
expired_password = B2S.login_verification_accounts[key]['expired_password']

