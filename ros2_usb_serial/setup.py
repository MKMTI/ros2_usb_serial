from setuptools import setup

package_name = 'ros2_usb_serial'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'pyserial'],
    zip_safe=True,
    maintainer='unyka4',
    maintainer_email='unyka4@example.com',
    description='Pacote que comunica qualquer microcontrolador ligado ao USB via porta serial para ROS 2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'usb_serial = ros2_usb_serial.usb_serial:main',
            'usb_serial_save_txt = ros2_usb_serial.usb_serial_save_txt:main',
        ],
    },
)

