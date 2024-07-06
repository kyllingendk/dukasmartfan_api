"""Setup of the dukasmartfan_api module."""

from setuptools import setup

setup(
    name="dukasmartfan_api",
    version="1.1.0",
    description="Duka One ventilation SDK entended",
    long_description=(
        "SDK for connection to the Duka One S6W ventilation. "
        "Made for interfacing to home assistant"
    ),
    author="Jens Østergaard Nielsen, Lars Laugesen",
    url="https://github.com/kyllingendk/dukasmartfan_api",
    packages=["dukasmartfan_api"],
    license="GPL-3.0",
)
