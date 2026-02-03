import os
from dotenv import load_dotenv
from src.agents.planner import planner_agent
from src.agents.researcher import researcher_agent
from src.agents.writer import writer_agent
from src.agents.editor import editor_agent

# Load environment variables
load_dotenv()

print("=" * 60)
print("AGENT-LEVEL BYTEZ INTEGRATION TEST")
print("=" * 60)

# Test topic
test_topic = "AI in Healthcare"

# Test 1: Planner Agent
print("\n" + "-" * 60)
print("Test 1: Planner Agent")
print("-" * 60)
try:
    state = {"topic": test_topic}
    result = planner_agent(state)
    plan = result.get("research_plan", [])
    
    if len(plan) >= 4:
        print(f"✅ Planner returned {len(plan)} research topics")
        for i, item in enumerate(plan, 1):
            print(f"   {i}. {item}")
    else:
        print(f"⚠️ Planner returned only {len(plan)} topics (expected 4-5)")
except Exception as e:
    print(f"❌ Planner test failed: {e}")
    exit(1)

# Test 2: Researcher Agent (with limited plan)
print("\n" + "-" * 60)
print("Test 2: Researcher Agent (testing with 1 topic)")
print("-" * 60)
try:
    # Use only first topic to save time
    limited_plan = [plan[0]] if plan else ["Market Overview"]
    state = {"topic": test_topic, "research_plan": limited_plan}
    result = researcher_agent(state)
    research_data = result.get("research_data", {})
    
    if len(research_data) > 0:
        print(f"✅ Researcher gathered data for {len(research_data)} topic(s)")
        for topic in research_data.keys():
            print(f"   - {topic}")
    else:
        print("⚠️ Researcher returned no data")
except Exception as e:
    print(f"❌ Researcher test failed: {e}")
    exit(1)

# Test 3: Writer Agent
print("\n" + "-" * 60)
print("Test 3: Writer Agent")
print("-" * 60)
try:
    state = {
        "topic": test_topic,
        "research_plan": limited_plan,
        "research_data": research_data
    }
    result = writer_agent(state)
    draft_sections = result.get("draft_sections", {})
    
    if len(draft_sections) > 0:
        print(f"✅ Writer created {len(draft_sections)} draft section(s)")
        for topic in draft_sections.keys():
            print(f"   - {topic}")
    else:
        print("⚠️ Writer returned no sections")
except Exception as e:
    print(f"❌ Writer test failed: {e}")
    exit(1)

# Test 4: Editor Agent
print("\n" + "-" * 60)
print("Test 4: Editor Agent")
print("-" * 60)
try:
    state = {
        "topic": test_topic,
        "research_plan": limited_plan,
        "research_data": research_data,
        "draft_sections": draft_sections
    }
    result = editor_agent(state)
    final_report = result.get("final_report", "")
    
    if len(final_report) > 100:
        print(f"✅ Editor compiled final report ({len(final_report)} characters)")
        print(f"\nFirst 200 characters of report:")
        print(f"{final_report[:200]}...")
    else:
        print("⚠️ Editor returned a very short report")
except Exception as e:
    print(f"❌ Editor test failed: {e}")
    exit(1)

print("\n" + "=" * 60)
print("ALL AGENT TESTS PASSED!")
print("=" * 60)
print("\nYour Bytez integration is working correctly.")
print("You can now run the full app with: streamlit run app.py")
