# 🤖 Multi-Agent Research Assistant

A sophisticated AI-powered research system built with Google's Gemini API that uses multiple specialized agents to conduct comprehensive research on any topic.

## 🌟 Features

- **Multi-Agent Architecture**: Three specialized AI agents working together
- **Intelligent Planning**: Breaks down complex topics into researchable questions
- **Real-time Research**: Uses Google Search integration for up-to-date information
- **Professional Reports**: Synthesizes findings into comprehensive reports
- **Easy to Use**: Simple command-line interface
- **Extensible**: Modular design for easy customization

## 🏗️ System Architecture

The system consists of three specialized agents:

### 1. 📋 Planner Agent
- **Role**: Project Manager
- **Function**: Breaks down broad topics into 3-5 specific, researchable questions
- **Output**: Structured list of research questions

### 2. 🔍 Search Agent
- **Role**: Research Analyst
- **Function**: Uses Google Search to find detailed information for each question
- **Output**: Comprehensive research data for each question

### 3. 📝 Synthesizer Agent
- **Role**: Technical Writer
- **Function**: Compiles all research findings into a coherent final report
- **Output**: Professional, well-structured research report

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Google Gemini API key ([Get it here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone or download this project**
   ```bash
   # Navigate to the project directory
   cd Multi-Agent-gemi
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   ```bash
   # Copy the example environment file
   copy .env.example .env
   
   # Edit .env and add your API key
   # GOOGLE_API_KEY=your_actual_api_key_here
   ```

### Running the System

1. **Start the main application**
   ```bash
   python main.py
   ```

2. **Or run example usage**
   ```bash
   python example_usage.py
   ```

## 🎯 JUST RUN IT - Super Simple Steps

**For anyone who just wants to run this immediately:**

### Step 1: Get API Key
1. Go to: https://makersuite.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key (looks like: `AIzaSyBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`)

### Step 2: Set Up (One Time Only)
```bash
# 1. Install Python packages
pip install -r requirements.txt

# 2. Create .env file with your API key
echo GOOGLE_API_KEY=your_actual_api_key_here > .env
```

### Step 3: Run It!
```bash
python main.py
```

**That's it!** Enter any topic when prompted and watch the AI agents work!

### 🚀 Alternative: Simple Version (No Google Search)
If you want to test without Google Search:
```bash
python simple_research.py
```

## 📖 Usage Guide

### Basic Usage

1. Run the application: `python main.py`
2. Enter your research topic when prompted
3. Wait for the system to:
   - Create a research plan
   - Conduct research on each question
   - Generate a final report
4. Review the comprehensive report
5. Optionally save the report to a file

### Example Topics

Try these example topics to get started:

- "Benefits of renewable energy"
- "Impact of social media on mental health"
- "Future of electric vehicles"
- "Artificial intelligence in healthcare"
- "Climate change solutions"

### Programmatic Usage

You can also use the system programmatically:

```python
from main import MultiAgentResearchAssistant

# Initialize the assistant
assistant = MultiAgentResearchAssistant()
assistant.initialize()

# Conduct research
report = assistant.conduct_research("Your research topic here")
print(report)
```

## 🧪 Testing

Run the example usage script to test the system:

```bash
python example_usage.py
```

This will provide options to:
- Run a quick system test
- Test individual agents
- Run example research sessions

## 📁 Project Structure

```
Multi-Agent-gemi/
├── main.py              # Main application and orchestrator
├── agents.py            # Individual agent implementations
├── config.py            # Configuration and API setup
├── example_usage.py     # Example usage and testing
├── requirements.txt     # Python dependencies
├── env_example.txt      # Environment variables template
└── README.md           # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with your API key:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### Model Configuration

The system uses `gemini-1.5-pro-latest` by default. You can modify this in `config.py`:

```python
return genai.GenerativeModel('gemini-1.5-pro-latest')
```

## 🛠️ Customization

### Adding New Agents

1. Create a new agent class in `agents.py`
2. Implement the required methods
3. Add the agent to the orchestrator in `main.py`

### Modifying Agent Behavior

Each agent can be customized by modifying their prompts in `agents.py`:

- **Planner Agent**: Adjust the planning prompt for different question types
- **Search Agent**: Modify search parameters and result processing
- **Synthesizer Agent**: Change report format and structure

### Extending Functionality

- Add new research tools (beyond Google Search)
- Implement different report formats (PDF, HTML, etc.)
- Add research result caching
- Implement parallel research processing

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your `.env` file exists and contains a valid API key
   - Verify the key is active at [Google AI Studio](https://makersuite.google.com/app/apikey)

2. **Import Errors**
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version (3.7+ required)

3. **Search Failures**
   - Google Search integration requires a valid Gemini API key
   - Some topics may not return results - try rephrasing

4. **Rate Limiting**
   - The system includes delays to avoid rate limits
   - If you encounter issues, increase delays in `main.py`

### Getting Help

If you encounter issues:

1. Run the quick test: `python example_usage.py` → Option 1
2. Check your API key is valid
3. Ensure all dependencies are installed
4. Try with a simple topic first

## 📊 Example Output

```
🤖 Multi-Agent Research Assistant
Built with Google Gemini API
==================================================

🚀 Initializing Multi-Agent Research Assistant...
   ✓ Gemini model configured
   ✓ API key validated
   ✓ All agents initialized
🎉 System ready for research!

==================================================
🎯 What would you like to research today?
(Type 'quit' or 'exit' to stop)

📝 Enter your research topic: Benefits of renewable energy

🔍 Starting research process for: 'Benefits of renewable energy'
============================================================

📋 STEP 1: Creating Research Plan
----------------------------------------
Planner Agent: Creating a research plan for 'Benefits of renewable energy'...
Planner Agent: Research plan created with 4 questions:
   1. What are the environmental benefits of renewable energy sources?
   2. How does renewable energy impact economic growth and job creation?
   3. What are the long-term cost benefits of transitioning to renewable energy?
   4. How does renewable energy improve energy security and independence?

🔎 STEP 2: Conducting Research (4 questions)
----------------------------------------

[1/4] Processing question...
Search Agent: Researching question: 'What are the environmental benefits of renewable energy sources?'...
   ✓ Information found and processed
   ✓ Question 1 completed

[2/4] Processing question...
Search Agent: Researching question: 'How does renewable energy impact economic growth and job creation?'...
   ✓ Information found and processed
   ✓ Question 2 completed

[3/4] Processing question...
Search Agent: Researching question: 'What are the long-term cost benefits of transitioning to renewable energy?'...
   ✓ Information found and processed
   ✓ Question 3 completed

[4/4] Processing question...
Search Agent: Researching question: 'How does renewable energy improve energy security and independence?'...
   ✓ Information found and processed
   ✓ Question 4 completed

📝 STEP 3: Creating Final Report
----------------------------------------
Synthesizer Agent: Writing the final report...
   ✓ Final report generated successfully

================================================================================
📊 FINAL RESEARCH REPORT
================================================================================
🎯 Topic: Benefits of renewable energy
================================================================================

# The Comprehensive Benefits of Renewable Energy

## Introduction

Renewable energy represents one of the most significant technological and environmental advances of our time. As the world grapples with climate change, energy security concerns, and economic challenges, renewable energy sources offer a multifaceted solution that addresses environmental, economic, and social needs simultaneously.

## Environmental Benefits

Renewable energy sources provide substantial environmental advantages that are crucial for addressing climate change and environmental degradation...

[Comprehensive report continues...]

================================================================================
📋 End of Report
================================================================================

💾 Would you like to save this report to a file? (y/n):
```

## 🤝 Contributing

This project is designed to be educational and extensible. Feel free to:

- Add new agent types
- Improve existing prompts
- Add new research tools
- Enhance the user interface
- Add new output formats

## 📄 License

This project is for educational purposes. Please ensure you comply with Google's Gemini API terms of service when using this system.

## 🙏 Acknowledgments

- Built with [Google's Gemini API](https://ai.google.dev/)
- Inspired by multi-agent system research
- Designed for educational and research purposes

---

**Happy Researching! 🚀**
