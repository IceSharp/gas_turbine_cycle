from distutils.core import setup

setup(
    name='gas_turbine_cycle',
    version='0.0.1',
    packages=['gas_turbine_cycle', 'gas_turbine_cycle.core', 'gas_turbine_cycle.tools', 'gas_turbine_cycle.templates'],
    package_data={'gas_turbine_cycle': ['templates/2N.tex', 'templates/equipment.tex']},
    url='',
    license='',
    author='Alexander Zhigalkin',
    author_email='aszhigalkin@gmail.com',
    description='Library for computation of gas turbine cycle'
)
