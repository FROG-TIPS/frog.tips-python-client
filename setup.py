from setuptools import setup, find_namespace_packages
from src.frogtips import constants

setup(name='frogtips',
      package_dir={'': 'src'},
      packages=find_namespace_packages(where='src'),
      #packages=["frogtips",
      #          "frogtips.api"],
      entry_points={"console_scripts": ['frogtips = frogtips.__main__:main']},
      version=constants.VERSION,
      description=constants.SHORT_DESCRIPTION,
      long_description=constants.LONG_DESCRIPTION,
      url='https://' + constants.FROG_TIPS_DOMAIN + '/',
      author='FROG Systems, Inc.',
      author_email='admin@frog.tips',
      license="MIT",
      install_requires=[
            'requests'
      ],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
      ])