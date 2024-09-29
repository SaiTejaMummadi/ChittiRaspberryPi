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




## Setting Up SSH Keys

Follow these steps to generate and add your SSH key to GitHub:

1. **Open Terminal**

    You can find Terminal in Applications → Utilities or by using Spotlight (Cmd + Space and type "Terminal").

2. **Generate the SSH Key**

    Run the following command, replacing `your_email@example.com` with your GitHub email address:

    ```bash
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```

3. **Save the SSH Key**

    When prompted with:

    ```bash
    Enter file in which to save the key (/Users/your_user/.ssh/id_rsa):
    ```

    Press Enter to accept the default file location (`/Users/your_user/.ssh/id_rsa`).

4. **Add a Passphrase (Optional)**

    You will be asked to enter a passphrase for your SSH key:

    ```bash
    Enter passphrase (empty for no passphrase):
    ```

    You can either enter a secure passphrase or leave it blank by pressing Enter for no passphrase.

5. **Add the SSH Key to the SSH Agent**

    Start the ssh-agent by running:

    ```bash
    eval "$(ssh-agent -s)"
    ```

    Then, add your SSH private key to the agent:

    ```bash
    ssh-add -K ~/.ssh/id_rsa
    ```

6. **Copy the SSH Key to the Clipboard**

    Copy the SSH public key to your clipboard by running:

    ```bash
    pbcopy < ~/.ssh/id_rsa.pub
    ```

    This will copy the public key to your clipboard so you can easily paste it in the next step.

7. **Add the SSH Key to GitHub**

    - Go to [GitHub.com](https://github.com/).
    - Navigate to **Settings** (click your profile picture in the upper right and select "Settings").
    - Click **SSH and GPG keys** from the sidebar.
    - Click **New SSH key**.
    - In the "Title" field, enter something descriptive like "My Mac SSH Key."
    - In the "Key" field, paste the SSH key (from Step 6).
    - Click **Add SSH key**.

8. **Test the SSH Connection**

    Now test the connection to GitHub to ensure everything is set up correctly:

    ```bash
    ssh -T git@github.com
    ```

    You should see a message like:

    ```bash
    Hi <your_username>! You've successfully authenticated, but GitHub does not provide shell access.
    ```
