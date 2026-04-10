from setuptools import setup


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname),
                encoding='utf-8').read()


setup(name='thermoencoder',
      version='0.1.2',
      description='Thermometer Encoding for ordinal variables',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='https://github.com/kmedian/thermoencoder',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['thermoencoder'],
      install_requires=[
          'setuptools>=78.1.1',
          'numpy>=1.19.0',
          'scikit-learn>=0.24.0'],
      python_requires='>=3.8',
      zip_safe=False)
