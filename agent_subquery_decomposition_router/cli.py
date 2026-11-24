"""CLI for Subquery Decomposition Router."""
import argparse
from .core import DecompositionRouter

def main():
    parser = argparse.ArgumentParser(description="Agent Subquery Decomposition Router CLI")
    parser.add_argument("--demo", action="store_true", help="Run query decomposition demo")
    args = parser.parse_args()

    q = "Explain OAuth configuration in docs and provide python code for token refresh"
    plan = DecompositionRouter.decompose_and_route(q)
    print(f"Original Query: {plan.original_query}")
    print("Decomposed & Routed Subqueries:")
    for sq in plan.subqueries:
        print(f"  -> [{sq['target_index'].upper()}] {sq['subquery']}")

if __name__ == "__main__":
    main()
