from setuptools import setup,find_packages

setup(
    name='twitter_auto',
    author='echo-vutsuak',
    version='1.1',
    long_description='This contains script to search for particular keywords from amongst the tweets ,'
                     ' and then auto like the tweet and auto follow the twiterrati and '
                     'also Unfollows the recently followed ',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask','tweepy']
)
