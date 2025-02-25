# Step 1: Use an official Python runtime as the base image
FROM python:3.12-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements.txt into the container at /app
COPY requirements.txt /app/

# Step 4: Install the dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the entire current directory (app) into the container's app directory
COPY . /app/

# Step 6: Expose the port your Flask app will run on
EXPOSE 5001

# Step 7: Set the environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001  

# Step 8: Run the Flask app with the correct port
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]

