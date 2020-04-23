from distutils.core import setup

with open('README.md') as file:
    readme = file.read()

with open('requirements.txt') as file:
    install_requires = file.readlines()


setup(
    name='chernobyl',
    version='0.1',
    packages=['chernobyl', 'chernobyl.new', 'chernobyl.new.controller'],
    package_data={
        "chernobyl": ["new/**", "new/controllers/**", "new/controllers/templates/**", "new/templates/**", "new/templates/.*", "new/templates/controllers/**", ],
    },
    include_package_data=True,
    install_requires=install_requires,
    url='',
    license='LICENSE.txt',
    description='',
    long_description=readme,
    author='Perry',
    author_email='perryism@gmail.com'
)
