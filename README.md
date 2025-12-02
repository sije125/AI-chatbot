# Azure OpenAI Chatbot

A conversational AI chatbot powered by Azure OpenAI Service (GPT-3.5-turbo).

## Features
- Real-time chat interface
- Conversation history
- Reset functionality
- Clean, responsive design

## Technologies Used
- **Backend:** Python, Flask
- **AI:** Azure OpenAI Service (GPT-5.0)
- **Frontend:** HTML, CSS, JavaScript
- **Cloud:** Microsoft Azure

## Setup Instructions

### Prerequisites
- Python 3.10+
- Azure account with OpenAI access

### Installation

1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/azure-openai-chatbot.git
cd azure-openai-chatbot
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables

Create `.env` file:
```
AZURE_OPENAI_ENDPOINT=your-endpoint
AZURE_OPENAI_KEY=your-key
DEPLOYMENT_NAME=your-deployment-name
```

5. Run the application
```bash
python app.py
```

6. Open browser to `http://localhost:5000`

## Future Enhancements
- User authentication
- Conversation persistence (database)
- Multiple chat sessions
- File upload for context

## Author
CJ Chairez - [LinkedIn](https://www.linkedin.com/in/christian-cj-chairez/) | 

## License
MIT License