# 🚀 Setup Guide - Multi-Agent Research Assistant

This guide will walk you through setting up the Multi-Agent Research Assistant step by step.

## 📋 What You Need

### 1. System Requirements
- **Python 3.7 or higher** (Check with: `python --version`)
- **Internet connection** (for API calls and Google Search)
- **Text editor** (VS Code, Notepad++, or any editor you prefer)

### 2. Google Gemini API Key
- Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
- Sign in with your Google account
- Click "Create API Key"
- Copy the generated key (keep it safe!)

## 🛠️ Step-by-Step Setup

### Step 1: Verify Python Installation
Open your command prompt/terminal and check:
```bash
python --version
```
If you don't have Python, download it from [python.org](https://python.org)

### Step 2: Navigate to Project Directory
```bash
cd "C:\Users\ACER\Desktop\datascienceaiml\ML-Begner\Multi-Agent-gemi"
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up API Key
1. **Copy the environment template:**
   ```bash
   copy env_example.txt .env
   ```

2. **Edit the .env file:**
   - Open `.env` in your text editor
   - Replace `your_gemini_api_key_here` with your actual API key
   - Save the file

   Example:
   ```
   GOOGLE_API_KEY=AIzaxzxzxzxzxzxzxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

### Step 5: Test the Setup
```bash
python example_usage.py
```
Choose option 1 (Quick System Test) to verify everything works.

## ✅ Verification Checklist

- [ ] Python 3.7+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created with valid API key
- [ ] Quick test passes
- [ ] Can run `python main.py` without errors

## 🎯 First Run

1. **Start the application:**
   ```bash
   python main.py
   ```

2. **Try a simple topic:**
   - Enter: "Benefits of solar energy"
   - Watch the agents work!
   - Review the generated report

## 🆘 Troubleshooting

### Problem: "Module not found" errors
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### Problem: "API key not found" error
**Solution:** Check your `.env` file
- Make sure it's named exactly `.env` (not `.env.txt`)
- Verify the API key is correct
- Ensure no extra spaces or quotes

### Problem: "API key validation failed"
**Solution:** 
- Verify your API key is active
- Check you have internet connection
- Try generating a new API key

### Problem: Python not recognized
**Solution:**
- Add Python to your system PATH
- Or use `python3` instead of `python`
- Or use full path: `C:\Python39\python.exe`

## 🎉 You're Ready!

Once the quick test passes, you can:
- Run research on any topic
- Explore the example usage
- Customize the agents
- Build your own extensions

**Happy researching! 🚀**
