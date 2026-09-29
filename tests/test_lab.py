import unittest
from pathlib import Path
from resilience_lab.cli import experiment,load,score,strength_sweep,threshold_sweep,train

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
 def test_strength_sweep_tracks_drift_curve(self):
  rows=load(DATA)
  curve=strength_sweep(rows,7,[0,.5,1.0],.5)
  self.assertEqual([x["strength"] for x in curve],[0,.5,1.0])
  self.assertEqual(curve[0]["recall_drop"],0)
  self.assertTrue(all("flipped_malicious_samples" in x for x in curve))
 def test_experiment_includes_optional_strength_sweep(self):
  report=experiment(load(DATA),7,1.0,.5,None,[0,1.0])
  self.assertEqual(len(report["strength_sweep"]),2)
if __name__=="__main__":unittest.main()
