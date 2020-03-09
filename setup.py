from distutils.core import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'Bulkren',         # How you named your package folder (MyLib)
  packages = ['Bulkren'],   # Chose the same as "name"
  version = '1.0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Bulkren can reduce your finger pains, just rename files in bulk',   # Give a short description about your library
  author = 'Akash Srivastava',                   # Type in your name
  author_email = 'sriakash.dev@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Dev-Akash/Bulkren',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Dev-Akash/Bulkren/archive/v1.0.3.tar.gz',    # I explain this later on
  keywords = ['rename files', 'bulk rename', 'rename', 'rename files in bulk', 'bulk', 'rename', 'files', 'all', '.pdf', '.txt', '.jpg'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'tqdm',
          'argparse',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  long_description=long_description,
  long_description_content_type='text/markdown',
)