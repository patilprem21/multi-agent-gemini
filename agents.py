"""
Multi-Agent System Implementation
Contains the three specialized agents: Planner, Search, and Synthesizer
"""

import google.generativeai as genai
from typing import List, Tuple
import re

class PlannerAgent:
    """
    The Planner Agent breaks down broad topics into specific, researchable questions.
    Acts as the project manager of the research process.
    """
    
    def __init__(self, model):
        self.model = model
        self.name = "Planner Agent"
    
    def create_research_plan(self, topic: str) -> List[str]:
        """
        Break down a topic into 3-5 specific, researchable questions
        
        Args:
            topic (str): The main topic to research
            
        Returns:
            List[str]: List of specific research questions
        """
        print(f"{self.name}: Creating a research plan for '{topic}'...")
        
        prompt = f"""
        You are an expert research planner. Your task is to break down the following topic
        into 3-5 specific, answerable questions that would provide comprehensive coverage
        of the subject matter.

        TOPIC: "{topic}"

        Guidelines:
        - Each question should be specific and focused
        - Questions should cover different aspects of the topic
        - Questions should be researchable and answerable
        - Return ONLY the questions as a Python list format

        Example output format: ["question 1", "question 2", "question 3", "question 4"]
        """
        
        try:
            response = self.model.generate_content(prompt)
            plan_str = response.text.strip()
            
            # Extract questions from the response
            questions = self._extract_questions(plan_str)
            
            if questions:
                print(f"{self.name}: Research plan created with {len(questions)} questions:")
                for i, question in enumerate(questions, 1):
                    print(f"   {i}. {question}")
                return questions
            else:
                print(f"{self.name}: Failed to extract questions from response")
                return []
                
        except Exception as e:
            print(f"Error in {self.name}: {e}")
            return []
    
    def _extract_questions(self, response_text: str) -> List[str]:
        """
        Extract questions from the model's response text
        
        Args:
            response_text (str): Raw response from the model
            
        Returns:
            List[str]: Cleaned list of questions
        """
        # Try to find list format first
        list_match = re.search(r'\[(.*?)\]', response_text, re.DOTALL)
        if list_match:
            list_content = list_match.group(1)
            # Split by comma and clean up
            questions = [q.strip().strip('"\'') for q in list_content.split(',')]
            return [q for q in questions if q and len(q) > 10]  # Filter out empty/short items
        
        # Fallback: split by newlines and look for question patterns
        lines = response_text.split('\n')
        questions = []
        for line in lines:
            line = line.strip()
            if (line.startswith(('1.', '2.', '3.', '4.', '5.')) or 
                line.startswith(('-', '*')) or
                ('?' in line and len(line) > 20)):
                # Clean up the line
                clean_line = re.sub(r'^\d+\.\s*', '', line)
                clean_line = re.sub(r'^[-*]\s*', '', clean_line)
                clean_line = clean_line.strip('"\'')
                if clean_line:
                    questions.append(clean_line)
        
        return questions[:5]  # Limit to 5 questions


class SearchAgent:
    """
    The Search Agent uses Google Search to find detailed information for specific questions.
    Acts as the diligent researcher gathering raw data.
    """
    
    def __init__(self, model):
        self.model = model
        self.name = "Search Agent"
    
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
            # Configure Google Search tool
            search_tool = genai.protos.Tool(
                google_search_retrieval=genai.protos.GoogleSearchRetrieval()
            )
            
            prompt = f"""
            Provide a comprehensive and detailed answer to the following question.
            Use the most current and reliable information available.
            Include relevant facts, statistics, and context.
            
            Question: {question}
            
            Please provide a thorough response with:
            - Key facts and information
            - Relevant statistics or data points
            - Important context or background
            - Current developments or trends
            """
            
            response = self.model.generate_content(prompt, tools=[search_tool])
            
            if response.text:
                print(f"   ✓ Information found and processed")
                return response.text
            else:
                print(f"   ✗ No information found")
                return ""
                
        except Exception as e:
            print(f"Error in {self.name}: {e}")
            # Fallback: Try without Google Search if search grounding fails
            if "Search Grounding is not supported" in str(e):
                print(f"   🔄 Trying fallback method (no Google Search)...")
                try:
                    fallback_prompt = f"""
                    Provide a comprehensive answer to: {question}
                    
                    Use your knowledge to provide detailed information including:
                    - Key facts and concepts
                    - Current trends and developments
                    - Expert insights and analysis
                    - Real-world examples
                    - Statistical data where available
                    """
                    
                    fallback_response = self.model.generate_content(fallback_prompt)
                    if fallback_response.text:
                        print(f"   ✓ Information found via fallback method")
                        return fallback_response.text
                except Exception as fallback_error:
                    print(f"   ✗ Fallback also failed: {fallback_error}")
            return ""


class SynthesizerAgent:
    """
    The Synthesizer Agent compiles all research findings into a coherent final report.
    Acts as the expert writer creating the final deliverable.
    """
    
    def __init__(self, model):
        self.model = model
        self.name = "Synthesizer Agent"
    
    def create_final_report(self, topic: str, research_results: List[Tuple[str, str]]) -> str:
        """
        Synthesize all research findings into a comprehensive report
        
        Args:
            topic (str): The main research topic
            research_results (List[Tuple[str, str]]): List of (question, research_data) tuples
            
        Returns:
            str: Final synthesized report
        """
        print(f"{self.name}: Writing the final report...")
        
        if not research_results:
            return "Error: No research data available to synthesize."
        
        # Compile all research notes
        research_notes = self._compile_research_notes(research_results)
        
        prompt = f"""
        You are an expert research analyst and technical writer. Your task is to synthesize
        the provided research notes into a comprehensive, well-structured report on the topic: "{topic}".

        Report Requirements:
        1. Create a professional, informative report
        2. Include an introduction that sets the context
        3. Organize findings into logical sections with clear headings
        4. Synthesize information from multiple sources into coherent insights
        5. Include a conclusion that summarizes key findings
        6. Use only the information provided in the research notes
        7. Write in a clear, professional tone
        8. Ensure the report flows logically from section to section

        ## Research Notes ##
        {research_notes}
        
        Please create a comprehensive report that effectively communicates the research findings.
        """
        
        try:
            response = self.model.generate_content(prompt)
            
            if response.text:
                print(f"   ✓ Final report generated successfully")
                return response.text
            else:
                return "Error: Could not generate the final report."
                
        except Exception as e:
            print(f"Error in {self.name}: {e}")
            return "Error: Could not generate the final report."
    
    def _compile_research_notes(self, research_results: List[Tuple[str, str]]) -> str:
        """
        Compile research results into formatted notes
        
        Args:
            research_results (List[Tuple[str, str]]): List of (question, research_data) tuples
            
        Returns:
            str: Formatted research notes
        """
        research_notes = ""
        
        for i, (question, data) in enumerate(research_results, 1):
            research_notes += f"""
### Research Question {i}: {question}

**Research Findings:**
{data}

---
"""
        
        return research_notes
