FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the source code and requirements file
COPY watch_next.py .
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download the Spacy model
RUN python -m spacy download en_core_web_md

# Start the program
CMD ["python", "watch_next.py"]
