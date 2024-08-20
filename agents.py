from crewai import Agent
from tools import yt_tool


import os
os.environ["OPENAI_API_KEY"] = "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"
os.environ["OPENAI_MODEL_NAME"]="gpt-3.5.turbo"

print(os.environ["OPENAI_API_KEY"])
## Create a senior blog content researcher

blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verboe=True,
    memory=True,
    backstory=(
       "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion" 
    ),
    tools=[yt_tool],
    allow_delegation=True
)

## creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False


)