"""Tests for DecompositionRouter."""
import unittest
from agent_subquery_decomposition_router.core import DecompositionRouter, TargetIndex

class TestDecompositionRouter(unittest.TestCase):
    def test_routing_logic(self):
        q = "Read architecture overview and review python code implementation"
        plan = DecompositionRouter.decompose_and_route(q)
        self.assertEqual(len(plan.subqueries), 2)
        self.assertEqual(plan.subqueries[0]["target_index"], TargetIndex.DOCS)
        self.assertEqual(plan.subqueries[1]["target_index"], TargetIndex.CODE)
