from setuptools import find_packages, setup

package_name = 'ros2_teleoperation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cdonoso',
    maintainer_email='clemente.donosok@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dashboard_viewer = ros2_teleoperation.main_window:main',
            'gpsmap_viewer = ros2_teleoperation.gps_map_window:main',
            'camera_viewer = ros2_teleoperation.camera_window:main',
            'lidar_viewer = ros2_teleoperation.lidar_window:main',
            'imu_viewer = ros2_teleoperation.imu_window:main',
            'plot_viewer = ros2_teleoperation.plot_window:main',
            'teleoperation_viewer = ros2_teleoperation.teleoperation_window:main',
            'gridmap_viewer = ros2_teleoperation.gridmap_window:main',
            'robotstate_viewer = ros2_teleoperation.robotstate_window:main',
        ],
    },
)
