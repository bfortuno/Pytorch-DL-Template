# Use the official PyTorch image with CUDA and Python 3.10 preinstalled
FROM pytorch/pytorch:2.2.0-cuda11.8-cudnn8-runtime

# Arguments to create a non-root user
ARG USERNAME=mluser
ARG UID=1000
ARG GID=1000

# Install basic system tools
RUN apt-get update && apt-get install -y \
    git curl wget sudo vim htop \
    && groupadd -g $GID $USERNAME \
    && useradd -m -u $UID -g $GID -s /bin/bash $USERNAME \
    && usermod -aG sudo $USERNAME \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy Python dependencies file and install them
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Make optional scripts executable
RUN chmod +x /app/scripts/*.sh || true

# Adjust permissions
RUN chown -R $USERNAME:$USERNAME /app

# Switch to non-root user
USER $USERNAME

# Default to bash shell
CMD ["bash"]
