from setuptools import setup, find_packages

setup(
    name             = 'preview-card',
    version          = '1.0.0',
    description      = 'Anyone can obtain data(url, image, title, description, etc) easily from plain text for showing preview card like Twitter, Facebook newsfeed',
    long_description = open('README.md').read(),
    author           = 'Jaewoong',
    author_email     = 'jaewoong.go@gmail.com',
    url              = 'https://github.com/jwkcp/django-preview-card',
    download_url     = 'https://github.com/jwkcp/django-preview-card/#files',
    install_requires = ['beautifulsoup4', 'requests', ],
    packages         = find_packages(exclude = ['docs', 'example']),
    keywords         = ['django', 'cardview', 'newsfeed'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
