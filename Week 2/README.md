# AI Blog Writer

AI Blog Writer is a web application that leverages artificial intelligence to help users generate blog posts on various topics

## Features

- **Custom Blog Generation**: Users can input the topic, select the desired tone, specify length, and add any specific instructions to guide the content generation.
- **Responsive Design**: Built with Bootstrap, the application is fully responsive and user-friendly, suitable for both desktop and mobile users.
- **Dark Mode**: A sleek dark mode interface for comfortable usage in low-light conditions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9 or later
- Flask
- OpenAI
- OpenAI API key

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ai-blog-writer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ai-blog-writer
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   flask run
   ```

The application should now be running on [http://localhost:5000](http://localhost:5000).

## Usage

To use the application, simply navigate to the homepage, fill in the form with your blog post requirements, and click on the "Generate Blog Post" button. The AI will process your request and display a generated blog post based on your specifications.

## Built With

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [Bootstrap](https://getbootstrap.com/) - The front-end framework used for responsive design
- [OpenAI API](https://openai.com/) - The AI model API for content generation
