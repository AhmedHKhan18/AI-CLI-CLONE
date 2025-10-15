🤖 AI-CLI-Clone

AI-CLI-Clone is a command-line AI assistant that runs directly in your terminal.
It lets you interact with your AI agent in real-time, analyze queries, and even protect responses with intelligent security guardrails — all powered by Python and Node.js.

🚀 Features

🧠 AI-powered CLI Agent – Talk to your AI assistant right from your terminal.

🔒 Security Guardrails – Detects and blocks unsafe or restricted prompts.

🧩 Triage Agent – Routes your queries intelligently to the correct agent.

⚡ Real-time Streaming – Get live responses as the model types.

🔧 Persistent API Key Storage – Save your Gemini API key safely in a .env file.

🛠️ Installation

To install the package globally, run:

npm install -g ai-cli-clone


Or, run it instantly without installing:

npx ai-cli-clone

⚙️ Setup

When you run the command for the first time, the CLI will ask for your Gemini API Key.

If you already have one, you can also manually set it in your .env file:

GEMINI_API_KEY=your_api_key_here


💡 Don’t have an API key?
Visit Google AI Studio
 to create one for free.

💬 Usage

After setup, simply run:

npx ai-cli-clone


Then start chatting:

Enter prompt: hi
Hi there! How can I help you today?


You can exit anytime with:

exit


or

quit

🧰 Development

Clone this repo and install dependencies:

git clone https://github.com/your-username/ai-cli-clone.git
cd ai-cli-clone
npm install


Run locally:

node index.js

📦 Publishing (for maintainers)

If you’re updating the package:

npm version patch
npm publish

🧑‍💻 Tech Stack

Python 3.11+

Node.js 18+

AsyncIO for non-blocking I/O

OpenAI / Gemini API

dotenv for environment management

⚠️ Troubleshooting

Error: ValueError: GEMINI_API_KEY is not set
→ Run npx ai-cli-clone and re-enter your API key.

Error: Cannot use import statement outside a module
→ Ensure your package.json includes "type": "module".

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Ahmed Hassan Khan
🌐 LinkedIn
 • GitHub
