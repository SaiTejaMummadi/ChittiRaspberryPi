# ChittiRaspberryPi


## Getting Started

### Clone the Repository

Clone the repository using SSH:

```bash
git clone git@github.com:SaiTejaMummadi/ChittiRaspberryPi.git
```

### Setting Up the Development Environment

#### Python Virtual Environment

1. **Create a virtual environment named `chitti_env`:**

    ```bash
    python3 -m venv chitti_env
    ```

2. **Activate the virtual environment:**

    - **On macOS and Linux:**

        ```bash
        source chitti_env/bin/activate
        ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

### Contributing

To contribute to this repository, follow these steps:

1. **Fork the repository.**

2. **Clone your forked repository:**

    ```bash
    git clone git@github.com:your_username/ChittiRaspberryPi.git
    ```

3. **Setting Up the Branches:**

    - **Push to Main:**

        If you have write access to the main repository and need to push directly to the `main` branch:

        ```bash
        git checkout main
        git pull origin main
        # Make your changes
        git add .
        git commit -m "Description of your changes"
        git push origin main
        ```

    - **Push for a Feature:**

        It is recommended to create a new feature branch for your changes:

        ```bash
        git checkout -b feature/your-feature-name
        # Make your changes
        git add .
        git commit -m "Description of your changes"
        git push origin feature/your-feature-name
        ```

4. **Creating a Pull Request:**

    After pushing your feature branch, navigate to the repository on GitHub and create a pull request:

    - Go to your forked repository on GitHub.
    - Click on the "Compare & pull request" button.
    - Provide a descriptive title and description for your pull request.
    - Submit the pull request to the main repository.

## macOS Specific Instructions

If you're using macOS, follow these additional steps to set up your environment:

1. **Install Homebrew (if not already installed):**

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. **Install Python 3:**

    ```bash
    brew install python
    ```

3. **Proceed with the virtual environment setup as described above.**



