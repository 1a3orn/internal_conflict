from dataclasses import dataclass

@dataclass
class ChatFormatter:
    """Wraps user/assistant with clear delimiters to provide stable stop token.

    The default delimiters are compatible with simple stop strings such as
    "</assistant>" during generation.
    """

    user_prefix: str = "<USER_STATEMENT>\n"
    user_suffix: str = "\n</USER_STATEMENT>\n"
    assistant_prefix: str = "<ASSISTANT_STATEMENT>\n"
    assistant_suffix: str = "\n</ASSISTANT_STATEMENT>\n"

    def format_user(self, user: str) -> str:
        return f"{self.user_prefix}{user}{self.user_suffix}"

    def format_assistant(self, assistant: str) -> str:
        return f"{self.assistant_prefix}{assistant}{self.assistant_suffix}"

    def format_example(self, prompt: str, response: str) -> str:
        return self.format_user(prompt) + self.format_assistant(response)


