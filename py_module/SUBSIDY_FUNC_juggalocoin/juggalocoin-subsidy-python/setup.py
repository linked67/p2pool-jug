from distutils.core import setup
from distutils.extension import Extension

setup(name="juggalocoin_subsidys",
    ext_modules=[
        Extension("juggalocoin_subsidy", ["juggalocoin_GetBlockBaseValue.cpp"],
        libraries = ["boost_python"])
    ])
