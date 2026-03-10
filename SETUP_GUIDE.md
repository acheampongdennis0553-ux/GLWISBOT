# GLWIS Academic Bot - Complete Setup & Usage Guide

## 📋 Overview

The GLWIS Academic Bot is an intelligent chatbot powered by OpenAI's GPT-3.5 that provides accurate information about **Glorious Living Word International School (GLWIS)** based on an official FAQ database.

**Key Benefits:**
- ✅ Answers questions 24/7 about school policies, fees, admissions, and facilities
- ✅ Provides consistent, factual information from verified sources
- ✅ Reduces administrative burden on school staff
- ✅ Improves communication with parents and prospective students
- ✅ Easy to maintain and update FAQ content

---

## 🚀 Quick Start (5 minutes)

### Step 1: Verify Python Installation
```bash
python --version
# Should show Python 3.8 or higher
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set API Key
Create a `.env` file in the project directory:
```
OPENAI_API_KEY=your-api-key-here
```

### Step 4: Run the Bot
```bash
python glwis_bot.py
```

### Step 5: Ask Questions
```
👤 You: Where is GLWIS located?
🎓 Bot: Glorious Living Word International School (GLWIS) is located in Beposo...
```

---

## 📦 Files Included

```
GLWIS/
├── glwis_bot.py              # ⭐ Main bot application (START HERE)
├── bot_features.py           # Advanced features (history, FAQ management)
├── setup_check.py            # Automated setup verification
├── requirements.txt          # Python dependencies
├── README.md                 # Quick reference guide
├── SETUP_GUIDE.md           # This file
├── .env.example             # Example environment variables
└── chat_history.json        # (Auto-created) Chat conversation logs
```

---

## 🔧 Installation Details

### Option A: Using Command Prompt

```batch
# Navigate to project directory
cd c:\Users\DENNY\AI\GLWIS

# Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run setup check
python setup_check.py

# Start the bot
python glwis_bot.py
```

### Option B: Using PowerShell

```powershell
# Navigate to project directory
cd 'c:\Users\DENNY\AI\GLWIS'

# Create virtual environment (optional)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run setup check
python setup_check.py

# Start the bot
python glwis_bot.py
```

---

## 🔑 API Key Setup

### Getting an OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign up or log in to your OpenAI account
3. Click "Create new secret key"
4. Copy the key (it starts with `sk-`)

### Setting the API Key

**Method 1: .env File (Recommended)**
```
1. Create a file named `.env` in the project directory
2. Add: OPENAI_API_KEY=sk-your-key-here
3. The bot will automatically read from this file
```

**Method 2: Environment Variable**
```bash
# Windows (Command Prompt)
set OPENAI_API_KEY=sk-your-key-here

# Windows (PowerShell)
$env:OPENAI_API_KEY="sk-your-key-here"

# Mac/Linux
export OPENAI_API_KEY=sk-your-key-here
```

---

## 💬 Using the Bot

### Starting a Chat Session

```bash
python glwis_bot.py
```

You'll see:
```
============================================================
🎓 GLWIS ACADEMIC BOT - Welcome!
============================================================
I can answer questions about Glorious Living Word International School
based on the official FAQ document.

Sample questions you can ask:
  • Where is GLWIS located?
  • How much is the admission fee?
  • What is the fee structure?
  • Do you have boarding facilities?
  • How can I contact the school?
  • What extracurricular activities are available?
  • How does the school handle discipline?

(Type 'exit', 'quit', or 'bye' to stop)

👤 You: 
```

### Example Conversations

**Example 1: Admission Information**
```
👤 You: How can I get admission at GLWIS?
🎓 Bot: To get admission at GLWIS, you need to:
1. Buy the admission form from the admission office
2. Fill and submit the form
3. Write the entrance examination
The admission fee varies by class level.
```

**Example 2: Fee Structure**
```
👤 You: What are the fees at GLWIS?
🎓 Bot: The total termly fee varies by class and student location. Here's the breakdown:
- Tuition Fee: GHS150.00 – GHS250.00 per term
- Feeding Fee (Canteen): GHS5.00 – GHS8.00 per day
- Transportation Fee: GHS5.00 – GHS15.00 per day
... (and more)
```

**Example 3: Not in FAQ**
```
👤 You: What's the name of the principal?
🎓 Bot: I don't have that information in the FAQ database. 
Please contact the school directly at +233553324378 for more details.
```

### Ending a Session

Type any of these to exit:
- `exit`
- `quit`
- `bye`
- Press `Ctrl+C`

---

## 🛠️ Advanced Features

### Chat History

The bot automatically saves conversations to `chat_history.json`:
```json
[
  {
    "timestamp": "2024-03-10T14:30:00",
    "question": "Where is GLWIS located?",
    "response": "Glorious Living Word International School..."
  }
]
```

### FAQ Management (bot_features.py)

```python
from bot_features import FAQManager

# Initialize FAQ manager
faq = FAQManager()

