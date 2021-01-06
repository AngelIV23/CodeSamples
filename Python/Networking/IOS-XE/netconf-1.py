from ncclient import manager

'''Warning: This code was ment for an Always-On device that is constanly changing in the public Devnet Sandbox. 
Refer to the documentation such as URL/Port/Username/Password in case it changes at: https://devnetsandbox.cisco.com/'''
          
router = {"host": "sandbox-iosxe-latest-1.cisco.com", "port": "830",
          "username": "developer", "password": "C1sco12345"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    m.close_session()
