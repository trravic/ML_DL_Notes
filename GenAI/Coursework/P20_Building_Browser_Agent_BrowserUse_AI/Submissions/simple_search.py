import asyncio
import os
import sys
import json
import traceback
from dotenv import load_dotenv

load_dotenv()

from browser_use import Agent, ChatGoogle

async def main():
    try:
        llm = ChatGoogle(model="gemini-flash-latest")
        task = "Search Google for 'what is browser automation' and tell me the top 3 results"
        agent = Agent(task=task, llm=llm)
        history = await agent.run()
        return history
    except Exception as e:
        print(f"Error occurred: {e}")
        traceback.print_exc()
        return None

def history_to_json(history) -> str:
    """Convert any history-like object into JSON safely."""
    def serialize(obj):
        if hasattr(obj, "__dict__"):
            return {k: serialize(v) for k, v in obj.__dict__.items()}
        elif isinstance(obj, list):
            return [serialize(i) for i in obj]
        elif isinstance(obj, dict):
            return {k: serialize(v) for k, v in obj.items()}
        else:
            return obj

    try:
        return json.dumps(serialize(history), indent=2)
    except Exception as e:
        return json.dumps({"error": f"Failed to serialize: {str(e)}"})

if __name__ == "__main__":
    try:
        print("Starting agent...")
        history = asyncio.run(main())

        print("\nRESULT")
        if history:
            # Print summary
            print(f"\nHistory type: {type(history)}")
            print(f"\nHistory content:\n{history}")

            # Print URLs (if available)
            if hasattr(history, "urls"):
                print("\nHistory URLs:", history.urls())

            # JSON dump
            history_json = history_to_json(history)
            print("\nHistory JSON:\n", history_json)

            # Save to file
            with open("history.json", "w") as f:
                f.write(history_json)

    except Exception as e:
        print(f"Error occurred: {e}")
        traceback.print_exc()


'''
( Also saved the entire output in submissions/history.json )
OUTPUT: 
History URLs:
 ['about:blank', 'https://www.google.com/search?q=what+is+browser+automation&udm=14']

History content:
AgentHistoryList(all_results=[ActionResult(is_done=False, success=None, error=None, attachments=None,
 long_term_memory="Searched Google for 'what is browser automation'", extracted_content="Searched Google for 'what is browser automation'", 
 include_extracted_content_only_once=False, metadata=None, include_in_memory=False), 
 ActionResult(is_done=True, success=True, error=None, attachments=[], 
 long_term_memory="Task completed: True - The top 3 Google search results for 'what is browser automation' are:
 \n\n1. **Title:** What is Browser - 858 more characters", extracted_content="The top 3 Google search results for
'what is browser automation' are:\n\n1. **Title:** What is Browser Automation: Tutorial to Get Started\n  
**Source:** BrowserStack (https://www.browserstack.com/guide)\n  
**Snippet:** Browser automation uses software to simulate user interactions with web browsers for automated testing,
data scraping, and repetitive tasks.\n\n2. **Title:** What is Browser Automation? Full Guide for Beginners\n   
**Source:** Browserless (https://www.browserless.io/blog/browser-automation)\n   
**Snippet:** Browser automation is controlling a browser's behavior programmatically, enabling routine tasks, data scraping,
 and website testing.\n\n3. **Title:** What Is Browser Automation: A Complete Tutorial\n   
 **Source:** LambdaTest (https://www.lambdatest.com/learning-hub)\n   **Snippet:** Browser automation refers to the process of 
 automating web browsers to perform repetitive tasks, simulate user interactions, and validate web applications.", 
 include_extracted_content_only_once=False, metadata=None, include_in_memory=False)], 
 
 all_model_outputs=[{'search': {'query': 'what is browser automation', 'search_engine': 'google'}, 'interacted_element': None}, 
 {'done': {'text': "The top 3 Google search results for 'what is browser automation' are:\n\n1. **Title:** What is Browser Automation: Tutorial to Get Started\n
**Source:** BrowserStack (https://www.browserstack.com/guide)\n   
**Snippet:** Browser automation uses software to simulate user interactions with web browsers for automated testing, data scraping, and repetitive tasks.
\n\n2. **Title:** What is Browser Automation? Full Guide for Beginners\n  
**Source:** Browserless (https://www.browserless.io/blog/browser-automation)\n   

**Snippet:** Browser automation is controlling a browser's behavior programmatically, enabling routine tasks, 
data scraping, and website testing.
\n\n3. **Title:** What Is Browser Automation: A Complete Tutorial\n  
 **Source:** LambdaTest (https://www.lambdatest.com/learning-hub)\n   
 **Snippet:** Browser automation refers to the process of automating web browsers to perform repetitive tasks,
   simulate user interactions, and validate web applications.", 'success': True}, 
 'interacted_element': None}])


'''