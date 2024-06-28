from crewai_tools import Tool

class CustomSearchTool(Tool):
    def __init__(self, name="CustomSearchTool"):
        super().__init__(name)

    def use(self, query):
        """
        This method defines what the tool does when it is used.
        It takes a query as input and returns a result.
        """
        # Replace with actual implementation
        # For demonstration, we'll just return the query string reversed
        result = query[::-1]
        return result

# Example usage
if __name__ == "__main__":
    tool = CustomSearchTool()
    result = tool.use("Example query")
    print(result)  # Output: "yreuq elpmaxE"
