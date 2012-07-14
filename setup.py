from setuptools import setup
import newpasswd

setup(
    name='newpasswd',
    version=newpasswd.__version__,
    author='Simonas Kazlauskas',
    url='https://github.com/simukis/newpasswd',
    description='Generate a brand new password',
    packages=[],
    scripts=['newpasswd'],
    zip_safe=False
    )
