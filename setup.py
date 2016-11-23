from setuptools import setup, find_packages

setup(
    name='pubnubsub-handler',
    version='0.0.3',
    description='Handles the PubNub subscriptions between PubNub and Home-Assistant for Wink',
    author='William Scanlon',
    py_modules=['pubnubsubhandler'],
    license='MIT',
    install_requires=[
        'pycryptodomex>=3.3',
        'requests>=2.4',
        'pubnub==4.0.1'
    ],
    zip_safe=True
)
