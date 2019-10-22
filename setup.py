from setuptools import setup, find_packages

print(find_packages())

setup (
       name='tlcc',
       description = 'Colony count with transfer learning',
       version='0.1',
       packages=find_packages(),
       install_requires=['argh', 'h5py', 'matplotlib'],
       data_files=[],
       classifiers=[
              'Development Status :: 3 - Alpha']
)
