from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='juce',
      license='MIT',
      version='0.1.0',
      author='Tobias Hienzsch',
      author_email='tobanteAudio@gmail.com',
      description='Python binding for manipulating Projucer jucer files & projects',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/tobanteAudio/python-juce',
      packages=['juce'],
      zip_safe=False)