# Add new FAQ
faq.add_faq(
    "What is the school motto?",
    "Living in the Word of God"
)

# Search FAQ
results = faq.search_faq("admission")

# Get context for bot
context = faq.get_faq_context()
```

### Statistics

```python
from bot_features import ChatHistory

history = ChatHistory()
stats = history.get_statistics()
print(f"Total conversations: {stats['total_conversations']}")
```

---

## ⚙️ Configuration

### Customizing the Bot

Edit settings in `glwis_bot.py`:

```python
# Model and response quality
MODEL = "gpt-3.5-turbo"      # OpenAI model
MAX_TOKENS = 400             # Max response length
TEMPERATURE = 0.1            # Lower = more factual (0-1)

# School information
SCHOOL_NAME = "GLWIS"
SCHOOL_CONTACT = "+233553324378"
```

### Temperature Explanation

- **0.1 (Current)**: Very factual, repeatable answers - BEST for FAQ
- **0.5**: Balanced, some variation
- **0.9**: Creative, varied responses - NOT recommended for FAQs

---

## 🐛 Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'openai'"

**Solution:**
```bash
pip install -r requirements.txt
```

### Problem: "API key not found" Error

**Solution:**
1. Verify `.env` file exists in the project directory
2. Check the file contains: `OPENAI_API_KEY=sk-...`
3. Restart the bot

### Problem: Bot gives wrong information

**Solution:**
1. The bot only uses FAQ data in the code
2. Verify the answer is in the `GLWIS_FAQ` variable
3. Update the FAQ data if needed
4. Restart the bot

### Problem: Slow responses or timeouts

**Solution:**
- Check internet connection
- Verify OpenAI API is up (https://status.openai.com)
- Try reducing MAX_TOKENS
- Check if API key has sufficient quota

### Problem: "Invalid API Key" Error

**Solution:**
1. Verify your API key starts with `sk-`
2. Check key is not expired/revoked on platform.openai.com
3. Ensure no extra spaces in `.env` file
4. Try re-creating the .env file

---

## 💰 Cost Management

### Pricing Overview
- **GPT-3.5-turbo**: ~$0.0005 per 1K input tokens, ~$0.0015 per 1K output tokens
- **Average Cost per Question**: $0.001 - $0.005 USD

### Monitoring Usage
```bash
# Check API usage at:
https://platform.openai.com/account/usage/overview
```

### Ways to Reduce Costs
1. Use shorter FAQ context
2. Reduce MAX_TOKENS
3. Use simpler prompts
4. Cache FAQ data locally

---

## 🎯 Use Cases

### For School Administration
- **24/7 Support**: Answer common questions automatically
- **Reduce Email**: Filter out FAQ-based inquiries
- **Consistency**: Same information always provided

### For Parents
- **Quick Answers**: Get fee/admission info instantly
- **No Waiting**: Available anytime, day/night
- **Accurate**: Uses official school data

### For Prospective Students
- **Easy Onboarding**: Learn about GLWIS
- **Contact Info**: Get school phone/email if needed
- **Next Steps**: Understand admission process

---

## 📚 Updating FAQ Data

### Method 1: Edit in Code (Quick)

Edit `GLWIS_FAQ` in `glwis_bot.py`:

```python
GLWIS_FAQ = """Questions,Answers
...your FAQ data...
"""
```

### Method 2: Use FAQ Manager (Scalable)

```python
from bot_features import FAQManager

faq = FAQManager("glwis_faq.csv")
faq.add_faq("New Question?", "New Answer")
faq.update_faq(0, answer="Updated Answer")
```

### Method 3: Import CSV File

Save FAQ as `glwis_faq.csv` with columns: `Questions`, `Answers`

---

## 📞 Support & Contact

**For GLWIS Information:**
- Phone: +233553324378
- Email: Contact school directly

**For Technical Issues:**
- Check OpenAI documentation: https://platform.openai.com/docs
- Review error messages carefully
- Test bot connectivity

---

## ✅ Verification Checklist

Before going live, ensure:
- [ ] Python 3.8+ is installed
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] OpenAI API key is set in `.env`
- [ ] Bot starts without errors (`python glwis_bot.py`)
- [ ] Sample questions are answered correctly
- [ ] Chat history is being saved
- [ ] API costs are monitored

---

## 📊 Performance Tips

1. **Keep FAQ Organized**: Well-structured FAQs = better answers
2. **Regular Updates**: Update FAQ monthly with new policies
3. **Monitor Costs**: Check usage dashboard weekly
4. **Test Thoroughly**: Ask bot various questions before deployment
5. **Backup Data**: Save chat_history.json regularly

---

## 🚀 Next Steps

1. ✅ Follow the Quick Start section above
2. ✅ Test the bot with sample questions
3. ✅ Update FAQ with current school information
4. ✅ Set up on a dedicated machine if using 24/7
5. ✅ Share bot access with school staff/students

---

**Last Updated:** March 10, 2026
**Bot Version:** 1.0
**Status:** Production Ready ✅
