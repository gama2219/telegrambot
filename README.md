Telebot: Telegram Bot for Gemini AI Interaction
Telebot is a Python-based project that integrates a Telegram bot with Google's Gemini AI, allowing users to communicate with the AI for personal assistance through Telegram. The project stores user-AI interactions in a SQL database, providing a seamless and persistent chat experience.
Project Structure
The project consists of 6 Python files:

botintegration.py: Manages communication between the Telegram Bot API and Gemini AI API.
databaseconf.py: Handles database creation and functions for database transactions.
flask_.py: Sets up a webhook to receive updates from the Telegram Bot API.
settings.py: Contains configuration variables and instructions for setup.
run.py: The main file that runs the entire program.
celery_.py:  contains Celery task definitions for asynchronous processing.

Setup and Installation
Prerequisites

Python 3.7+
Redis
ngrok or Cloudflare for tunneling

Step-by-step Setup

Install Redis and start the Redis server
# Install Redis (Ubuntu example)
sudo apt-get install redis-server

# Start Redis server
redis-server

Set up tunneling for the webhook
Use ngrok or Cloudflare to create a tunnel from your local server to the internet.
Example with ngrok:ngrok http 5000

Configure settings
Open settings.py and set the following variables:

BOT_API_KEY: Your Telegram Bot API token
GEMINI_API_KEY: Your Google Gemini AI API key
WEBHOOK_URL: The external URL from ngrok or Cloudflare
Add any specific instructions for the Gemini AI


Install required Python packages
pip install -r requirements.txt

Start Celery workers
celery -A celery_tasks worker --loglevel=info

Run the application
python run.py


Usage
Once the bot is running, users can interact with it through Telegram. The bot will process messages, communicate with Gemini AI, and store conversations in the database.
Features

Real-time messaging between Telegram users and Gemini AI
Persistent storage of conversations in SQL database
Asynchronous processing with Celery
Webhook-based updates from Telegram
