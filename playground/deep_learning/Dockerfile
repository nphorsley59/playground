# Use Jupyter base image with Python
FROM jupyter/minimal-notebook:latest

# Set environment variables
ENV JUPYTER_ENABLE_LAB=yes
ENV NB_USER=jupyter
ENV NB_UID=1000
ENV NB_GID=100

# Install additional Python packages
RUN pip install --no-cache-dir --upgrade pip \
    h5py \
    gensim \
    gym \
    keras \
    nltk \
    matplotlib \
    tensorflow \
    torch \
    torchvision \
    torchaudio

# Set working directory
WORKDIR /home/$NB_USER/work

# Expose Jupyter Notebook port
EXPOSE 8888

# Start Jupyter Notebook
CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''"]
