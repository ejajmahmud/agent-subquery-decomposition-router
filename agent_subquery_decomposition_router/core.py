"""Core Subquery Decomposition Router implementation."""
import re
from typing import Dict, List

class TargetIndex:
    CODE = "code"
    DOCS = "docs"
    CHANGELOG = "changelog"

class SubqueryPlan:
    def __init__(self, original_query: str, subqueries: List[Dict[str, str]]):
        self.original_query = original_query
        self.subqueries = subqueries

class DecompositionRouter:
    @classmethod
    def decompose_and_route(cls, query: str) -> SubqueryPlan:
        # Split on coordinating conjunctions
        parts = re.split(r"(?i)\s+(?:and|also|while|compare|versus|vs)\s+", query)
        clean_parts = [p.strip() for p in parts if p.strip()]

        planned = []
        for p in clean_parts:
            # Classify target index
            lower = p.lower()
            if any(k in lower for k in ("code", "function", "def", "implementation", "script")):
                target = TargetIndex.CODE
            elif any(k in lower for k in ("migration", "version", "diff", "v1", "v2", "release")):
                target = TargetIndex.CHANGELOG
            else:
                target = TargetIndex.DOCS

            planned.append({"subquery": p, "target_index": target})

        return SubqueryPlan(query, planned)
