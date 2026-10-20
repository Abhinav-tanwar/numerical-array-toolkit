import unittest,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from analysis import matrix_inverse,temperature_summary,matrix_features
class ArrayTest(unittest.TestCase):
 def test_inverse_and_singularity(self):
  a=np.array([[2.,1.],[1.,3.]])
  np.testing.assert_allclose(a@matrix_inverse(a)['inverse'],np.eye(2),atol=1e-12)
  with self.assertRaises(ValueError):matrix_inverse(np.ones((3,3)))
 def test_temperature_ties(self):
  r=temperature_summary([0,10,10]);self.assertEqual(r['hottest_days'].tolist(),[2,3]);self.assertEqual(r['fahrenheit'][0],32)
 def test_slice_and_no_mutation(self):
  a=np.arange(49).reshape(7,7);r=matrix_features(a);self.assertEqual(r['submatrix'].shape,(3,3));self.assertEqual(a[0,2],2)
if __name__=='__main__':unittest.main()
