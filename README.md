# Groq-Chat-App

This is a simple chatbot application built using Streamlit and Langchain, powered by Groq LLM models. The app allows users to interact with different Groq models, maintaining conversational memory for a more interactive chat experience.

## Features
- Select between different Groq LLM models (`mixtral-8x7b-32768`, `llama2-70b-4096`).
- Maintain conversation history with adjustable memory length.
- Interactive chat interface built with Streamlit.
- Secure API key management using environment variables.

## Installation

### Prerequisites
Ensure you have Python installed (>=3.8). You also need a Groq API key.

### Clone the repository
```sh
git clone https://github.com/RahulRmCoder/Groq-Chat-App.git
cd Groq-Chat-App
```

### Install dependencies
```sh
pip install -r requirements.txt
```

### Set up environment variables
Create a `.env` file and add your Groq API key:
```sh
GROQ_API_KEY=your_api_key_here
```

## Usage
Run the application with:
```sh
streamlit run app.py
```

## Project Structure
```
├── app.py                 # Main application script
├── requirements.txt       # Dependencies
├── .env                   # Environment variables (not to be shared)
├── README.md              # Documentation
```

## Technologies Used
- **Streamlit**: For the interactive UI
- **Langchain**: To structure LLM interactions
- **Groq**: Provides the AI models
- **Dotenv**: For managing environment variables

## Contributing
Feel free to fork this repository and submit pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License.

## Author
Developed by [Rahul Rajasekharanmenon](https://github.com/RahulRmCoder).

