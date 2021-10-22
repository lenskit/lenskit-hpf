project = 'LensKit'
copyright = '2021 Boise State University'
author = 'Michael D. Ekstrand'

import lenskit_hpf

# The short X.Y version
version = '.'.join(lenskit_hpf.__version__.split('.')[:2])
# The full version, including alpha/beta/rc tags
release = lenskit_hpf.__version__

extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinxcontrib.bibtex',
    'sphinx_rtd_theme',
]

html_theme = 'sphinx_rtd_theme'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'pandas': ('http://pandas.pydata.org/pandas-docs/stable/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'hpfrec': ('https://hpfrec.readthedocs.io/en/latest/', None),
    'implicit': ('https://implicit.readthedocs.io/en/latest/', None),
    'scikit': ('https://scikit-learn.org/stable/', None),
    'binpickle': ('https://binpickle.lenskit.org/en/stable/', None),
    'csr': ('https://csr.lenskit.org/en/latest/', None),
    'seedbank': ('https://seedbank.lenskit.org/en/latest/', None),
    'lenskit': ('https://lkpy.lenskit.org/en/stable/', None)
}

autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'show-inheritance': True
}
