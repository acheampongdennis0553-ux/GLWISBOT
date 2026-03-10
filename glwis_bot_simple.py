"""
GLWIS Academic Bot - Simplified Version without Pandas
Glorious Living Word International School (GLWIS) Academic Assistant
"""

import os
import openai
from typing import Optional

# Configuration
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set")
openai.api_key = API_KEY
MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 400
TEMPERATURE = 0.1

# GLWIS FAQ Data - Simple dict-based instead of pandas CSV
GLWIS_FAQs = {
    "What is GLWIS?": "Glorious Living Word International School (GLWIS) is a private mission school owned by Living word temple in the United Kingdom, located in Beposo in the sekyere-central district in the Ashanti Region. They offer Basic education (Nursery, Kindergarten, Primary and Junior High)",
    "Where is GLWIS located?": "Glorious Living Word International School (GLWIS) is located in Beposo in the sekyere -central district in the Ashanti Region.",
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
    "How do you support students who are struggling financially (extra help)?": "The school support students financially based on the student academic performance thereby giving discounts of some specific fees including Tuition fee, Feeding fee, P.T.A Dues, Entertainment fee, cadet & sports fee, and entertainment fee.",
    "What is the school's strategy for preparing students for BECE (Basic Education Certificate Examination)?": "The school has a well-trained teaching professional which make sure to cover all topics as required by the Ghana education service of which the Basic Education Certificate Examination questions are based on.",
    "What education facilities are available in the school (e.g., science lab, computer lab, library, play area)?": "The school has a modern computer lab, Library and playing area.",
    "What security measures are in place to ensure student safety and or security?": "The school has a land size of 100 ^ 120-meter square which is fully fenced with blocks and iron gates which prevent students and other peoples from coming in and going out of the school premises without authorized permission.",
    "Are there meals provided for students in the school?": "Yes, the school provide lunch to students every day with specific food menu for further enquiries, contact the accounts department on +2330553324378.",
    "What extracurricular activities (sports, clubs, arts) are available in the school?": "The school train student as a cadet officers for students who have the passion to join Ghana Army, police service, prison service fire service and emigration service in the future. Also, the school perform sporting activities which prepare them to participate in the inter schools sporting activities.",
    "How does the school handle conflict between students and enforce discipline?": "The school authorities appoint two or more teachers every week as a teacher on duty who is responsible for leading the teachers and students through the week, whereby solving any misunderstanding between teachers and or students.",
    "What is the school's vision for student development over the next 5 years?": "The school's vision for student development over the next 5 years is not specified in the provided FAQ.",
    "How does the school facilitate communication between teachers and parents?": "The school authorities in collaboration with the executives of the Parents and Teachers Association (P.T.A) usually organize meeting at least twice every term to discuss about the welfare of the students and the teacher of the school. Moreover, teachers are required to communicate frequently with the parents to ensure the betterment of the students.",
    "Are parents involved in school activities or advisory boards?": "Yes, parents are involved in school activities and or advisory boards through their representatives (ie P.T.A executives)",
    "Does the school have a boarding facility?": "No, GLWIS is a day basic education.",
    "How do I contact the school authorities?": "The school authorities can be contact via email at or contact number +233553324378.",
}


class GLWISAcademicBot:
    """Academic chatbot for GLWIS"""
    
    def __init__(self):
        """Initialize the bot with FAQ data"""
        self.faq_context = self._build_faq_context()
        self.system_prompt = self._build_system_prompt()
    
    def _build_faq_context(self) -> str:
        """Build FAQ context from dict"""
        context = ""
        for question, answer in GLWIS_FAQs.items():
            if answer and str(answer).strip():
                context += f"Q: {question}\nA: {answer}\n\n"
        return context
    
    def _build_system_prompt(self) -> str:
        """Build the system prompt for the bot"""
        return """You are a helpful academic assistant for Glorious Living Word International School (GLWIS). 
Your ONLY source of information is the FAQ document provided. You must ONLY answer questions using the exact information 
from the FAQs. If the information is not in the FAQs, politely say you don't have that information and suggest asking 
something else from the FAQ."""
    
    def answer_question(self, user_question: str) -> Optional[str]:
        """
        Generate an answer to a user question based on the FAQ context
        
        Args:
            user_question: The user's question
            
        Returns:
            The bot's response, or None if an error occurred
        """
        if not user_question.strip():
            return "Please ask me a question about GLWIS."
        
        try:
            response = openai.ChatCompletion.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "system", "content": f"Here are the GLWIS FAQs. Use ONLY this information to answer questions:\n\n{self.faq_context}"},
                    {"role": "user", "content": f"Question about GLWIS: {user_question}"}
                ],
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURE,
                presence_penalty=0,
                frequency_penalty=0
            )
            
            return response['choices'][0]['message']['content'].strip()
        
        except Exception as e:
            print(f"Error: {e}")
            return "Sorry, I encountered an error. Please try again."
    
    def display_welcome_message(self) -> None:
        """Display welcome message and instructions"""
        print("\n" + "=" * 60)
        print("🎓 GLWIS ACADEMIC BOT - Welcome!")
        print("=" * 60)
        print("I can answer questions about Glorious Living Word International School")
        print("based on the official FAQ document.")
        print("\nSample questions you can ask:")
        print("  • Where is GLWIS located?")
        print("  • How much is the admission fee?")
        print("  • What is the fee structure?")
        print("  • Do you have boarding facilities?")
        print("  • How can I contact the school?")
        print("  • What extracurricular activities are available?")
        print("  • How does the school handle discipline?")
        print("\n(Type 'exit', 'quit', or 'bye' to stop)\n")
    
    def run_interactive(self) -> None:
        """Run the bot in interactive mode"""
        self.display_welcome_message()
        
        while True:
            try:
                user_input = input("👤 You: ").strip()
                
                if user_input.lower() in ["exit", "quit", "bye"]:
                    print("\n🎓 Bot: Thank you for using the GLWIS Academic Bot! Have a great day! Goodbye!\n")
                    break
                
                if not user_input:
                    print("🎓 Bot: Please ask me a question about GLWIS.\n")
                    continue
                
                response = self.answer_question(user_input)
                if response:
                    print(f"🎓 Bot: {response}\n")
            
            except KeyboardInterrupt:
                print("\n\n🎓 Bot: Thank you for using the GLWIS Academic Bot! Goodbye!\n")
                break


def main():
    """Main entry point"""
    bot = GLWISAcademicBot()
    bot.run_interactive()


if __name__ == "__main__":
    main()
