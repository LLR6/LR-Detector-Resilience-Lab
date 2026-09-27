import unittest
from pathlib import Path
from resilience_lab.cli import load,train,score,experiment

DATA=Path(__file__).parents[1]/"examples/features.csv"
class LabTests(unittest.TestCase):
 def test_training_separates_sample(self):
  rows=load(DATA); model=train(rows)
  benign=sum(score(model,r) for r in rows if not r['label'])/10
  malicious=sum(score(model,r) for r in rows if r['label'])/10
  self.assertGreater(malicious,benign)
 def test_experiment_is_deterministic(self):
  rows=load(DATA); self.assertEqual(experiment(rows,7),experiment(rows,7))
 def test_report_states_non_executable_boundary(self):
  self.assertIn("no executable",experiment(load(DATA))["boundary"].lower())
if __name__=="__main__":unittest.main()
