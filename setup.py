import os
import setuptools
from setuptools import Distribution

DOC_STUB_IMPORTS = [
    'hpfrec'
]
BUILDING_DOCS = 'READTHEDOCS' in os.environ


class LKExtDist(Distribution):
    def _finalize_requires(self):
        if self.install_requires and BUILDING_DOCS:
            i = 0
            while i < len(self.install_requires):
                req = self.install_requires[i]
                if req in DOC_STUB_IMPORTS:
                    del self.install_requires[i]
                else:
                    i += 1
        super()._finalize_requires()


setuptools.setup(distclass=LKExtDist)
