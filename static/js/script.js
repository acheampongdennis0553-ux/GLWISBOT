// GLWIS Academic Bot - Web Interface JavaScript

// DOM Elements
const chatForm = document.getElementById('chat-form');
const messageInput = document.getElementById('message-input');
const chatMessages = document.getElementById('chat-messages');
const clearBtn = document.getElementById('clear-btn');
const historyBtn = document.getElementById('history-btn');
const historyModal = document.getElementById('history-modal');
const closeModalBtns = document.querySelectorAll('.close-modal, .close-btn');
const clearHistoryBtn = document.getElementById('clear-history-btn');
const statusIndicator = document.getElementById('status-indicator');
const statusText = document.getElementById('status-text');
const questionButtonsContainer = document.getElementById('question-buttons');

// Check bot status on page load
document.addEventListener('DOMContentLoaded', () => {
    checkBotStatus();
    loadSampleQuestions();
    setupEventListeners();
});

// Setup event listeners
function setupEventListeners() {
    chatForm.addEventListener('submit', handleSendMessage);
    clearBtn.addEventListener('click', clearChat);
    historyBtn.addEventListener('click', openHistory);
    closeModalBtns.forEach(btn => {
        btn.addEventListener('click', closeHistory);
    });
    clearHistoryBtn.addEventListener('click', clearAllHistory);
    
    // Close modal when clicking outside
    historyModal.addEventListener('click', (e) => {
        if (e.target === historyModal) {
            closeHistory();
        }
    });
}

// Check bot status
async function checkBotStatus() {
    try {
        const response = await fetch('/api/status');
        const data = await response.json();
        
        updateStatusIndicator(data.status);
        
        if (data.status === 'ready') {
            statusText.textContent = 'Bot Ready';
        } else if (data.status === 'error') {
            statusText.textContent = 'Bot Error - Check API Key';
            showWarning('⚠️ Bot initialization failed. Make sure you have set OPENAI_API_KEY in your .env file.');
        }
    } catch (error) {
        console.error('Status check failed:', error);
        updateStatusIndicator('error');
        statusText.textContent = 'Connection Error';
    }
}

// Update status indicator
function updateStatusIndicator(status) {
    statusIndicator.className = `status ${status}`;
}

// Load sample questions
async function loadSampleQuestions() {
    try {
        const response = await fetch('/api/sample-questions');
        const data = await response.json();
        
        questionButtonsContainer.innerHTML = '';
        data.questions.forEach(question => {
            const btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'question-btn';
            btn.textContent = question;
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                messageInput.value = question;
                messageInput.focus();
                handleSendMessage(e);
            });
            questionButtonsContainer.appendChild(btn);
        });
    } catch (error) {
        console.error('Failed to load sample questions:', error);
    }
}

// Handle send message
async function handleSendMessage(e) {
    e.preventDefault();
    
    const message = messageInput.value.trim();
    if (!message) return;
    
    // Clear input immediately
    messageInput.value = '';
    messageInput.focus();
    
    // Show user message
    addMessage(message, 'user');
    
    // Hide sample questions
    document.querySelector('.sample-questions').style.display = 'none';
    
    // Send to bot
    try {
        chatForm.classList.add('sending');
        
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        });
        
        const data = await response.json();
        
        if (data.success) {
            addMessage(data.response, 'bot');
        } else {
            addMessage(`Error: ${data.error}`, 'bot');
        }
    } catch (error) {
        console.error('Error sending message:', error);
        addMessage('Sorry, I encountered an error. Please try again.', 'bot');
    } finally {
        chatForm.classList.remove('sending');
    }
}

// Add message to chat
function addMessage(text, sender) {
    const messageEl = document.createElement('div');
    messageEl.className = `message ${sender}`;
    
    const contentEl = document.createElement('div');
    contentEl.className = 'message-content';
    
    // Parse and format bot responses
    if (sender === 'bot') {
        contentEl.innerHTML = formatBotResponse(text);
    } else {
        contentEl.textContent = text;
    }
    
    messageEl.appendChild(contentEl);
    chatMessages.appendChild(messageEl);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Format bot response (handle lists, bold text, etc.)
function formatBotResponse(text) {
    let html = text;
    
    // Escape HTML
    html = document.createElement('div').appendChild(document.createTextNode(html)).parentNode.innerHTML;
    
    // Bold text within ** **
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Line breaks
    html = html.replace(/\n/g, '<br>');
    
    // Links
    html = html.replace(/\[([^\]]+)\]\(([^\)]+)\)/g, '<a href="$2" target="_blank">$1</a>');
    
    return html;
}

// Clear chat
function clearChat() {
    if (confirm('Are you sure you want to clear the chat?')) {
        // Clear messages except welcome message
        const messages = chatMessages.querySelectorAll('.message');
        messages.forEach((msg, index) => {
            if (index > 0) { // Keep welcome message
                msg.remove();
            }
        });
        
        // Show sample questions again
        document.querySelector('.sample-questions').style.display = 'block';
        
        messageInput.focus();
    }
}

// Open history
async function openHistory() {
    try {
        const response = await fetch('/api/history');
        const data = await response.json();
        
        const historyList = document.getElementById('history-list');
        
        if (data.history.length === 0) {
            historyList.innerHTML = '<p style="text-align: center; color: #7f8c8d;">No chat history yet</p>';
        } else {
            historyList.innerHTML = data.history.map(item => `
                <div class="history-item">
                    <strong>You:</strong> ${escapeHtml(item.user)}
                    <strong style="margin-top: 8px; display: block;">Bot:</strong> ${escapeHtml(item.bot.substring(0, 150))}${item.bot.length > 150 ? '...' : ''}
                    <small>${new Date(item.timestamp).toLocaleString()}</small>
                </div>
            `).join('');
        }
        
        historyModal.classList.add('show');
    } catch (error) {
        console.error('Failed to load history:', error);
    }
}

// Close history
function closeHistory() {
    historyModal.classList.remove('show');
}

// Clear all history
async function clearAllHistory() {
    if (confirm('Are you sure you want to clear all chat history? This cannot be undone.')) {
        try {
            const response = await fetch('/api/clear', { method: 'POST' });
            const data = await response.json();
            
            if (data.success) {
                document.getElementById('history-list').innerHTML = 
                    '<p style="text-align: center; color: #7f8c8d;">No chat history yet</p>';
            }
        } catch (error) {
            console.error('Failed to clear history:', error);
        }
    }
}

// Show warning message
function showWarning(message) {
    const warningEl = document.createElement('div');
    warningEl.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: #f39c12;
        color: white;
        padding: 15px 20px;
        border-radius: 6px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        z-index: 2000;
        max-width: 400px;
    `;
    warningEl.textContent = message;
    document.body.appendChild(warningEl);
    
    setTimeout(() => {
        warningEl.remove();
    }, 5000);
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}

// Allow Enter to send (Shift+Enter for new line)
messageInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        chatForm.dispatchEvent(new Event('submit'));
    }
});

// Auto-focus input on page load
window.addEventListener('load', () => {
    messageInput.focus();
});
