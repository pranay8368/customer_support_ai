"""
main.py
-------
Entry point for the AI-Powered Customer Support Automation System.

Runs the LangGraph workflow against the 5 sample demonstration
queries from the assignment.

Task 10: Demonstrate the system using the five sample customer queries.
"""

from memory import init_db
from graph import build_graph

# The 5 sample queries from the assignment, each from a different
# (fictional) customer for clarity in the demo and memory recall test.
DEMO_QUERIES = [
    {"customer_name": "Alice", "query": "What are the pricing plans available for your software?"},
    {"customer_name": "Bob", "query": "I forgot my account password."},
    {"customer_name": "Carol", "query": "My application crashes whenever I upload a file."},
    {"customer_name": "David", "query": "I need a refund for my annual subscription."},
    {"customer_name": "David", "query": "What was my previous support issue?"},
]


def run_demo():
    print("Initializing database...")
    init_db()

    app = build_graph()

    for i, item in enumerate(DEMO_QUERIES, start=1):
        print("\n" + "#" * 70)
        print(f"DEMO QUERY {i}")
        print(f"Customer: {item['customer_name']}")
        print(f"Query: {item['query']}")
        print("#" * 70)

        initial_state = {
            "customer_name": item["customer_name"],
            "query": item["query"],
            "intent": None,
            "retrieved_context": None,
            "memory_context": None,
            "draft_response": None,
            "needs_approval": False,
            "approval_status": None,
            "final_response": None,
        }

        result = app.invoke(initial_state)

        print("\n--- FINAL RESPONSE TO CUSTOMER ---")
        print(result["final_response"])
        print()


if __name__ == "__main__":
    run_demo()