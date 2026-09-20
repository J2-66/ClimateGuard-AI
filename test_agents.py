from agent_router import route_query, run_agent


print("=" * 60)
print("       CLIMATEGUARD AI - AGENT TEST")
print("=" * 60)


questions = [

    "What should I do during a flood?",

    "How can I reduce my carbon footprint?",

    "According to the documents, what is climate adaptation?",

    "What is climate change?"
]


for question in questions:

    print("\n" + "-" * 60)

    print("QUESTION:")
    print(question)

    print("\nROUTING...")

    agent = route_query(question)

    print("Selected Agent:", agent)

    print("\nRunning agent...")

    result = run_agent(question)

    print("\nRESPONSE:")

    print(result["response"])


print("\n" + "=" * 60)

print("✅ AGENT TEST COMPLETE")

print("=" * 60)