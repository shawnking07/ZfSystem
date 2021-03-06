from setuptools import setup

setup(
    name='ZfSystem',
    version='0.1',
    packages=['venv.lib.python3.6.distutils', 'venv.lib.python3.6.encodings', 'venv.lib.python3.6.importlib',
              'venv.lib.python3.6.collections', 'venv.lib.python3.6.site-packages.PIL',
              'venv.lib.python3.6.site-packages.pip', 'venv.lib.python3.6.site-packages.pip.req',
              'venv.lib.python3.6.site-packages.pip.vcs', 'venv.lib.python3.6.site-packages.pip.utils',
              'venv.lib.python3.6.site-packages.pip.compat', 'venv.lib.python3.6.site-packages.pip.models',
              'venv.lib.python3.6.site-packages.pip._vendor', 'venv.lib.python3.6.site-packages.pip._vendor.distlib',
              'venv.lib.python3.6.site-packages.pip._vendor.distlib._backport',
              'venv.lib.python3.6.site-packages.pip._vendor.colorama',
              'venv.lib.python3.6.site-packages.pip._vendor.html5lib',
              'venv.lib.python3.6.site-packages.pip._vendor.html5lib._trie',
              'venv.lib.python3.6.site-packages.pip._vendor.html5lib.filters',
              'venv.lib.python3.6.site-packages.pip._vendor.html5lib.treewalkers',
              'venv.lib.python3.6.site-packages.pip._vendor.html5lib.treeadapters',
              'venv.lib.python3.6.site-packages.pip._vendor.html5lib.treebuilders',
              'venv.lib.python3.6.site-packages.pip._vendor.lockfile',
              'venv.lib.python3.6.site-packages.pip._vendor.progress',
              'venv.lib.python3.6.site-packages.pip._vendor.requests',
              'venv.lib.python3.6.site-packages.pip._vendor.requests.packages',
              'venv.lib.python3.6.site-packages.pip._vendor.requests.packages.chardet',
              'venv.lib.python3.6.site-packages.pip._vendor.requests.packages.urllib3',
              'venv.lib.python3.6.site-packages.pip._vendor.requests.packages.urllib3.util',
              'venv.lib.python3.6.site-packages.pip._vendor.requests.packages.urllib3.contrib',
              'venv.lib.python3.6.site-packages.pip._vendor.requests.packages.urllib3.packages',
              'venv.lib.python3.6.site-packages.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
              'venv.lib.python3.6.site-packages.pip._vendor.packaging',
              'venv.lib.python3.6.site-packages.pip._vendor.cachecontrol',
              'venv.lib.python3.6.site-packages.pip._vendor.cachecontrol.caches',
              'venv.lib.python3.6.site-packages.pip._vendor.webencodings',
              'venv.lib.python3.6.site-packages.pip._vendor.pkg_resources',
              'venv.lib.python3.6.site-packages.pip.commands', 'venv.lib.python3.6.site-packages.pip.operations',
              'venv.lib.python3.6.site-packages.idna', 'venv.lib.python3.6.site-packages.lxml',
              'venv.lib.python3.6.site-packages.lxml.html', 'venv.lib.python3.6.site-packages.lxml.includes',
              'venv.lib.python3.6.site-packages.lxml.isoschematron', 'venv.lib.python3.6.site-packages.numpy',
              'venv.lib.python3.6.site-packages.numpy.ma', 'venv.lib.python3.6.site-packages.numpy.doc',
              'venv.lib.python3.6.site-packages.numpy.fft', 'venv.lib.python3.6.site-packages.numpy.lib',
              'venv.lib.python3.6.site-packages.numpy.core', 'venv.lib.python3.6.site-packages.numpy.f2py',
              'venv.lib.python3.6.site-packages.numpy.compat', 'venv.lib.python3.6.site-packages.numpy.linalg',
              'venv.lib.python3.6.site-packages.numpy.random', 'venv.lib.python3.6.site-packages.numpy.testing',
              'venv.lib.python3.6.site-packages.numpy.distutils',
              'venv.lib.python3.6.site-packages.numpy.distutils.command',
              'venv.lib.python3.6.site-packages.numpy.distutils.fcompiler',
              'venv.lib.python3.6.site-packages.numpy.matrixlib', 'venv.lib.python3.6.site-packages.numpy.polynomial',
              'venv.lib.python3.6.site-packages.scipy', 'venv.lib.python3.6.site-packages.scipy.io',
              'venv.lib.python3.6.site-packages.scipy.io.arff', 'venv.lib.python3.6.site-packages.scipy.io.arff.tests',
              'venv.lib.python3.6.site-packages.scipy.io.tests', 'venv.lib.python3.6.site-packages.scipy.io.matlab',
              'venv.lib.python3.6.site-packages.scipy.io.matlab.tests',
              'venv.lib.python3.6.site-packages.scipy.io.harwell_boeing',
              'venv.lib.python3.6.site-packages.scipy.io.harwell_boeing.tests',
              'venv.lib.python3.6.site-packages.scipy.odr', 'venv.lib.python3.6.site-packages.scipy.odr.tests',
              'venv.lib.python3.6.site-packages.scipy._lib', 'venv.lib.python3.6.site-packages.scipy._lib.tests',
              'venv.lib.python3.6.site-packages.scipy.misc', 'venv.lib.python3.6.site-packages.scipy.misc.tests',
              'venv.lib.python3.6.site-packages.scipy.stats', 'venv.lib.python3.6.site-packages.scipy.stats.tests',
              'venv.lib.python3.6.site-packages.scipy.linalg', 'venv.lib.python3.6.site-packages.scipy.linalg.tests',
              'venv.lib.python3.6.site-packages.scipy.signal', 'venv.lib.python3.6.site-packages.scipy.signal.tests',
              'venv.lib.python3.6.site-packages.scipy.sparse', 'venv.lib.python3.6.site-packages.scipy.sparse.tests',
              'venv.lib.python3.6.site-packages.scipy.sparse.linalg',
              'venv.lib.python3.6.site-packages.scipy.sparse.linalg.eigen',
              'venv.lib.python3.6.site-packages.scipy.sparse.linalg.eigen.arpack',
              'venv.lib.python3.6.site-packages.scipy.sparse.linalg.eigen.arpack.tests',
              'venv.lib.python3.6.site-packages.scipy.sparse.linalg.eigen.lobpcg',
              'venv.lib.python3.6.site-packages.scipy.sparse.linalg.eigen.lobpcg.tests',
              'venv.lib.python3.6.site-packages.scipy.sparse.linalg.tests',
              'venv.lib.python3.6.site-packages.scipy.sparse.linalg.dsolve',
              'venv.lib.python3.6.site-packages.scipy.sparse.linalg.dsolve.tests',
              'venv.lib.python3.6.site-packages.scipy.sparse.linalg.isolve',
              'venv.lib.python3.6.site-packages.scipy.sparse.linalg.isolve.tests',
              'venv.lib.python3.6.site-packages.scipy.sparse.csgraph',
              'venv.lib.python3.6.site-packages.scipy.sparse.csgraph.tests',
              'venv.lib.python3.6.site-packages.scipy.cluster', 'venv.lib.python3.6.site-packages.scipy.cluster.tests',
              'venv.lib.python3.6.site-packages.scipy.fftpack', 'venv.lib.python3.6.site-packages.scipy.fftpack.tests',
              'venv.lib.python3.6.site-packages.scipy.ndimage', 'venv.lib.python3.6.site-packages.scipy.ndimage.tests',
              'venv.lib.python3.6.site-packages.scipy.spatial', 'venv.lib.python3.6.site-packages.scipy.spatial.tests',
              'venv.lib.python3.6.site-packages.scipy.special', 'venv.lib.python3.6.site-packages.scipy.special.tests',
              'venv.lib.python3.6.site-packages.scipy.special._precompute',
              'venv.lib.python3.6.site-packages.scipy.optimize', 'venv.lib.python3.6.site-packages.scipy.optimize._lsq',
              'venv.lib.python3.6.site-packages.scipy.optimize.tests',
              'venv.lib.python3.6.site-packages.scipy.optimize._trlib',
              'venv.lib.python3.6.site-packages.scipy.constants',
              'venv.lib.python3.6.site-packages.scipy.constants.tests',
              'venv.lib.python3.6.site-packages.scipy.integrate',
              'venv.lib.python3.6.site-packages.scipy.integrate._ivp',
              'venv.lib.python3.6.site-packages.scipy.integrate.tests',
              'venv.lib.python3.6.site-packages.scipy.interpolate',
              'venv.lib.python3.6.site-packages.scipy.interpolate.tests',
              'venv.lib.python3.6.site-packages.scipy._build_utils', 'venv.lib.python3.6.site-packages.wheel',
              'venv.lib.python3.6.site-packages.wheel.tool', 'venv.lib.python3.6.site-packages.wheel.signatures',
              'venv.lib.python3.6.site-packages.certifi', 'venv.lib.python3.6.site-packages.chardet',
              'venv.lib.python3.6.site-packages.chardet.cli', 'venv.lib.python3.6.site-packages.olefile',
              'venv.lib.python3.6.site-packages.pyquery', 'venv.lib.python3.6.site-packages.sklearn',
              'venv.lib.python3.6.site-packages.sklearn.svm', 'venv.lib.python3.6.site-packages.sklearn.svm.tests',
              'venv.lib.python3.6.site-packages.sklearn.tree', 'venv.lib.python3.6.site-packages.sklearn.tree.tests',
              'venv.lib.python3.6.site-packages.sklearn.tests', 'venv.lib.python3.6.site-packages.sklearn.utils',
              'venv.lib.python3.6.site-packages.sklearn.utils.tests',
              'venv.lib.python3.6.site-packages.sklearn.utils.sparsetools',
              'venv.lib.python3.6.site-packages.sklearn.utils.sparsetools.tests',
              'venv.lib.python3.6.site-packages.sklearn.cluster',
              'venv.lib.python3.6.site-packages.sklearn.cluster.tests',
              'venv.lib.python3.6.site-packages.sklearn.metrics',
              'venv.lib.python3.6.site-packages.sklearn.metrics.tests',
              'venv.lib.python3.6.site-packages.sklearn.metrics.cluster',
              'venv.lib.python3.6.site-packages.sklearn.metrics.cluster.tests',
              'venv.lib.python3.6.site-packages.sklearn.mixture',
              'venv.lib.python3.6.site-packages.sklearn.mixture.tests',
              'venv.lib.python3.6.site-packages.sklearn.datasets',
              'venv.lib.python3.6.site-packages.sklearn.datasets.tests',
              'venv.lib.python3.6.site-packages.sklearn.ensemble',
              'venv.lib.python3.6.site-packages.sklearn.ensemble.tests',
              'venv.lib.python3.6.site-packages.sklearn.manifold',
              'venv.lib.python3.6.site-packages.sklearn.manifold.tests',
              'venv.lib.python3.6.site-packages.sklearn.externals',
              'venv.lib.python3.6.site-packages.sklearn.externals.joblib',
              'venv.lib.python3.6.site-packages.sklearn.neighbors',
              'venv.lib.python3.6.site-packages.sklearn.neighbors.tests',
              'venv.lib.python3.6.site-packages.sklearn.covariance',
              'venv.lib.python3.6.site-packages.sklearn.covariance.tests',
              'venv.lib.python3.6.site-packages.sklearn._build_utils',
              'venv.lib.python3.6.site-packages.sklearn.linear_model',
              'venv.lib.python3.6.site-packages.sklearn.linear_model.tests',
              'venv.lib.python3.6.site-packages.sklearn.__check_build',
              'venv.lib.python3.6.site-packages.sklearn.decomposition',
              'venv.lib.python3.6.site-packages.sklearn.decomposition.tests',
              'venv.lib.python3.6.site-packages.sklearn.preprocessing',
              'venv.lib.python3.6.site-packages.sklearn.preprocessing.tests',
              'venv.lib.python3.6.site-packages.sklearn.neural_network',
              'venv.lib.python3.6.site-packages.sklearn.neural_network.tests',
              'venv.lib.python3.6.site-packages.sklearn.model_selection',
              'venv.lib.python3.6.site-packages.sklearn.model_selection.tests',
              'venv.lib.python3.6.site-packages.sklearn.semi_supervised',
              'venv.lib.python3.6.site-packages.sklearn.semi_supervised.tests',
              'venv.lib.python3.6.site-packages.sklearn.gaussian_process',
              'venv.lib.python3.6.site-packages.sklearn.gaussian_process.tests',
              'venv.lib.python3.6.site-packages.sklearn.feature_selection',
              'venv.lib.python3.6.site-packages.sklearn.feature_selection.tests',
              'venv.lib.python3.6.site-packages.sklearn.feature_extraction',
              'venv.lib.python3.6.site-packages.sklearn.feature_extraction.tests',
              'venv.lib.python3.6.site-packages.sklearn.cross_decomposition',
              'venv.lib.python3.6.site-packages.sklearn.cross_decomposition.tests',
              'venv.lib.python3.6.site-packages.urllib3', 'venv.lib.python3.6.site-packages.urllib3.util',
              'venv.lib.python3.6.site-packages.urllib3.contrib',
              'venv.lib.python3.6.site-packages.urllib3.contrib._securetransport',
              'venv.lib.python3.6.site-packages.urllib3.packages',
              'venv.lib.python3.6.site-packages.urllib3.packages.backports',
              'venv.lib.python3.6.site-packages.urllib3.packages.ssl_match_hostname',
              'venv.lib.python3.6.site-packages.requests', 'venv.lib.python3.6.site-packages.cssselect',
              'venv.lib.python3.6.site-packages.setuptools', 'venv.lib.python3.6.site-packages.setuptools.extern',
              'venv.lib.python3.6.site-packages.setuptools.command', 'venv.lib.python3.6.site-packages.pkg_resources',
              'venv.lib.python3.6.site-packages.pkg_resources.extern',
              'venv.lib.python3.6.site-packages.pkg_resources._vendor',
              'venv.lib.python3.6.site-packages.pkg_resources._vendor.packaging'],
    url='',
    license='',
    author='shawn',
    author_email='',
    description='', install_requires=['Pillow', 'numpy', 'requests', 'pyquery', 'scikit-learn']
)
