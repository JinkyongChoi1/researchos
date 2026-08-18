import unittest
from pathlib import Path

from researchos.core import STAGES, load_fixture, run_demo, validate


class ResearchOSTest(unittest.TestCase):
    def setUp(self):
        self.fixture = load_fixture(Path(__file__).parents[1] / "fixtures" / "demo_project.json")

    def test_fixture_has_valid_provenance(self):
        self.assertEqual(validate(self.fixture), [])

    def test_demo_completes_every_stage(self):
        state = run_demo(self.fixture)
        self.assertEqual(state["workflow"]["completed"], STAGES)
        self.assertEqual(len(state["events"]), len(STAGES))

    def test_demo_keeps_decision_pending(self):
        state = run_demo(self.fixture)
        self.assertEqual(state["decision"]["status"], "pending")
        self.assertEqual(state["events"][4]["actor"], "human-review")


if __name__ == "__main__":
    unittest.main()
