"""
GLWIS Academic Bot - Streamlit Interface
Glorious Living Word International School (GLWIS) Academic Assistant
Deployed on Streamlit Cloud
"""

import streamlit as st
import os
import openai
from datetime import datetime
from typing import Optional

# Page configuration
st.set_page_config(
    page_title="GLWIS Academic Bot",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stChatMessage {
        background-color: #f0f0f0;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    .stChatMessage.user {
        background-color: #667eea;
        color: white;
    }
    .header-title {
        color: white;
        text-align: center;
        font-size: 2.5em;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .info-box {
        background-color: rgba(255,255,255,0.95);
        border-left: 4px solid #667eea;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Configuration
API_KEY = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
if not API_KEY:
    st.error("❌ OPENAI_API_KEY not configured. Please add it to Streamlit secrets or environment.")
    st.stop()

openai.api_key = API_KEY
MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 400
TEMPERATURE = 0.1

# GLWIS FAQ Data
GLWIS_FAQs = {
    "What is GLWIS?": "Glorious Living Word International School (GLWIS) is a private mission school owned by Living word temple in the United Kingdom, located in Beposo in the sekyere-central district in the Ashanti Region. They offer Basic education (Nursery, Kindergarten, Primary and Junior High)",
    "Where is GLWIS located?": "Glorious Living Word International School (GLWIS) is located in Beposo in the sekyere-central district in the Ashanti Region.",
    "Is GLWIS private or government school?": "Glorious Living Word International School (GLWIS) is a private mission school owned by Living word temple in the United Kingdom.",
    "Which type of education do they offer?": "Glorious Living Word International School (GLWIS) offer Basic education specifically (Nursery, Kindergarten, Primary and Junior High)",
    "What is the land size of the school?": "The school has a land size of 100 ^ 120-meter square which is fully fenced with blocks and iron gates.",
    "How can I get admission at GLWIS?": "Buy the admission form from the admission office, fill and submit the form and write the entrance examination.",
    "What is the total cost of the admission form/fee at GLWIS?": "Admission fee varies depending on the class category the student will belong to. From Nursery to primary six pays a fee of GHS100 and JHS 1 to 3 pays a fee of GHS120.",
    "What is the total termly fee structure, including tuition fees, Canteen, transport, books, uniforms, and any other fees?": "The total termly fee of the student varies depending on the class and location of the student. Suggested fee categories are summarized below: Tuition Fee: GHS150.00 – GHS250.00 per term, Feeding Fee (Canteen): GHS5.00 – GHS8.00 per day, Transportation Fee: GHS5.00 – GHS15.00 per day, Cadet & Sports Fee: GHS10.00 per term, P.T.A Dues: GHS10.00 per term, Printing Fee (Exams): GHS8.00 - GHS15.00 per term, Entertainment fee: GHs5.00 per term, School Cloth (Thursday wear): GHS45/yard, Cadet uniform: GHS50/yard, T-Shirt (Friday wear): GHS35",
    "What is the maximum class size and the current student-teacher ratio?": "The maximum class size is 25 and teacher to student ratio is 1:5.",
    "Are there any sibling discounts available at GLWIS?": "Yes, there is a discounted fee of three or more siblings.",
    "Are there any payment plans available at GLWIS?": "Yes, there is a payment structure available for parents who can not fully pay all fees at once.",
    "Does the school follow the GES curriculum, British/Cambridge, or a blend of both?": "The school follow the GES curriculum.",
    "What are the school hours?": "The school operates from 7:30 AM to 3:30 PM with break times in between.",
    "Does GLWIS have an online learning platform?": "Information about online learning platforms can be obtained from the school administration office.",
    "What extracurricular activities are available?": "GLWIS offers various extracurricular activities including sports, cultural activities, and educational clubs.",
    "How often are school reports issued?": "School reports are issued at the end of each term (3 terms per academic year).",
    "What is the school's academic performance?": "GLWIS maintains high academic standards with consistent performance in national examinations.",
    "Are there scholarships available?": "Scholarship opportunities may be available. Contact the admission office for more details.",
    "What is the school's approach to special needs education?": "GLWIS is committed to inclusive education and welcomes students with special needs.",
    "How can parents contact the school?": "Parents can contact the school administration office during school hours or send emails through the school's official channels.",
    "What is the school's vision and mission?": "GLWIS aims to provide quality education that develops students' academic, social, and spiritual growth.",
}

def create_system_prompt() -> str:
    """Create the system prompt for the bot"""
    faq_context = "\n\n".join([f"Q: {q}\nA: {a}" for q, a in GLWIS_FAQs.items()])
    return f"""You are GLWIS Academic Bot, a helpful assistant for Glorious Living Word International School (GLWIS).

Your role is to:
1. Answer questions about GLWIS using the provided FAQ information
2. Be helpful, professional, and friendly
3. Provide accurate information about school policies, fees, and procedures
4. Suggest contacting the administration office for questions beyond your knowledge
5. Always maintain a positive and welcoming tone

GLWIS Information Context:
{faq_context}

Remember: If a question is not answered in the FAQs, acknowledge the question and suggest contacting the school directly."""

def answer_question(user_question: str) -> str:
    """Get an answer from OpenAI based on the user's question"""
    try:
        system_prompt = create_system_prompt()
        
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_question}
            ],
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        )
        
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; color: white;'>
        <h2>🎓 GLWIS Bot</h2>
        <p><strong>Glorious Living Word International School</strong></p>
        <p>Academic Assistant</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("📚 Quick Questions")
    
    # Sample questions
    sample_questions = [
        "What is GLWIS?",
        "Where is GLWIS located?",
        "How can I get admission?",
        "What is the school fee structure?",
        "What are the school hours?",
        "Are there scholarships available?"
    ]
    
    for question in sample_questions:
        if st.button(question, key=question):
            st.session_state.messages.append({"role": "user", "content": question})
    
    st.markdown("---")
    st.subheader("ℹ️ About")
    st.info("""
    **GLWIS Academic Bot** helps you get information about:
    - School details and location
    - Admission procedures
    - Fee structure
    - School hours and activities
    - Contact information
    
    For detailed inquiries, please contact the school directly.
    """)
    
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.session_state.conversation_history = []
        st.rerun()

# Main content
st.markdown('<div class="header-title">🎓 GLWIS Academic Bot</div>', unsafe_allow_html=True)
st.markdown('<div class="info-box"><strong>Welcome to GLWIS Academic Assistant</strong><br>Ask me anything about Glorious Living Word International School (GLWIS) - admissions, fees, school information, and more!</div>', unsafe_allow_html=True)

# Chat display
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Input area
col1, col2 = st.columns([6, 1])

with col1:
    user_input = st.chat_input("Ask a question about GLWIS...")

with col2:
    pass  # Spacer for alignment

# Process user input
if user_input:
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.conversation_history.append({
        "role": "user",
        "message": user_input,
        "timestamp": datetime.now().isoformat()
    })
    
    # Get bot response
    with st.spinner("🤔 Thinking..."):
        bot_response = answer_question(user_input)
    
    # Add bot response to chat
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.session_state.conversation_history.append({
        "role": "assistant",
        "message": bot_response,
        "timestamp": datetime.now().isoformat()
    })
    
    # Rerun to display new messages
    st.rerun()

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("📧 Contact: admissions@glwis.edu.gh")
with col2:
    st.caption("📍 Beposo, Sekyere-Central, Ashanti Region")
with col3:
    st.caption("🌐 GLWIS Academic Bot v1.0")
