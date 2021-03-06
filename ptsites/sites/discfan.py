from ..site_base import SiteBase
from ..nexusphp import NexusPHP

# auto_sign_in
URL = 'https://discfan.net/attendance.php'
SUCCEED_REGEX = '這是您的第 .* 次簽到，已連續簽到 .* 天，本次簽到獲得 .* 個魔力值。|您今天已經簽到過了，請勿重複刷新。'


class MainClass(NexusPHP):
    @staticmethod
    def build_sign_in(entry, config):
        SiteBase.build_sign_in_entry(entry, config, URL, SUCCEED_REGEX)

    def build_selector(self):
        selector = super(MainClass, self).build_selector()
        selector['details']['hr'] = {
            'regex': '(H&R).*?(\\d+)',
            'group': 2,
        }
        return selector
