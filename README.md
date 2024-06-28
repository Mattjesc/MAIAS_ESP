# Multi AI Agent Systems: Embedded Systems Prototyping

This project demonstrates the setup and use of a Multi-AI Agents for embedded systems prototyping using CrewAI.

**Note:** This project is financially constrained and not ready for production. It is a prototype and does not represent a perfect system. There are many improvements to be made.

## Project Structure

```
MAIAS_ESP/
├── Dockerfile
├── requirements.txt
├── .devcontainer/
│   └── devcontainer.json
├── src/
│   └── MAIAS_EmbeddedSystemsPrototyping/
│       ├── main.py
│       ├── crew.py
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       ├── tools/
│       │   └── custom_tool.py
├── MAIAS_EmbeddedSystemsPrototyping.ipynb
└── README.md
```

### Files and Directories

- `Dockerfile`: Defines the Docker image, including the base image, dependencies, and commands to run the application.
- `requirements.txt`: Lists the Python dependencies needed for the project.
- `.devcontainer/`: Contains the configuration for VSCode Dev Containers.
  - `devcontainer.json`: Configuration file for setting up the development container.
- `src/MAIAS_EmbeddedSystemsPrototyping/`: Source code for the project.
  - `main.py`: Entry point for the application.
  - `crew.py`: Contains crew-related code.
  - `config/`: Configuration files for agents and tasks.
    - `agents.yaml`: Configuration for agents.
    - `tasks.yaml`: Configuration for tasks.
  - `tools/`: Custom tools for the project.
    - `custom_tool.py`: Placeholder for custom tool code.
- `MAIAS_EmbeddedSystemsPrototype.ipynb`: Jupyter notebook file containing project setup and code.
- `README.md`: Project documentation.

## Prerequisites

Before running the project, ensure you have the following installed:

- [Docker](https://www.docker.com/products/docker-desktop)
- [VSCode](https://code.visualstudio.com/)
- [VSCode Remote - Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## Setup and Usage

### Using Docker

1. **Build the Docker Image**:
   Open a terminal in the root directory of your project and run:
   ```sh
   docker build -t maias-embedded-systems-prototype .
   ```

2. **Run the Docker Container**:
   To start the Docker container, run:
   ```sh
   docker run -p 8080:8080 --name maias-embedded-systems-container maias-embedded-systems-prototype
   ```

### Using VSCode Dev Containers

VSCode Dev Containers allow you to develop inside a Docker container, providing a consistent development environment.

1. **Open the Project in VSCode**:
   Open the root directory of your project in VSCode.

2. **Reopen in Container**:
   Click the green button in the bottom-left corner of VSCode, and select **"Remote-Containers: Reopen in Container"**. VSCode will use the `devcontainer.json` configuration to build the Docker image and reopen the project within the container.

#### `.devcontainer/devcontainer.json`

```json
{
  "name": "MAIAS Embedded Systems Prototyping",
  "dockerFile": "../Dockerfile",
  "context": "..",
  "appPort": ["8080:8080"],
  "extensions": [
    "ms-python.python",
    "ms-azuretools.vscode-docker"
  ],
  "settings": {
    "python.pythonPath": "/usr/local/bin/python"
  }
}
```

### Project Workflow

1. **Initialize API Keys**:
   Set your API keys in the environment:
   ```python
   def get_openai_api_key():
       return "Your_OpenAI_API_Key"

   def get_serper_api_key():
       return "Your_Serper_API_Key"

   openai_api_key = get_openai_api_key()
   serper_api_key = get_serper_api_key()

   os.environ["OPENAI_API_KEY"] = openai_api_key
   os.environ["SERPER_API_KEY"] = serper_api_key
   os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
   ```

2. **Define Agents and Tasks**:
   Define your agents and tasks in `main.py`:
   ```python
   from crewai import Agent, Task, Crew, Process
   from crewai_tools import SerperDevTool

   search_tool = SerperDevTool()

   ideation_agent = Agent(
       role='Product Ideation Specialist',
       goal='Identify a viable industry and use case for the product.',
       tools=[search_tool]
   )

   # Define more agents...

   ideation_task = Task(
       description="Prompt the user for the industry or specific use case.",
       expected_output='A validated industry and use case.',
       agent=ideation_agent,
   )

   # Define more tasks...

   embedded_systems_crew = Crew(
       agents=[ideation_agent, ...],  # Add all agents here
       tasks=[ideation_task, ...],  # Add all tasks here
       process=Process.sequential
   )
   ```

3. **Kickoff the Crew**:
   Start the project with initial inputs:
   ```python
   result = embedded_systems_crew.kickoff(inputs={'industry': 'Healthcare', 'use_case': 'Remote Patient Monitoring'})
   ```

4. **Display the Result**:
   Display the result using Markdown:
   ```python
   from IPython.display import Markdown, display
   display(Markdown(result))
   ```

### Notes

- Ensure that all necessary environment variables (e.g., API keys) are set before running the application.
- Modify `agents.yaml` and `tasks.yaml` in the `config` directory to fit your project's specific requirements.

By following this comprehensive guide, you should be able to set up and run your multi-agent AI system for embedded systems prototyping effectively.