"""
Example usage and test cases for the Multi-Agent Research Assistant
This file demonstrates how to use the system programmatically
"""

import time
from config import configure_gemini, validate_api_key
from agents import PlannerAgent, SearchAgent, SynthesizerAgent
from main import MultiAgentResearchAssistant

def test_individual_agents():
    """
    Test each agent individually to ensure they work correctly
    """
    print("🧪 Testing Individual Agents")
    print("=" * 40)
    
    try:
        # Initialize model
        model = configure_gemini()
        print("✓ Model configured successfully")
        
        # Test Planner Agent
        print("\n📋 Testing Planner Agent...")
        planner = PlannerAgent(model)
        test_topic = "Artificial Intelligence in Healthcare"
        questions = planner.create_research_plan(test_topic)
        
        if questions:
            print(f"✓ Planner Agent working - Generated {len(questions)} questions")
            for i, q in enumerate(questions[:2], 1):  # Show first 2 questions
                print(f"   {i}. {q}")
        else:
            print("✗ Planner Agent failed")
            return False
        
        # Test Search Agent (with a simple question)
        print("\n🔍 Testing Search Agent...")
        searcher = SearchAgent(model)
        test_question = "What is machine learning?"
        research_data = searcher.research_question(test_question)
        
        if research_data:
            print(f"✓ Search Agent working - Found {len(research_data)} characters of data")
        else:
            print("✗ Search Agent failed")
            return False
        
        # Test Synthesizer Agent
        print("\n📝 Testing Synthesizer Agent...")
        synthesizer = SynthesizerAgent(model)
        test_results = [(test_question, research_data)]
        report = synthesizer.create_final_report(test_topic, test_results)
        
        if report and not report.startswith("Error"):
            print(f"✓ Synthesizer Agent working - Generated {len(report)} character report")
        else:
            print("✗ Synthesizer Agent failed")
            return False
        
        print("\n🎉 All agents tested successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False


def run_example_research():
    """
    Run a complete example research session
    """
    print("\n🔬 Running Example Research Session")
    print("=" * 50)
    
    # Initialize the assistant
    assistant = MultiAgentResearchAssistant()
    if not assistant.initialize():
        print("❌ Failed to initialize assistant")
        return
    
    # Example research topics
    example_topics = [
        "Benefits of renewable energy",
        "Impact of social media on mental health",
        "Future of electric vehicles"
    ]
    
    print("📚 Example research topics:")
    for i, topic in enumerate(example_topics, 1):
        print(f"   {i}. {topic}")
    
    # Let user choose or use first topic
    choice = input(f"\nChoose a topic (1-{len(example_topics)}) or press Enter for topic 1: ").strip()
    
    try:
        topic_index = int(choice) - 1 if choice.isdigit() else 0
        selected_topic = example_topics[topic_index]
    except (ValueError, IndexError):
        selected_topic = example_topics[0]
    
    print(f"\n🎯 Selected topic: {selected_topic}")
    
    # Conduct research
    report = assistant.conduct_research(selected_topic)
    
    if not report.startswith("❌"):
        assistant.display_report(selected_topic, report)
        
        # Save the example report
        save_choice = input("\n💾 Save this example report? (y/n): ").strip().lower()
        if save_choice in ['y', 'yes']:
            from main import save_report_to_file
            save_report_to_file(selected_topic, report)
    else:
        print(f"\n{report}")


def quick_test():
    """
    Quick test to verify the system is working
    """
    print("⚡ Quick System Test")
    print("=" * 30)
    
    # Test API key
    if not validate_api_key():
        print("❌ API key validation failed")
        return False
    
    print("✓ API key is valid")
    
    # Test model configuration
    try:
        model = configure_gemini()
        print("✓ Model configuration successful")
    except Exception as e:
        print(f"❌ Model configuration failed: {e}")
        return False
    
    # Test a simple generation
    try:
        response = model.generate_content("Say 'Hello, Multi-Agent System!'")
        if response.text:
            print("✓ Model generation working")
            print(f"   Response: {response.text[:50]}...")
        else:
            print("❌ Model generation failed")
            return False
    except Exception as e:
        print(f"❌ Model generation error: {e}")
        return False
    
    print("\n🎉 Quick test passed! System is ready.")
    return True


def main():
    """
    Main function for example usage
    """
    print("🤖 Multi-Agent Research Assistant - Example Usage")
    print("=" * 60)
    
    while True:
        print("\n📋 Available Options:")
        print("1. Quick System Test")
        print("2. Test Individual Agents")
        print("3. Run Example Research")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == "1":
            quick_test()
        elif choice == "2":
            test_individual_agents()
        elif choice == "3":
            run_example_research()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
