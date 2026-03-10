# GLWIS Academic Bot 🎓

An intelligent academic chatbot for **Glorious Living Word International School (GLWIS)** powered by OpenAI's GPT-3.5.

## Features

- 🤖 **AI-Powered Responses**: Uses OpenAI's GPT-3.5-turbo for intelligent answers
- 📚 **FAQ-Based Knowledge**: Answers questions exclusively from official GLWIS FAQ data
- 💬 **Interactive Chat**: User-friendly command-line interface
- 🔒 **Accurate Information**: Only provides information from the verified FAQ database
- 📋 **Wide Coverage**: Answers questions about:
  - School location and background
  - Admission procedures and fees
  - Fee structure and payment plans
  - Facilities and resources
  - Extracurricular activities
  - Discipline and conduct
  - Parent-teacher communication
  - Contact information

## Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Setup Steps

1. **Clone or navigate to the project directory**:
   ```bash
   cd c:\Users\DENNY\AI\GLWIS
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your OpenAI API key**:
   - **Option A**: Create a `.env` file in the project directory:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```
   - **Option B**: Set the environment variable directly in the script

## Usage

### Run the Interactive Bot

```bash
python glwis_bot.py
```

### Example Queries

```
👤 You: Where is GLWIS located?
🎓 Bot: Glorious Living Word International School (GLWIS) is located in Beposo in the sekyere-central district in the Ashanti Region.

👤 You: What is the fee structure?
🎓 Bot: [Detailed fee breakdown from FAQ]

👤 You: How can I contact the school?
🎓 Bot: The school authorities can be contacted via contact number +233553324378.
```

### Exit the Bot

Type any of the following:
- `exit`
- `quit`
- `bye`
- Press `Ctrl+C`

## Project Structure

```
GLWIS/
├── glwis_bot.py          # Main bot application
├── requirements.txt      # Project dependencies
├── README.md            # This file
└── .env                 # Environment variables (create this)
```

## Configuration

Key configuration parameters in `glwis_bot.py`:

```python
API_KEY = os.getenv("OPENAI_API_KEY", "...")  # Your OpenAI API key
MODEL = "gpt-3.5-turbo"                        # GPT model to use
MAX_TOKENS = 400                               # Max response length
TEMPERATURE = 0.1                              # Lower = more factual
```

## Bot Behavior

- **Answer Source**: Only uses information from the GLWIS FAQ database
- **Response Style**: Factual, accurate, and helpful
- **Limitations**: If information is not in the FAQ, the bot will politely indicate this
- **Safety**: Very low temperature (0.1) ensures consistent, fact-based responses

## API Costs

This bot uses OpenAI's API. Monitor your usage and costs:
- Each question costs a small amount based on tokens used
- Approximately $0.001-0.002 per question with GPT-3.5-turbo

## Troubleshooting

### "API key not found"
- Ensure your OpenAI API key is set in the `.env` file or environment variable

### "Module not found" error
- Run `pip install -r requirements.txt`
- Verify virtual environment is activated

### Bot giving incorrect information
- The bot only uses the FAQ database. Verify the FAQ data is correct in the code.

## Future Enhancements

- [ ] Add more FAQ entries
- [ ] Support for FAQ file uploads
- [ ] Web interface (Flask/Django)
- [ ] Multi-language support
- [ ] Student portal integration
- [ ] PDF document generation
- [ ] Analytics and logging

## Support

For issues or questions about the bot:
- Contact GLWIS: +233553324378
- API Issues: Check OpenAI documentation at https://platform.openai.com/docs

## License

This project is for GLWIS use only.

---

**Made with 🎓 for GLWIS**
