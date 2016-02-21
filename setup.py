from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='realcookie',
      version='1.0.6',
      description="Benolot's cookie API, python version",
      long_description='This module allows you to save cookie images from a URL to a folder and then provides you with the path to a random image in that folder.',
      url='https://github.com/secknv/cookie-api',
      author='secknv',
      license='MIT',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
      packages=['realcookie'],
      include_package_data=True,
      zip_safe=False)
