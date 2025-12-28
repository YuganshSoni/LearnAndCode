from services.chat_service import ChatService

def handle_user_input():
    active = True
    while active:
        user_input = input("Enter your Marketing query : ")
        if user_input == 'q':
            active = False
            break
        chat_service = ChatService()
        llm_response = chat_service.chat_response(user_input)
        print("ai response : ", llm_response, end = "\n")

if __name__ == "__main__":
    handle_user_input()