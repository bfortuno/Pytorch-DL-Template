# PyTorch Deep Learning Training Template

This repository provides a flexible and scalable template for deep learning model training using PyTorch. It is designed for seamless setup and deployment using Docker, Docker Compose, and Visual Studio Code's DevContainer, making it an ideal starting point for machine learning engineers, data scientists, and AI researchers.

## 📦 Project Structure

```
pytorch_template/
├── .gitignore
├── docker-compose.yaml
├── main.py
├── README.md
├── requirements.txt
├── start_jupyter.sh
├── .devcontainer/
│   ├── devcontainer.json
│   └── docker-compose.yml
├── docker/
│   ├── container.py
│   └── Dockerfile
├── experiments/
│   └── exp1.yaml
├── scripts/
│   ├── download_data.sh
│   ├── start_tensorboard.sh
│   └── start_training.sh
└── src/
    └── __init__.py
```

## 🚀 Key Features

* Docker and Docker Compose for isolated, reproducible training environments
* Visual Studio Code DevContainer support for seamless development
* Easy-to-use scripts for data preparation, training, and experiment tracking
* YAML-based experiment configuration for flexibility and reproducibility
* Python-based container management with `docker/container.py`

## 📋 Prerequisites

* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* [Visual Studio Code](https://code.visualstudio.com/)
* VS Code Extensions:

  * Remote - Containers
  * Python

## 🛠️ Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/bfortuno/Pytorch-DL-Template.git
   cd pytorch_template
   ```

2. **Build Docker Image**

   ```bash
   docker-compose build
   ```

3. **Launch DevContainer** (optional, for VS Code users)

   * Open the repository in VS Code
   * Use the `Remote - Containers` extension to reopen the folder in the container

### DevContainer Configuration

The `.devcontainer/` directory provides pre-configured settings for developing inside a Docker container using VS Code. This setup ensures a consistent development environment across different systems, including:

* **Environment Configuration** (`devcontainer.json`): Specifies the base image, extensions, and workspace settings for the container.
* **Docker Compose Integration** (`docker-compose.yml`): Links the VS Code workspace to the services defined in your Docker Compose file, ensuring the code and data are accessible within the container.

**Key Features:**

* Simplified development environment setup
* Consistent dependency management
* Integrated terminal and debugger

**Example Workflow:**

1. Open the repository in VS Code.
2. Reopen the folder in the container (Command Palette: `Remote-Containers: Reopen in Container`).
3. Use the integrated terminal for running training scripts, starting Jupyter notebooks, or debugging.

Ensure that the Docker Compose service names match those used in `docker-compose.yml` to avoid connection issues.

4. **Install Python Dependencies** (if running locally without Docker)

   ```bash
   pip install -r requirements.txt
   ```

## 🚦 Usage Instructions

### Run Jupyter Notebook

```bash
./start_jupyter.sh
```

### Start Training

```bash
./scripts/start_training.sh
```

### Launch TensorBoard

```bash
./scripts/start_tensorboard.sh
```

### Container Management

The `docker/container.py` script provides a simple command-line interface for managing your Docker Compose environment. It supports the following commands:

**Start Container (`start`)**

* Starts the Docker Compose environment in detached mode.

```bash
./docker/container.py start
```

Equivalent to:

```bash
docker compose up -d
```

**Enter Container (`enter`)**

* Opens an interactive shell session inside the specified service container (default: `ai`).

```bash
./docker/container.py enter --service ai
```

Equivalent to:

```bash
docker compose exec ai bash
```

**Stop Container (`stop`)**

* Stops and removes the running Docker Compose environment.

```bash
./docker/container.py stop
```

Equivalent to:

```bash
docker compose down
```

### Error Handling

The script uses the `subprocess.run()` method with `check=True` to ensure that errors in the underlying Docker commands result in immediate termination, providing clear error messages if a command fails.

Ensure to adjust the container name and settings in the Dockerfile and docker-compose.yml for your specific project needs.

## ⚙️ Customization

* Add new datasets to the `data/` directory (create this folder if missing)
* Update `experiments/exp1.yaml` for new training configurations
* Extend the `src/` directory for custom models, data loaders, or utilities

## 🐛 Troubleshooting

* **Container Build Fails:** Check for missing dependencies in `requirements.txt`
* **DevContainer Not Starting:** Verify Docker and Docker Compose are correctly installed
* **Port Conflicts:** Modify exposed ports in `docker-compose.yml`

## 🤝 Contributing

Feel free to open issues or submit pull requests for improvements. Ensure your code is well-documented and follows the project's style.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🔮 Future Work

* Add support for distributed training
* Integrate MLFlow for experiment tracking
* Include automated testing for better reliability

## 💬 Contact

For questions or support, feel free to reach out via GitHub issues or discussions.
