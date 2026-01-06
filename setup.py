from setuptools import setup
import os
from glob import glob

package_name = 'battery_notifier'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kaito Kubota',
    maintainer_email='kaitokubota@example.com',
    description='ROS 2 package to notify real-time battery status',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'battery_publisher = battery_notifier.battery_publisher:main',
            'warning_listener = battery_notifier.warning_listener:main',
        ],
    },
)
