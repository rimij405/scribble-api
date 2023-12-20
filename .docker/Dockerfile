# Dockerfile for creating Python server environment.
FROM python:3.12-slim

# Working directory.
WORKDIR /code

# Copy the requirements.
COPY ./requirements.txt /code/requirements.txt

# Install the requirements.
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application source code into the working directory.
COPY ./app /code/app

# Run the entrypoint command.
CMD [ "uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80" ]