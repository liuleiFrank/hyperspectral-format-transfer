from setuptools import setup

setup(
    author="Liulei",
    author_email="1760840620@qq.com",
    name="hyperspectral-mat2lan",
    version="0.1.0",
    license="MIT",
    py_modules=['GenLan','osgeo','numpy'],
    description="transform .mat to .lan hyperspecral file",
    entry_points={
        'console_scripts':['m2l=GenLan:command_line_runner']
    }
)
