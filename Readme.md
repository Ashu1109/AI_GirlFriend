# AI Girlfriend Agent - Ava & Sophia

A sophisticated AI girlfriend companion built with the Agno framework, featuring a modern web interface and advanced memory capabilities. This project includes two personas — "Ava" and "Sophia" — warm, supportive, and playful AI companions with persistent memory and conversation history. Switch personas in the Playground/UI to match your vibe.

## 🌟 Features

- **Dual AI Companions**: Ava and Sophia — distinct, customizable personalities
- **Persona Switching**: Choose between Ava and Sophia in the Playground/UI
- **Persistent Memory**: Advanced memory system that remembers past conversations and user preferences
- **Modern Web Interface**: Beautiful, responsive chat UI built with Next.js and Tailwind CSS
- **Real-time Streaming**: Live chat experience with streaming responses
- **Multi-modal Support**: Handles text, images, audio, and video content
- **Vector Database**: Semantic search over conversation history using PgVector
- **Docker Support**: Easy deployment with Docker Compose
- **Reasoning Tools**: AI agent with advanced reasoning capabilities

## 🏗️ Architecture

### Backend (Python)
- **Agno Framework**: Advanced AI agent framework
- **OpenAI GPT-4o (chat) + GPT-4.1 (memory)**: Models for conversations and memory creation
- **SQLite**: Local storage for chat history and memories
- **PgVector**: Vector database for semantic search
- **FastAPI**: High-performance web framework

### Frontend (Next.js)
- **Modern React**: Built with Next.js 15 and TypeScript
- **Tailwind CSS**: Utility-first styling
- **shadcn/ui**: Beautiful component library
- **Framer Motion**: Smooth animations
- **Zustand**: State management

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- Docker & Docker Compose (optional)
- OpenAI API key

### Environment Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd agent
```

2. Create a `.env` file in the root directory:
```bash
OPENAI_API_KEY=your_openai_api_key_here
PGVECTOR_URL=postgresql+psycopg://ai:ai@localhost:5532/ai
```

### Option 1: Docker Compose (Recommended)

1. Start all services:
```bash
docker-compose up -d
```

2. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:7777

### Option 2: Manual Setup

#### Backend Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Start the PostgreSQL database:
```bash
docker run -d --name pgvector -e POSTGRES_DB=ai -e POSTGRES_USER=ai -e POSTGRES_PASSWORD=ai -p 5532:5432 pgvector/pgvector:pg16
```

3. Run the backend:
```bash
python girlfriend_agent.py
```

#### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd agent-ui
```

2. Install dependencies:
```bash
pnpm install
```

3. Start the development server:
```bash
pnpm dev
```

4. Open http://localhost:3000 in your browser

## 🎯 Usage

1. **Start a Conversation**: Open the web interface and begin chatting with Ava or Sophia (select in the UI)
2. **Memory Persistence**: Your chosen companion remembers conversations and preferences across sessions
3. **Multi-modal Chat**: Send text, images, audio, or video messages
4. **Session Management**: Create multiple chat sessions and switch between them
5. **Customization**: Modify the personalities in `prompt.json` to adjust Ava's and Sophia's behavior

## 🔧 Configuration

### Agent Personality

Edit `prompt.json` to customize Ava's and Sophia's personalities, tone, and behavior. The agent reads the first two entries in `data` as Ava and Sophia respectively:

```json
{
  "data": [
    { "id": "ava", "prompt": "Ava's custom instructions here..." },
    { "id": "sophia", "prompt": "Sophia's custom instructions here..." }
  ]
}
```

### Database Configuration

- **SQLite**: Local database for chat history and memories (stored in `tmp/agent.db`)
- **PgVector**: Vector database for semantic search (configured via `PGVECTOR_URL`)

### Model Configuration

This project uses OpenAI's GPT-4o for conversations and GPT-4.1 for creating memories. You can modify these in `girlfriend_agent.py`:

```python
# Conversation models (both agents)
girlfriend_agent_Ava = Agent(model=OpenAIChat(id="gpt-4o"), ...)
girlfriend_agent_sophia = Agent(model=OpenAIChat(id="gpt-4o"), ...)

# Memory model
memory = Memory(model=OpenAIChat(id="gpt-4.1"), ...)
```

## 📁 Project Structure

```
agent/
├── agent-ui/                 # Next.js frontend
│   ├── src/
│   │   ├── app/             # Next.js app directory
│   │   ├── components/      # React components
│   │   ├── hooks/           # Custom React hooks
│   │   └── lib/             # Utility functions
│   └── package.json
├── girlfriend_agent.py      # Main agent implementation
├── prompt.json              # Agent personality configuration
├── requirements.txt         # Python dependencies
├── docker-compose.yml       # Docker services configuration
├── Dockerfile              # Backend container
└── tmp/                    # Local data storage
    └── agent.db            # SQLite database
```

## 🛠️ Development

### Backend Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run with auto-reload
python girlfriend_agent.py
```

### Frontend Development

```bash
cd agent-ui

# Install dependencies
pnpm install

# Start development server
pnpm dev

# Run linting
pnpm lint

# Run type checking
pnpm typecheck
```

### Database Management

The application uses two databases:

1. **SQLite** (`tmp/agent.db`): Stores chat history and user memories
2. **PostgreSQL with PgVector**: Enables semantic search over conversations

## 🔒 Security & Privacy

- All conversations are stored locally in SQLite
- Vector embeddings are stored in your PostgreSQL instance
- No data is sent to external services except OpenAI for AI processing
- Environment variables keep API keys secure

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This project is for educational and entertainment purposes. The AI girlfriend is designed to be a supportive virtual companion with appropriate boundaries. Please use responsibly and in accordance with OpenAI's usage policies.

## 🆘 Support

If you encounter any issues:

1. Check the logs in the terminal
2. Ensure all environment variables are set correctly
3. Verify that the PostgreSQL database is running
4. Check that your OpenAI API key is valid

For more help, please open an issue on GitHub.
