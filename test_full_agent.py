from agent_router import run_granite_agent


print("=" * 60)
print("       CLIMATEGUARD AI - FULL AGENT TEST")
print("=" * 60)


question = input(
    "\nAsk ClimateGuard AI: "
)


print("\nAnalyzing question...")

result = run_granite_agent(question)


print("\nSelected Agent:")
print(result["agent"])


print("\nClimateGuard AI:")
print(result["response"])


print("\n" + "=" * 60)
print("FULL AGENT WORKFLOW COMPLETE")
print("=" * 60)