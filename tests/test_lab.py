import unittest
from pathlib import Path
from resilience_lab.cli import experiment,load,score,threshold_sweep,train

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
 def test_threshold_sweep_reports_recall_drop(self):
  rows=load(DATA);model=train(rows);base=[score(model,r) for r in rows]
  changed=experiment(rows,7,1.0,.5,[.3,.5,.7])["threshold_sweep"]
  self.assertEqual([x["threshold"] for x in changed],[.3,.5,.7])
  self.assertTrue(all("recall_drop" in x for x in changed))
 def test_experiment_includes_optional_sweep(self):
  report=experiment(load(DATA),7,1.0,.5,[.4,.6])
  self.assertEqual(len(report["threshold_sweep"]),2)
if __name__=="__main__":unittest.main()
