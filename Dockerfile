# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /Users/tutudaranijo/Downloads/Github_projects/Python_Project/TextSummerzation/Model.py

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 7860

# Run model.py when the container launches
CMD ["python", "./model.py"]
