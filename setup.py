from setuptools import setup, find_packages

install_requires = []
dependency_links = []
with open('requirements.txt') as reader:
    for line in reader:
        line = line.strip()
        if line.startswith('git+'):
            dependency_links.append(line)
        else:
            install_requires.append(line)

setup(
    name='botbuddy',
    version='0.0.1',
    pymodules=['botbuddy.bot'],
    description='Simple Twitter Bot Tool',
    packages=find_packages(),
    package_data={'': ['*.yaml', '*.json']},
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
    setup_requires=['flake8'],
    entry_points='''
        [console_scripts]
        random_retweet=botbuddy.main:random_retweet
        twitter_query=botbuddy.main:query_twitter
    ''',
)
