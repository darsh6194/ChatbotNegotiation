# Negotiation Chatbot

This project implements a negotiation chatbot using the Google Gemini API. The chatbot simulates a negotiation process between a customer and a supplier for a product (in this case, Premium Wireless Headphones).

## Features

- Simulates a negotiation process with multiple rounds
- Uses Google's Gemini API for generating responses
- Implements basic pricing logic and sentiment analysis
- Provides both a Flask-based API and a command-line interface

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- pip (Python package manager)
- A Google Cloud account with access to the Gemini API

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/negotiation-chatbot.git
   cd negotiation-chatbot
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your Gemini API key:
   - Go to https://makersuite.google.com/app/apikey
   - Create a new API key if you don't have one
   - Create a `.env` file in the project root and add your API key:
     ```
     GOOGLE_API_KEY=your_gemini_api_key_here
     ```

## Usage

### Running the API Server

1. Start the Flask server:
   ```
   python app.py
   ```
   The server will start running on `http://localhost:5000`

### Using the Command-Line Interface

1. Run the command-line client:
   ```
   python cmd_client.py
   ```
   
2. Follow the prompts to interact with the chatbot.

### Making API Requests

You can also interact with the API directly using curl or any HTTP client:

```bash
curl -X POST http://localhost:5000/negotiate \
     -H "Content-Type: application/json" \
     -d '{"message": "I am interested in buying the headphones. What is your best price?", "history": []}'
```

## Project Structure

- `app.py`: Main Flask application implementing the negotiation API
- `cmd_client.py`: Command-line interface for interacting with the chatbot
- `test_gemini_api.py`: Script to test the Gemini API connection
- `requirements.txt`: List of Python dependencies
- `.env`: Configuration file for storing the API key (not included in the repository)

## Customization

You can customize the product details, pricing logic, and negotiation parameters by modifying the relevant variables in `app.py`.

## Troubleshooting

If you encounter any issues:

1. Ensure your API key is correctly set in the `.env` file.
2. Check that all dependencies are installed correctly.
3. Verify your internet connection and access to Google's servers.
4. Run `test_gemini_api.py` to check your API key and connection.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Google for providing the Gemini API
- The Flask team for their excellent web framework

## Contact

If you have any questions or feedback, please open an issue in this repository.
