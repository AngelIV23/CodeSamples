from ncclient import manager


router = {"host": "sandbox-iosxe-latest-1.cisco.com", "port": "830",
          "username": "developer", "password": "C1sco12345"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    m.close_session()
