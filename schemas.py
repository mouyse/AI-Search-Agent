from typing import List

from pydantic import BaseModel, Field


class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The URL to the source")


class AgentResponse(BaseModel):
    """Schema for a response from the agent with answer and sources"""

    answer: str = Field(description="The agent's answer to the query")
    sources: List[Source] = Field(
        default_factory=list,
        description="A list of sources that the agent generated",
    )
