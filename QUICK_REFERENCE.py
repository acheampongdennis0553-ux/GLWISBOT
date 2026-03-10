"""
GLWIS Academic Bot - Quick Reference Card
Print this out or keep it handy!
"""

QUICK_START = """
╔════════════════════════════════════════════════════════════════════════╗
║            🎓 GLWIS ACADEMIC BOT - QUICK START CARD 🎓                ║
╚════════════════════════════════════════════════════════════════════════╝

📦 SETUP (5 minutes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣  Install dependencies:
    pip install -r requirements.txt

2️⃣  Create .env file with your API key:
    OPENAI_API_KEY=sk-your-key-here

3️⃣  Start the bot:
    python glwis_bot.py

4️⃣  Ask a question!
    👤 You: Where is GLWIS located?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚙️ VERIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Run tests before using:
    python test_bot.py

Setup wizard:
    python setup_check.py

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💬 SAMPLE QUESTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Location & Info:
    • Where is GLWIS located?
    • What is GLWIS?
    • Is GLWIS a private school?

Admissions:
    • How can I get admission?
    • What is the admission fee?
    • Do I need to write an exam?

Fees & Payments:
    • What is the fee structure?
    • Are there payment plans?
    • Do you offer sibling discounts?

Facilities:
    • What facilities are available?
    • Do you have a computer lab?
    • What about a library?

Activities & Policies:
    • What extracurricular activities?
    • How is discipline handled?
    • Are meals provided?
    • Do you have boarding?

Contact:
    • How can I contact the school?
    • What's the phone number?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 FILES EXPLAINED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MAIN FILES:
  • glwis_bot.py          ⭐ START HERE - The main bot
  • requirements.txt      📦 Dependencies to install
  • .env                  🔑 Your API key (create this)

DOCUMENTATION:
  • README.md             📖 Quick reference
  • SETUP_GUIDE.md        📚 Complete guide (10,000+ words)
  • PROJECT_SUMMARY.md    📋 Overview of everything

ADVANCED:
  • bot_features.py       🛠️  History, FAQ management
  • test_bot.py           🧪 Automated tests
  • setup_check.py        ⚙️  Verification wizard

AUTO-CREATED:
  • chat_history.json     💬 Conversation logs
  • bot_config.json       ⚙️  Bot configuration

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⌨️ BOT COMMANDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Type any question:    Get answer from bot
Type "exit":          Exit bot
Type "quit":          Exit bot
Type "bye":           Exit bot
Ctrl+C:               Force exit

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🐛 TROUBLESHOOTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Problem              Solution
────────────────────────────────────────────────────────────────────
No module error      pip install -r requirements.txt

API key error        Create .env file with API key

Bot not responding   Check internet connection

Wrong information    FAQ data needs updating

Connection timeout   Try again or check OpenAI status

See SETUP_GUIDE.md for more troubleshooting!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📞 GLWIS CONTACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phone: +233553324378
Location: Beposo, Sekyere-Central, Ashanti Region, Ghana

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💰 COST ESTIMATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Light usage (100 q/month):      ~$0.50/month
Medium usage (1,000 q/month):   ~$5/month
Heavy usage (10,000 q/month):   ~$50/month

Monitor at: https://platform.openai.com/account/usage/overview

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ KEY FEATURES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ 24/7 Availability
✅ Instant Responses (< 2 seconds)
✅ Accurate Information (FAQ-based)
✅ Natural Language Understanding
✅ Chat History Logging
✅ Easy to Update FAQ
✅ Production-Ready Code
✅ Well-Documented

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📖 GETTING HELP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Quick answers:     README.md
Detailed help:     SETUP_GUIDE.md (10,000+ words)
Project overview:  PROJECT_SUMMARY.md
Test bot:          python test_bot.py
Setup wizard:      python setup_check.py

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎓 Status: ✅ PRODUCTION READY
Version: 1.0
Last Updated: March 10, 2026

╔════════════════════════════════════════════════════════════════════════╗
║  Ready to go? Run: python glwis_bot.py                                 ║
║  Questions? See: SETUP_GUIDE.md or PROJECT_SUMMARY.md                 ║
║  Not working? Run: python test_bot.py                                  ║
╚════════════════════════════════════════════════════════════════════════╝
"""

if __name__ == "__main__":
    print(QUICK_START)
