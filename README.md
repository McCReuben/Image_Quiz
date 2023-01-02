# Image Quiz Generator

Need to spin up a quick image quiz for an exam? Look no further.

Welcome to Reuben's Image Quiz Generator! This project uses the Google Images SerpApi to generate an Image Quiz on the fly.

## Prerequisites

Before you begin, you will need to have the following tools installed on your computer:

- Python 3
- Flask
- SerpAPI

## Installation

To install the project, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   $ git clone https://github.com/McCReuben/Image_Quiz.git
   ```

2. Navigate to the directory where the project was cloned and create a virtual environment:

```
cd Image_Quiz
python3 -m venv venv
```

3. Make a copy of the example environment variables file, inputing your SerpApi key

   ```bash
    $ cp .env.example .env
   ```

4. Activate the virtual environment:

   ```bash
   $ source venv/bin/activate
   ```

   If using Windows Powershell, run:

   ```bash
   $ . .venv/Scripts/activate
   ```

5. Install the dependencies (you may need to use `pip3` instead):
   ```bash
   $ pip install -r requirements.txt
   ```

## Usage

To use the project, follow these steps:

1. Run the Flask development server:
   ```bash
   $ flask run
   ```
2. Open your web browser and navigate to http://127.0.0.1:5000/ to access the application.
3. Use the form on the page to generate a random fantasy character name. You can specify the length of the name and whether it should be male or female.

## Contributing

To contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make the changes and commit them to your branch.
4. Push the changes to your fork.
5. Open a pull request and describe the changes you have made.
