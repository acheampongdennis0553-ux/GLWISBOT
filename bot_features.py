"""
GLWIS Academic Bot - Advanced Features
Includes logging, persistent chat history, and FAQ management
"""

import json
import os
from datetime import datetime
from typing import List, Dict
import pandas as pd
from io import StringIO


class ChatHistory:
    """Manages chat history and statistics"""
    
    def __init__(self, history_file: str = "chat_history.json"):
        """Initialize chat history manager"""
        self.history_file = history_file
        self.conversations: List[Dict] = self._load_history()
    
    def _load_history(self) -> List[Dict]:
        """Load chat history from file"""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Warning: Could not load chat history: {e}")
                return []
        return []
    
    def add_conversation(self, user_question: str, bot_response: str) -> None:
        """Add a conversation to history"""
        self.conversations.append({
            "timestamp": datetime.now().isoformat(),
            "question": user_question,
            "response": bot_response
        })
        self._save_history()
    
    def _save_history(self) -> None:
        """Save chat history to file"""
        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(self.conversations, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Warning: Could not save chat history: {e}")
    
    def get_statistics(self) -> Dict:
        """Get chat history statistics"""
        return {
            "total_conversations": len(self.conversations),
            "first_chat": self.conversations[0]["timestamp"] if self.conversations else None,
            "last_chat": self.conversations[-1]["timestamp"] if self.conversations else None
        }


class FAQManager:
    """Manages FAQ data and updates"""
    
    def __init__(self, faq_file: str = "glwis_faq.csv"):
        """Initialize FAQ manager"""
        self.faq_file = faq_file
        self.faq_data: pd.DataFrame = self._load_faq()
    
    def _load_faq(self) -> pd.DataFrame:
        """Load FAQ from CSV file"""
        if os.path.exists(self.faq_file):
            try:
                return pd.read_csv(self.faq_file)
            except Exception as e:
                print(f"Warning: Could not load FAQ file: {e}")
                return pd.DataFrame(columns=['Questions', 'Answers'])
        return pd.DataFrame(columns=['Questions', 'Answers'])
    
    def add_faq(self, question: str, answer: str) -> None:
        """Add a new FAQ entry"""
        new_entry = pd.DataFrame({
            'Questions': [question],
            'Answers': [answer]
        })
        self.faq_data = pd.concat([self.faq_data, new_entry], ignore_index=True)
        self._save_faq()
    
    def update_faq(self, index: int, question: str = None, answer: str = None) -> None:
        """Update an existing FAQ entry"""
        if 0 <= index < len(self.faq_data):
            if question:
                self.faq_data.at[index, 'Questions'] = question
            if answer:
                self.faq_data.at[index, 'Answers'] = answer
            self._save_faq()
    
    def _save_faq(self) -> None:
        """Save FAQ to CSV file"""
        try:
            self.faq_data.to_csv(self.faq_file, index=False)
        except Exception as e:
            print(f"Warning: Could not save FAQ file: {e}")
    
    def get_faq_context(self) -> str:
        """Get FAQ data formatted as context string"""
        context = ""
        for idx, row in self.faq_data.iterrows():
            if row['Answers'] and str(row['Answers']).strip():
                context += f"Q: {row['Questions']}\nA: {row['Answers']}\n\n"
        return context
    
    def search_faq(self, keyword: str) -> List[Dict]:
        """Search FAQ for keyword"""
        results = []
        keyword_lower = keyword.lower()
        
        for idx, row in self.faq_data.iterrows():
            if keyword_lower in str(row['Questions']).lower() or keyword_lower in str(row['Answers']).lower():
                results.append({
                    'index': idx,
                    'question': row['Questions'],
                    'answer': row['Answers']
                })
        
        return results


class BotConfig:
    """Manages bot configuration"""
    
    def __init__(self, config_file: str = "bot_config.json"):
        """Initialize bot configuration"""
        self.config_file = config_file
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        """Load configuration from file"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except Exception:
                return self._default_config()
        return self._default_config()
    
    def _default_config(self) -> Dict:
        """Get default configuration"""
        return {
            "model": "gpt-3.5-turbo",
            "max_tokens": 400,
            "temperature": 0.1,
            "enable_history": True,
            "enable_logging": True,
            "school_name": "Glorious Living Word International School (GLWIS)",
            "school_contact": "+233553324378"
        }
    
    def save_config(self) -> None:
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save config: {e}")
    
    def get(self, key: str, default=None):
        """Get configuration value"""
        return self.config.get(key, default)


# Example usage
if __name__ == "__main__":
    # Initialize components
    history = ChatHistory()
    faq_manager = FAQManager()
    config = BotConfig()
    
    print("📊 Chat History Statistics:")
    stats = history.get_statistics()
    print(f"  Total conversations: {stats['total_conversations']}")
    print(f"  First chat: {stats['first_chat']}")
    print(f"  Last chat: {stats['last_chat']}")
    
    print("\n⚙️ Bot Configuration:")
    print(f"  Model: {config.get('model')}")
    print(f"  Max tokens: {config.get('max_tokens')}")
    print(f"  Temperature: {config.get('temperature')}")
    
    print("\n📚 FAQ Statistics:")
    print(f"  Total FAQs: {len(faq_manager.faq_data)}")
