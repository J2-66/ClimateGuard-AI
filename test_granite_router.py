from granite_router import get_agent


print("=" * 60)
print("      CLIMATEGUARD AI - GRANITE ROUTER TEST")
print("=" * 60)


questions = [

    "What should I do during severe flooding?",

    "How can I reduce my carbon footprint?",

    "What is climate adaptation?",

    "Why is climate change happening?",

    "How does heavy rainfall increase flood risk?",

    "How can I reduce emissions from electricity?"
]


for question in questions:

    print("\n" + "-" * 60)

    print("Question:")
    print(question)

    agent = get_agent(question)

    print("Selected Agent:")
    print(agent)


print("\n" + "=" * 60)
print("GRANITE ROUTER TEST COMPLETE")
print("=" * 60)