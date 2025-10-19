"""
Multi-Agent Research Assistant
Main orchestrator that coordinates all agents to perform comprehensive research
"""

import sys
import time
from config import configure_gemini, validate_api_key
from agents import PlannerAgent, SearchAgent, SynthesizerAgent

class MultiAgentResearchAssistant:
    """
    Main orchestrator class that coordinates the three agents:
    - Planner Agent: Breaks down topics into research questions
    - Search Agent: Researches each question using Google Search
    - Synthesizer Agent: Creates the final comprehensive report
    """
    
    def __init__(self):
        self.model = None
        self.planner = None
        self.searcher = None
        self.synthesizer = None
        
    def initialize(self):
        """
        Initialize the system by configuring the Gemini model and creating agent instances
        
        Returns:
            bool: True if initialization successful, False otherwise
        """
        try:
            print("🚀 Initializing Multi-Agent Research Assistant...")
            
            # Configure Gemini model
            self.model = configure_gemini()
            print("   ✓ Gemini model configured")
            
            # Validate API key
            if not validate_api_key():
                print("   ✗ API key validation failed")
                return False
            print("   ✓ API key validated")
            
            # Initialize agents
            self.planner = PlannerAgent(self.model)
            self.searcher = SearchAgent(self.model)
            self.synthesizer = SynthesizerAgent(self.model)
            print("   ✓ All agents initialized")
            
            print("🎉 System ready for research!")
            return True
            
        except Exception as e:
            print(f"❌ Initialization failed: {e}")
            return False
    
    def conduct_research(self, topic: str) -> str:
        """
        Conduct comprehensive research on a given topic using all three agents
        
        Args:
            topic (str): The topic to research
            
        Returns:
            str: Final research report
        """
        if not self.model:
            return "Error: System not initialized. Please run initialize() first."
        
        print(f"\n🔍 Starting research process for: '{topic}'")
        print("=" * 60)
        
        # Step 1: Create research plan
        print("\n📋 STEP 1: Creating Research Plan")
        print("-" * 40)
        research_plan = self.planner.create_research_plan(topic)
        
        if not research_plan:
            return "❌ Could not create a research plan. Please try a different topic."
        
        # Step 2: Research each question
        print(f"\n🔎 STEP 2: Conducting Research ({len(research_plan)} questions)")
        print("-" * 40)
        research_results = []
        
        for i, question in enumerate(research_plan, 1):
            print(f"\n[{i}/{len(research_plan)}] Processing question...")
            research_data = self.searcher.research_question(question)
            
            if research_data:
                research_results.append((question, research_data))
                print(f"   ✓ Question {i} completed")
            else:
                print(f"   ⚠️  Question {i} - no data found")
            
            # Small delay to avoid rate limiting
            time.sleep(1)
        
        if not research_results:
            return "❌ Could not find any information during research. Please try a different topic."
        
        # Step 3: Synthesize final report
        print(f"\n📝 STEP 3: Creating Final Report")
        print("-" * 40)
        final_report = self.synthesizer.create_final_report(topic, research_results)
        
        return final_report
    
    def display_report(self, topic: str, report: str):
        """
        Display the final research report in a formatted way
        
        Args:
            topic (str): The research topic
            report (str): The final report
        """
        print("\n" + "=" * 80)
        print("📊 FINAL RESEARCH REPORT")
        print("=" * 80)
        print(f"🎯 Topic: {topic}")
        print("=" * 80)
        print(report)
        print("=" * 80)
        print("📋 End of Report")
        print("=" * 80)


def main():
    """
    Main function to run the Multi-Agent Research Assistant
    """
    print("🤖 Multi-Agent Research Assistant")
    print("Built with Google Gemini API")
    print("=" * 50)
    
    # Initialize the system
    assistant = MultiAgentResearchAssistant()
    if not assistant.initialize():
        print("\n❌ Failed to initialize the system. Please check your API key and try again.")
        print("\n💡 Setup Instructions:")
        print("1. Get your Gemini API key from: https://makersuite.google.com/app/apikey")
        print("2. Create a .env file in this directory")
        print("3. Add your API key: GOOGLE_API_KEY=your_key_here")
        return
    
    # Main interaction loop
    while True:
        print("\n" + "=" * 50)
        print("🎯 What would you like to research today?")
        print("(Type 'quit' or 'exit' to stop)")
        
        topic = input("\n📝 Enter your research topic: ").strip()
        
        if topic.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Thank you for using the Multi-Agent Research Assistant!")
            break
        
        if not topic:
            print("⚠️  Please enter a valid topic to research.")
            continue
        
        try:
            # Conduct research
            report = assistant.conduct_research(topic)
            
            # Display results
            if report.startswith("❌"):
                print(f"\n{report}")
            else:
                assistant.display_report(topic, report)
                
                # Ask if user wants to save the report
                save_choice = input("\n💾 Would you like to save this report to a file? (y/n): ").strip().lower()
                if save_choice in ['y', 'yes']:
                    save_report_to_file(topic, report)
        
        except KeyboardInterrupt:
            print("\n\n⏹️  Research interrupted by user.")
            break
        except Exception as e:
            print(f"\n❌ An error occurred during research: {e}")
            print("Please try again with a different topic.")


def save_report_to_file(topic: str, report: str):
    """
    Save the research report to a text file
    
    Args:
        topic (str): The research topic
        report (str): The report content
    """
    try:
        # Create filename from topic
        safe_topic = "".join(c for c in topic if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_topic = safe_topic.replace(' ', '_')
        filename = f"research_report_{safe_topic}_{int(time.time())}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Research Report: {topic}\n")
            f.write("=" * 50 + "\n")
            f.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 50 + "\n\n")
            f.write(report)
        
        print(f"✅ Report saved as: {filename}")
        
    except Exception as e:
        print(f"❌ Failed to save report: {e}")


if __name__ == "__main__":
    main()
