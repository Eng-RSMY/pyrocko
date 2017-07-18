import unittest
import shutil
import tempfile
from pyrocko import util, gf
from pyrocko.fomosto import qssp


class QSSPTestCase(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix='pyrocko.qseis')

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def test_qssp_build(self):
        qssp.init(self.tmpdir, '2010')
        store = gf.store.Store(self.tmpdir, 'r')
        store.make_ttt()
        qssp.build(self.tmpdir)


if __name__ == '__main__':
    util.setup_logging('test_gf_qssp', 'warning')
    unittest.main()