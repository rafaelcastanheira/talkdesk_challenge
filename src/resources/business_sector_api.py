import requests
from src.resources.phone_number_info import PhoneNumberInfo


def set_business_sector(phone_info: PhoneNumberInfo):
    try:
        res = requests.get("https://challenge-business-sector-api.meza.talkdeskstg.com/sector/{}".format(phone_info.get_number()))
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    phone_info.set_sector(res.json()["sector"])