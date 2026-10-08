# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# If your game uses external libraries (like pygame or colorama), 
# include a requirements.txt file and uncomment the next two lines:
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Copy all your game files into the container
COPY . .

# Run your main game script (replace main.py with your actual script name)
CMD ["python", "main.py"]