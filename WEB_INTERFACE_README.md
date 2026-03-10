# GLWIS Academic Bot - Web Interface

A beautiful, responsive web interface for the GLWIS Academic Chatbot built with Flask, HTML, CSS, and JavaScript.

## 🌐 Features

✨ **Modern Web UI**
- Clean, professional design
- Responsive (works on desktop, tablet, mobile)
- Dark mode support ready
- Smooth animations

💬 **Interactive Chat**
- Real-time messaging
- Message history
- Quick question buttons
- Sample questions
- Clear chat functionality

📊 **Sidebar Information**
- School location
- Contact information
- Quick help guide
- Fast access to key info

⚡ **Performance**
- Instant responses
- Smooth scrolling
- Optimized CSS/JS
- No external CDN dependencies

🔐 **Security**
- HTML escaping to prevent XSS
- CORS headers
- Safe API endpoints
- Environment variable for API key

## 🚀 Quick Start

### Installation

```bash
# 1. Install dependencies (includes Flask)
pip install -r requirements.txt

# 2. Create .env file with your API key
# OPENAI_API_KEY=sk-your-key-here

# 3. Run the web server
python app.py
```

### Access the Bot

Open your web browser and go to:
```
http://localhost:5000
```

That's it! The web interface will load and you can start chatting.

## 📁 File Structure

```
GLWIS/
├── app.py                      # Flask application (main server)
├── glwis_bot.py               # Bot core (used by app.py)
├── requirements.txt           # Python dependencies
│
├── templates/
│   └── index.html             # Main chat interface
│
└── static/
    ├── css/
    │   └── style.css          # All styling
    └── js/
        └── script.js          # Client-side JavaScript
```

## 🎨 Web Interface Sections

### Header
- Bot title and school name
- Real-time status indicator (Ready/Error)
- Professional gradient background

### Main Chat Area
- Message display with auto-scroll
- User messages on the right (blue)
- Bot messages on the left (gray)
- Welcome message with quick tips
- Sample question buttons for quick access

### Input Area
- Text input field with placeholder
- Send button with icon
- Helpful hints below input
- Enter to send, Shift+Enter for new line

### Sidebar
- School location details
- Contact information
- Quick action buttons (Clear, History)
- Help guide

### Modals
- Chat history viewer
- Timestamped conversations
- Clear history option

## 🔧 Configuration

Edit `app.py` to customize:

```python
# Change port
app.run(port=5000)

# Enable/disable debug mode
app.run(debug=True)

# Change host (0.0.0.0 for network access)
app.run(host='0.0.0.0')
```

## 📱 Responsive Breakpoints

- **Desktop (1024px+)**: Full sidebar layout
- **Tablet (768px-1023px)**: Stacked layout
- **Mobile (<768px)**: Single column, hidden sidebar

## 🌟 Usage Tips

### For Users
1. **Quick Questions**: Click sample question buttons
2. **View History**: Click "📋 View History" button
3. **Clear Chat**: Click "🗑️ Clear Chat" to start fresh
4. **Multiple Lines**: Use Shift+Enter for new lines in input

### For Administrators
1. Update FAQ in `glwis_bot.py`
2. Changes apply immediately (restart not needed with debug=False)
3. Check `/api/history` endpoint for API access

## 🔌 API Endpoints

All endpoints return JSON:

### POST `/api/chat`
Send a message to the bot
```json
Request:  { "message": "Where is GLWIS located?" }
Response: { "success": true, "response": "...", "history_count": 5 }
```

### GET `/api/history`
Get all chat history
```json
Response: {
  "history": [
    { "timestamp": "...", "user": "...", "bot": "..." }
  ],
  "total": 5
}
```

### POST `/api/clear`
Clear all chat history
```json
Response: { "success": true, "message": "History cleared" }
```

### GET `/api/sample-questions`
Get sample questions
```json
Response: {
  "questions": ["Where is GLWIS located?", ...]
}
```

### GET `/api/status`
Check bot status
```json
Response: {
  "status": "ready",
  "message": "Bot is ready",
  "api_key_set": true
}
```

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"
```bash
pip install Flask
```

### "Address already in use"
Port 5000 is busy. Change port in `app.py`:
```python
app.run(port=5001)  # Use 5001 instead
```

### API Key Error
1. Check `.env` file exists
2. Verify `OPENAI_API_KEY=sk-...` is set
3. Restart app.py

### Bot Not Responding
1. Check bot status indicator in web UI
2. Run `python test_bot.py` to diagnose
3. Check internet connection

### Styling Not Applied
- Clear browser cache (Ctrl+Shift+Delete)
- Hard refresh (Ctrl+F5)
- Check static folder exists

## 🚀 Deployment

### Local Network Access
Allow other computers on your network to access:

```python
app.run(host='0.0.0.0', port=5000)
```

Then access from another computer:
```
http://your-computer-ip:5000
```

### Production Deployment
For production, use a proper WSGI server:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker (Optional)
Create `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t glwis-bot .
docker run -p 5000:5000 glwis-bot
```

## 📊 Performance Tips

1. **Reduce Request Size**: Short FAQ responses
2. **Cache Static Files**: Browser caching enabled
3. **Optimize Images**: Use compressed assets
4. **Monitor Costs**: Check OpenAI usage dashboard

## 🔒 Security Considerations

- Never commit `.env` file
- Use strong API keys
- Change API key if exposed
- Monitor API usage for fraud
- Sanitize user input (already done)

## 🎨 Customization

### Change Colors
Edit `static/css/style.css`:
```css
:root {
    --primary-color: #2c3e50;        /* Main color */
    --secondary-color: #3498db;      /* Accent color */
    --accent-color: #e74c3c;         /* Error color */
}
```

### Change Title
Edit `templates/index.html`:
```html
<h1>🎓 GLWIS Academic Bot</h1>
```

### Change School Info
Edit `app.py` or `templates/index.html` sidebar

## 📞 Support

**For Bot Issues**: See `SETUP_GUIDE.md`
**For Web Interface Issues**: Check browser console (F12)
**For API Issues**: Check `app.py` logs

## 📈 Future Enhancements

- [ ] Dark mode toggle
- [ ] Export chat as PDF
- [ ] User authentication
- [ ] Analytics dashboard
- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Mobile app wrapper

## 📄 License

Created for GLWIS. Use as needed.

---

**Version:** 1.0
**Status:** ✅ Production Ready
**Access:** http://localhost:5000

Made with 🎓 for Glorious Living Word International School
