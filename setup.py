from setuptools import find_packages
from setuptools import setup

package_name = 'ros2top'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['asciimatics', 'ros2cli', 'setuptools'],
    zip_safe=True,
    maintainer='Hironori Fujimoto',
    maintainer_email='broadbarredfirefish@gmail.com',
    url='https://github.com/fujimo-t/ros2top',
    description='Top-like interface as a ros2cli command',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'ros2cli.command': [
            'top = ros2top.command.top:TopCommand',
        ],
    },
)
