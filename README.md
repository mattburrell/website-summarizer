# Website Summarizer

A Python-based tool that retrieves the content of a specified website and generates a concise summary using OpenAI's GPT API. This tool is perfect for quickly understanding lengthy articles, blogs, or online resources.

---

## Features

- Fetches and extracts text from any website URL.
- Summarizes the content using OpenAI's GPT-3.5-turbo model.
- Lightweight and easy to use.
- Customizable to focus on specific content (e.g., articles, blog posts).

---

## Tech Stack

- **Python**
- `requests` for fetching website content
- `BeautifulSoup` for HTML parsing
- `python-dotenv` for environment variable management
- OpenAI API for text summarization

---

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mattburrell/website-summarizer.git
   cd website-summarizer
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up OpenAI API Key**

   - Create a `.env` file in the project directory and add your OpenAI API key:

   ```bash
   touch .env
   ```

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Run the Script**
   ```bash
   python main.py
   ```

---

## Usage

1. Enter a website URL when prompted.
2. The tool will fetch the content and provide a concise summary.

---

## Example Output

**Input URL:**  
`https://en.wikipedia.org/wiki/Python_(programming_language)`

**Summary:**  
Python is a high-level, general-purpose programming language known for its simplicity and versatility. It supports multiple programming paradigms and has a vast standard library, making it widely used for various applications such as web development, data analysis, and artificial intelligence.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## Acknowledgments

- Built with the power of [OpenAI](https://openai.com/).
- Web scraping powered by [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/).
