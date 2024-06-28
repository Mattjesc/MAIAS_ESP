import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# Function to get API keys
def get_openai_api_key():
    return "Your_OpenAI_API_Key"

def get_serper_api_key():
    return "Your_Serper_API_Key"

# Setting up environment variables
openai_api_key = get_openai_api_key()
serper_api_key = get_serper_api_key()

os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["SERPER_API_KEY"] = serper_api_key
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

# Initialize the search tool
search_tool = SerperDevTool()

# Function to generate Mermaid diagram for the architectural diagram
def generate_architectural_diagram():
    return """
    graph TD;
        A[User] --> B[Embedded Device]
        B --> C[Firmware]
        B --> D[Microcontroller]
        D --> E[Sensor Module]
        D --> F[Communication Module]
        B --> G[Power Supply]
        B --> H[Actuator]
        B --> I[Cloud Server]
        I --> J[Database]
        I --> K[Mobile/PC Application]
    """

# Creating Agents
ideation_agent = Agent(
    role='Product Ideation Specialist',
    goal='Identify a viable industry and use case for the product.',
    verbose=True,
    memory=True,
    backstory=(
        "An experienced professional in product development who excels at "
        "identifying market needs and brainstorming innovative solutions."
    ),
    tools=[search_tool]
)

market_research_agent = Agent(
    role='Market Analyst',
    goal='Conduct market research to understand the problem and pricing.',
    verbose=True,
    memory=True,
    backstory=(
        "A data-driven analyst with a knack for uncovering market trends and consumer behavior."
    ),
    tools=[search_tool]
)

technical_spec_agent = Agent(
    role='Requirements Engineer',
    goal='Develop a detailed requirements specification document.',
    verbose=True,
    memory=True,
    backstory=(
        "An engineer with a strong background in defining technical requirements and documentation."
    ),
    tools=[]
)

solution_architect_agent = Agent(
    role='Solution Architect',
    goal='Design the architecture of the embedded system.',
    verbose=True,
    memory=True,
    backstory=(
        "An expert in embedded systems with extensive experience in hardware and software design."
    ),
    tools=[],
    additional_actions=[
        lambda: f"Architectural Diagram:\n{generate_architectural_diagram()}"
    ]
)

component_selection_agent = Agent(
    role='Component Engineer',
    goal='Select appropriate components and finalize the design.',
    verbose=True,
    memory=True,
    backstory=(
        "A meticulous engineer who excels at choosing the best components for a project."
    ),
    tools=[]
)

test_plan_agent = Agent(
    role='Test Engineer',
    goal='Develop a comprehensive test plan.',
    verbose=True,
    memory=True,
    backstory=(
        "An engineer specializing in validation and verification of hardware and software designs."
    ),
    tools=[]
)

implementation_agent = Agent(
    role='Software Developer',
    goal='Implement the design through detailed coding and programming.',
    verbose=True,
    memory=True,
    backstory=(
        "A skilled software developer with expertise in embedded systems programming."
    ),
    tools=[]
)

documentation_agent = Agent(
    role='Technical Writer',
    goal='Compile final summary documentation for the client.',
    verbose=True,
    memory=True,
    backstory=(
        "An expert in creating clear and comprehensive technical documentation."
    ),
    tools=[]
)

# Creating Tasks
ideation_task = Task(
    description=(
        "Prompt the user for the industry or specific use case. "
        "Validate the use case with the user until a suitable one is found."
    ),
    expected_output='A validated industry and use case.',
    tools=[search_tool],
    agent=ideation_agent,
)

market_research_task = Task(
    description=(
        "Perform online research on the problem the product will solve. "
        "Determine the average price customers would pay for the solution."
    ),
    expected_output='A detailed market research report with problem analysis and pricing.',
    tools=[search_tool],
    agent=market_research_agent,
)

technical_spec_task = Task(
    description=(
        "Create a document outlining the product purpose, block diagram flow, main features, and environmental conditions."
    ),
    expected_output='A detailed technical specification document.',
    tools=[],
    agent=technical_spec_agent,
)

solution_architect_task = Task(
    description=(
        "Develop strategies to build the solution. "
        "Design the firmware, mobile/PC/cloud application architecture. "
        "Create the architectural diagram using Mermaid."
    ),
    expected_output='An architectural diagram and detailed design strategies.',
    tools=[],
    agent=solution_architect_agent,
)

component_selection_task = Task(
    description=(
        "Decide on the components to be used. "
        "Finalize the design."
    ),
    expected_output='A list of selected components and finalized design.',
    tools=[],
    agent=component_selection_agent,
)

test_plan_task = Task(
    description=(
        "Create a test plan covering hardware design validation, software design validation, and production-level testing."
    ),
    expected_output='A comprehensive test plan document.',
    tools=[],
    agent=test_plan_agent,
)

implementation_task = Task(
    description=(
        "Code and program the embedded system according to the design specifications in detail."
    ),
    expected_output='Implemented code and program for the embedded system in detail.',
    tools=[],
    agent=implementation_agent,
)

documentation_task = Task(
    description=(
        "Create user guides, technical details, and final summary documents. "
        "Integrate necessary diagrams (e.g., architectural diagrams) using Mermaid."
    ),
    expected_output='Complete documentation with user guides and technical details.',
    tools=[],
    agent=documentation_agent,
)

# Forming the Crew
embedded_systems_crew = Crew(
    agents=[
        ideation_agent,
        market_research_agent,
        technical_spec_agent,
        solution_architect_agent,
        component_selection_agent,
        test_plan_agent,
        implementation_agent,
        documentation_agent
    ],
    tasks=[
        ideation_task,
        market_research_task,
        technical_spec_task,
        solution_architect_task,
        component_selection_task,
        test_plan_task,
        implementation_task,
        documentation_task
    ],
    process=Process.sequential
)
