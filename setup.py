# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages
requirements = [
    'qrcode',
    'CRC-ITU'
]

setup(
    name='pypromptpay',
    version='0.4',
    description="PromptPay QR code in Python",
    author='Wannaphong Phatthiyaphaibun',
    author_email='wannaphong@kkumail.com',
    url='https://github.com/wannaphongcom/pypromptpay',
    packages=['.'],
    package_data={'': ['LICENSE','README.md']},
    include_package_data=True,
    install_requires=requirements,
    license='Apache Software License 2.0',
    zip_safe=False,
    keywords='promptpay',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: Implementation'],
)
