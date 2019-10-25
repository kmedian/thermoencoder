from setuptools import setup


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='thermoencoder',
      version='0.1.2',
      description='Thermometer Encoding for ordinal variables',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='http://github.com/kmedian/thermoencoder',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['thermoencoder'],
      install_requires=[
          'setuptools>=40.0.0',
          'nose>=1.3.7',
          'numpy>=1.14.5',
          'scikit-learn>=0.20.0'],
      python_requires='>=3.6',
      zip_safe=False)
