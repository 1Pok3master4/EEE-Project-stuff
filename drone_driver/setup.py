from setuptools import find_packages, setup

package_name = 'drone_driver'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy',],
    zip_safe=True,
    maintainer='mocha1410',
    maintainer_email='amogha_ss@ph.iitr.ac.in',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "drone_controller = drone_driver.attempt_at_control:main",
            "test = drone_driver.test:main",
        ],
    },
)
