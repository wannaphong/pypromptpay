# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages
requirements = [
    'qrcode',
    'CRC-ITU',
    'crc16'
]
with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name='pypromptpay',
    version='0.5.2',
    description="PromptPay QR code in Python",
    author='Wannaphong Phatthiyaphaibun',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='wannaphong@kkumail.com',
    url='https://github.com/wannaphong/pypromptpay',
    packages=['.'],
    package_data={'': ['LICENSE','README.md']},
    include_package_data=True,
    test_suite="test",
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
