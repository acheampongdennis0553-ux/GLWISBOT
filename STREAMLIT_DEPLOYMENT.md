# 🚀 Streamlit Deployment Guide

## Overview
The GLWIS Academic Bot is now ready to be deployed on Streamlit Cloud for free public access.

## Prerequisites
1. GitHub account with the GLWIS bot repository
2. Streamlit Cloud account (free at https://streamlit.io/cloud)
3. OpenAI API key

## Deployment Steps

### Step 1: Push Code to GitHub ✅
The code is already pushed to GitHub at:
```
https://github.com/acheampongdennis0553-ux/GLWISBOT.git
```

### Step 2: Create Streamlit Cloud Account
1. Go to https://streamlit.io/cloud
2. Sign up with GitHub
3. Authorize Streamlit to access your GitHub repositories

### Step 3: Deploy the App
1. Click "New app"
2. Select repository: `acheampongdennis0553-ux/GLWISBOT`
3. Select branch: `master`
4. Set main file path: `streamlit_app.py`
5. Click "Deploy"

### Step 4: Add OpenAI API Key
1. Go to your app settings
2. Click "Secrets"
3. Add the following:
```toml
OPENAI_API_KEY = "your-openai-api-key-here"
```
4. Save and your app will automatically restart

## App Features
- **Instant Chat Interface**: Beautiful, responsive chat interface
- **FAQ Integration**: Answers based on 23 GLWIS FAQ topics
- **Smart AI Responses**: Uses OpenAI GPT-3.5-turbo for intelligent answers
- **Quick Questions**: Pre-built buttons for common questions
- **Conversation History**: Maintains chat history during session
- **Mobile Friendly**: Works on phones, tablets, and desktop

## File Structure
```
GLWISBOT/
├── streamlit_app.py          # Main Streamlit application
├── glwis_bot_simple.py       # Bot logic (for reference)
├── app.py                     # Flask API (local use)
├── requirements.txt           # Python dependencies
├── .streamlit/
│   ├── config.toml           # Streamlit configuration
│   └── secrets.toml.example  # Secrets template
├── static/                    # Static files (CSS, JS)
├── templates/                 # HTML templates
└── README.md                  # Project documentation
```

## Local Testing (Before Deployment)
To test the Streamlit app locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
copy .env.example .env
# Edit .env and add your OpenAI API key

# Run Streamlit app
streamlit run streamlit_app.py
```

The app will open at `http://localhost:8501`

## Production Configuration
- **Platform**: Streamlit Cloud (Free tier)
- **Runtime**: Python 3.10+
- **Python Packages**: Automatically installed from requirements.txt
- **Secrets Management**: Via Streamlit Cloud dashboard
- **Database**: Session state (in-memory, reset on app reload)
- **Auto-reload**: Enabled when you push to GitHub

## Monitoring & Maintenance
1. **View Logs**: Streamlit Cloud app settings > Logs
2. **Analytics**: Streamlit Cloud dashboard shows usage stats
3. **Updates**: Any push to master branch automatically redeploys
4. **Costs**: Free tier includes up to 3 active apps

## Troubleshooting

### "OPENAI_API_KEY not configured"
- Go to app Settings > Secrets
- Add your OpenAI API key
- Wait for app to restart

### "ModuleNotFoundError"
- Ensure requirements.txt is in repository root
- Check that module names are spelled correctly
- Streamlit Cloud will install from requirements.txt

### App is Loading Slowly
- First load may take up to 60 seconds
- Subsequent loads are much faster due to caching
- Check internet connection and API rate limits

### Secrets Not Showing Up
- Go to app Settings > Edit secrets
- Secrets are **not** checked into GitHub for security
- They're managed only in Streamlit Cloud dashboard

## API Cost Estimates
- **Free tier**: ~$5-10/month with typical usage
- Each chat message uses OpenAI API
- Monitor usage at https://platform.openai.com/account/billing

## Support Resources
- **Streamlit Docs**: https://docs.streamlit.io
- **Streamlit Community**: https://discuss.streamlit.io
- **OpenAI API Docs**: https://platform.openai.com/docs

## Next Steps
1. ✅ Code is pushed to GitHub
2. ✅ Streamlit app file created (streamlit_app.py)
3. 👉 Create Streamlit Cloud account
4. 👉 Deploy from GitHub repository
5. 👉 Add OpenAI API key to secrets
6. 👉 Share public URL with users

## Public URL
After deployment, your app will be available at:
```
https://glwisbot.streamlit.app
```
(or a custom URL you configure)

---
**Status**: Ready for Streamlit Cloud deployment ✅
**Files Updated**: streamlit_app.py, requirements.txt, .streamlit/config.toml
**Next Action**: Create Streamlit Cloud account and deploy
