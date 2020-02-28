# pypromptpay

[![Build Status](https://travis-ci.org/wannaphong/pypromptpay.svg?branch=master)](https://travis-ci.org/wannaphong/pypromptpay)

QR Code PromptPay in Python 3.

## Install

```
pip install pypromptpay
```

## Using

```python
from pypromptpay import qr_code
qr_code(account,one_time=True,path_qr_code="",country="TH",money="",currency="THB")
```

- account is phone number or  identification number.
- one_time : if you use once than it's True.
- path_qr_code : path save file qr code image.
- country : TH
- money : money (if have)
- currency : THB

return True (if have path_qr_code) or text (if haven't path_qr_code)

## License

Apache Software License 2.0



## Develop

Wannaphong Phatthiyaphaibun (wannaphong@kkumail.com)
