from setuptools import setup

package_name = 'line_follower'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/simulate.launch.py']),
        ('share/' + package_name + '/urdf', ['urdf/line_follower.urdf']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='thanuja',
    maintainer_email='thanuja@todo.todo',
    description='Line Follower Robot simulation',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'line_follower_node = line_follower.line_follower_node:main',
        ],
    },
)

