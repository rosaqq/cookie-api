from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='realcookie',
      version='0.1',
      description="Benolot's cookie API, python version",
      long_description='This module allows you to save cookies from a URL to a folder and then provides you with the path to a random image in that folder',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5.1',
      ],
      url='https://github.com/benolot/cookie-api/tree/python',
      author='secknv',
      license='MIT',
      packages=['realcookie'],
      include_package_data=True,
      zip_safe=False)
