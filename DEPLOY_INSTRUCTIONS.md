# 🚀 Deploy GLWIS Bot to Streamlit Cloud - Step-by-Step

## ⚠️ Current Status
- ✅ Code pushed to GitHub: https://github.com/acheampongdennis0553-ux/GLWISBOT
- ❌ **NOT YET** deployed to Streamlit Cloud

## 🎯 Quick Deploy (5 Minutes)

### Step 1: Go to Streamlit Cloud
1. Open: https://streamlit.io/cloud
2. Click **"Sign in with GitHub"**
3. Use account: `acheampongdennis0553-ux`

### Step 2: Create New App
1. Click **"New app"** button (top-left)
2. **Repository**: `acheampongdennis0553-ux/GLWISBOT`
3. **Branch**: `master`
4. **Main file path**: `streamlit_app.py`
5. Click **"Deploy"** button

### Step 3: Wait for Deployment
- Takes 2-5 minutes
- Watch the deployment logs
- When done, you'll see the live app

### Step 4: Add Your OpenAI API Key
1. Click **⋮ (menu)** in top-right
2. Select **"Settings"**
3. Go to **"Secrets"** tab
4. Paste this:
```toml
OPENAI_API_KEY = "sk-proj-YOUR-API-KEY-HERE"
```
5. Click **"Save"**
6. App will auto-restart

### Step 5: Copy Your Live Link
- URL format: `https://glwisbot-RANDOMSTRING.streamlit.app`
- Share this link with anyone!

---

## ✅ After Deployment

Your app will be live at:
```
https://glwisbot-[randomstring].streamlit.app
```

**Features Available:**
- 💬 Real-time chat
- 🎓 23 GLWIS FAQ answers
- 📱 Mobile-friendly
- ⚡ Instant responses

---

## 🔧 Troubleshooting

### "App not found"
- Wait 2-3 minutes for initial deployment
- Refresh the page
- Check deployment logs in Streamlit Cloud

### "OPENAI_API_KEY not configured"
- Go to app Settings > Secrets
- Add your API key exactly as shown above
- Wait for auto-restart (30 seconds)

### "Module not found"
- Check `requirements.txt` is in repository root
- Verify GitHub repo has `streamlit_app.py` file
- Try redeploying from Streamlit Cloud

### "Authentication error"
- Sign out and sign back in with `acheampongdennis0553-ux` account
- Check GitHub account has access to GLWISBOT repo

---

## 📋 Verify Before Deploying

✅ Check these are on GitHub:
- [ ] `streamlit_app.py` - Main app file
- [ ] `requirements.txt` - Has `streamlit>=1.28.0`
- [ ] `.streamlit/config.toml` - Configuration
- [ ] `glwis_bot_simple.py` - Bot engine
- [ ] `.gitignore` - Excludes secrets

✅ Code Status:
- [ ] No hardcoded API keys
- [ ] All imports work
- [ ] `.env` file NOT in repo

---

## 🎉 Success Indicators

When deployed successfully, you'll see:
1. ✅ No error messages
2. ✅ Chat input box appears
3. ✅ Sample questions visible
4. ✅ Can type and get responses

---

## 📞 Need Help?

**Streamlit Support**: https://discuss.streamlit.io
**GitHub Repo**: https://github.com/acheampongdennis0553-ux/GLWISBOT
**OpenAI API**: https://platform.openai.com/account/billing

---

## 💡 Pro Tips

1. **Share the link** - Anyone can use it, no login needed
2. **Monitor costs** - Check OpenAI usage at platform.openai.com
3. **Auto-redeploy** - Any GitHub push auto-redeploys (within minutes)
4. **Custom domain** - Optional paid feature in Streamlit Cloud

---

**Ready? Go to:** https://streamlit.io/cloud

Click **"New app"** and follow Step 1-5 above! 🚀
