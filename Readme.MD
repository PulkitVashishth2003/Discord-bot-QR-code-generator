Discord QR Code Generator Bot

A lightweight and efficient Discord bot built with Python that generates QR codes from user-provided text or URLs and displays them directly in Discord as an embedded image.
This project demonstrates real-world Discord bot development, third-party API integration, and secure configuration management.

🚀 Features
• Generate QR codes from text or URLs
• Display QR codes as embedded images (no link previews)
• Simple command-based interaction
• Secure handling of sensitive data using environment variables
• Clean and minimal codebase, easy to extend

🛠 Tech Stack
• Python 3
• discord.py
• python-dotenv
• QR Code API (qrserver.com)

📂 Project Structure
discord-qr-code-bot/
├── bot.py
├── requirements.txt
├── .gitignore
└── README.md

Note: The .env file is intentionally excluded from version control for security reasons.

⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/discord-qr-code-bot.git
cd discord-qr-code-bot

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Create Environment Variables
Create a .env file in the project root:

DISCORD_TOKEN=your_discord_bot_token_here

⚠️ Never commit this file to GitHub.

4️⃣ Run the Bot
python bot.py

You should see:
Logged in as BotName#1234

▶️ Usage

In any Discord text channel where the bot is present:

!qr <text or URL>

Examples
!qr https://google.com

!qr Hello World

The bot will respond with a QR code image embedded directly in Discord.

🔐 Security Practices

Bot token stored in .env
.env excluded via .gitignore
No secrets committed to the repository

📌 Possible Enhancements
• Slash command support (/qr)
• Custom QR size and color options
• Downloadable QR images
• Hosting the bot for 24/7 uptime
• Logging and analytics

📄 License

This project is open-source and free to use for learning and personal projects.

👤 Author

Pulkit Vashishth
Aspiring Software Engineer | Python & Automation Enthusiast

⭐ Why This Project Matters

This project showcases:
• Practical Discord bot development
• API integration skills
• Secure configuration handling
• Clean and maintainable Python code
• Readiness for real-world software projects
