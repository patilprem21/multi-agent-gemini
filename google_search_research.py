"""
Multi-Agent Research Assistant with Google Search Integration
This version properly implements Google Search for real-time information
"""

import time
from config import configure_gemini, validate_api_key
from agents import PlannerAgent, SynthesizerAgent
import google.generativeai as genai

class GoogleSearchAgent:
    """
    Enhanced Search Agent that uses Google Search for real-time information
    """
    
    def __init__(self, model):
        self.model = model
        self.name = "Google Search Agent"
    
    def research_question(self, question: str) -> str:
        """
        Research a specific question using Google Search
        
        Args:
            question (str): The specific question to research
            
        Returns:
            str: Detailed research findings
        """
        print(f"{self.name}: Researching question: '{question}'...")
        
        try:
            # Method 1: Try with Google Search tool
            try:
                search_tool = genai.protos.Tool(
                    google_search_retrieval=genai.protos.GoogleSearchRetrieval()
                )
                
                prompt = f"""
                Search the web for current, accurate information about: {question}
                
                Provide a comprehensive answer based on the most recent and reliable sources found.
                Include:
                - Current facts and data
                - Recent statistics and trends
                - Expert opinions and analysis
                - Real-world examples and case studies
                - Up-to-date developments
                
                Make sure to use only information from credible, recent sources.
                """
                
                response = self.model.generate_content(prompt, tools=[search_tool])
                
                if response.text:
                    print(f"   ✓ Information found via Google Search")
                    return response.text
                else:
                    print(f"   ⚠️  Google Search returned no results, trying alternative method...")
                    
            except Exception as search_error:
                print(f"   ⚠️  Google Search failed: {search_error}")
                print(f"   🔄 Trying alternative research method...")
            
            # Method 2: Fallback to Gemini's knowledge with search context
            fallback_prompt = f"""
            Research and provide comprehensive information about: {question}
            
            Please provide:
            - Current facts and data (as of your knowledge cutoff)
            - Recent trends and developments
            - Expert insights and analysis
            - Real-world examples and case studies
            - Statistical data where available
            
            Focus on providing the most accurate and up-to-date information possible.
            """
            
            response = self.model.generate_content(fallback_prompt)
            
            if response.text:
                print(f"   ✓ Information found via knowledge base")
                return response.text
            else:
                print(f"   ✗ No information found")
                return ""
                
        except Exception as e:
            print(f"Error in {self.name}: {e}")
            return ""


class GoogleSearchResearchAssistant:
    """
    Multi-Agent Research Assistant with Google Search Integration
    """
    
    def __init__(self):
        self.model = None
        self.planner = None
        self.searcher = None
        self.synthesizer = None
        
    def initialize(self):
        """
        Initialize the system by configuring the Gemini model and creating agent instances
        """
        try:
            print("🚀 Initializing Google Search Multi-Agent Research Assistant...")
            
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
            self.searcher = GoogleSearchAgent(self.model)
            self.synthesizer = SynthesizerAgent(self.model)
            print("   ✓ All agents initialized")
            
            print("🎉 System ready for research with Google Search!")
            return True
            
        except Exception as e:
            print(f"❌ Initialization failed: {e}")
            return False
    
    def conduct_research(self, topic: str) -> str:
        """
        Conduct comprehensive research on a given topic using all three agents
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
            time.sleep(2)
        
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
    Main function to run the Google Search Multi-Agent Research Assistant
    """
    print("🤖 Google Search Multi-Agent Research Assistant")
    print("Built with Google Gemini API + Google Search Integration")
    print("=" * 70)
    
    # Initialize the system
    assistant = GoogleSearchResearchAssistant()
    if not assistant.initialize():
        print("\n❌ Failed to initialize the system. Please check your API key and try again.")
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
    """
    try:
        # Create filename from topic
        safe_topic = "".join(c for c in topic if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_topic = safe_topic.replace(' ', '_')
        filename = f"google_search_report_{safe_topic}_{int(time.time())}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Google Search Research Report: {topic}\n")
            f.write("=" * 50 + "\n")
            f.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 50 + "\n\n")
            f.write(report)
        
        print(f"✅ Report saved as: {filename}")
        
    except Exception as e:
        print(f"❌ Failed to save report: {e}")


if __name__ == "__main__":
    main()
