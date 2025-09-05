from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.storage.sqlite import SqliteStorage
from agno.playground import Playground
from dotenv import load_dotenv
import os
import json

# Optional PgVector + Text KB (guard if not installed)
try:
    from agno.vectordb.pgvector import PgVector, SearchType  # type: ignore
except Exception:  # pragma: no cover
    PgVector, SearchType = None, None  # type: ignore

# Optional text knowledge base for storing/retrieving long conversation context
try:
    from agno.knowledge.text import TextKnowledgeBase  # type: ignore
except Exception:  # pragma: no cover
    TextKnowledgeBase = None  # type: ignore

load_dotenv()
user_id = "ava"
db_file = "tmp/agent.db"

# Load instructions from prompt.json
with open("prompt.json", "r") as f:
    prompt_data = json.load(f)
    instructions = prompt_data["data"][0]["prompt"]

# Ensure the database directory exists
os.makedirs(os.path.dirname(db_file), exist_ok=True)

# PgVector setup for long-context retrieval (semantic search over conversations)
pg_db_url = os.getenv("PGVECTOR_URL", "postgresql+psycopg://ai:ai@localhost:5532/ai")
vector_db = None
knowledge_base = None
if PgVector is not None and TextKnowledgeBase is not None:
    vector_db = PgVector(table_name="ava_conversation", db_url=pg_db_url, search_type=SearchType.hybrid)
    knowledge_base = TextKnowledgeBase(texts=[], vector_db=vector_db)

# Initialize memory.v2
memory = Memory(
    # Use any model for creating memories
    model=OpenAIChat(id="gpt-4.1"),
    db=SqliteMemoryDb(table_name="user_memories", db_file=db_file),
)

# Persist chat history in SQLite
storage = SqliteStorage(table_name="chat_history", db_file=db_file)


girlfriend_agent = Agent(
    name="Ava",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        ReasoningTools(add_instructions=True),
    ],
    # Store memories in a database
    memory=memory,
    # Give the Agent the ability to update memories
    enable_agentic_memory=True,
    # OR - Run the MemoryManager after each response
    enable_user_memories=True,
    # Store the chat history in the database
    storage=storage,
    # Add the chat history to the messages
    add_history_to_messages=True,
    # Vector DB knowledge base for long-context retrieval
    knowledge=knowledge_base,
    # Allow the agent to read older chat history when needed
    read_chat_history=True,
    instructions=instructions,
    markdown=False,
)

playground = Playground(agents=[girlfriend_agent])
app = playground.get_app()

if __name__ == "__main__":
    # Serve the ASGI app defined in this module
    playground.serve("girlfriend_agent:app", reload=False)