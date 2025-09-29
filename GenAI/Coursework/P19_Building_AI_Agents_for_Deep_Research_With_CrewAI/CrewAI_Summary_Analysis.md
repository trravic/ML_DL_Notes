# Summary 

**Crew AI**
* Lets us to create amazing workflows with AI Agents.
* Build and deploy automated workflows using any LLM and cloud platform.

* Analysing the marketing crew AI - workflow 

The workflow process was initialized with sequential manner - and verbose was marked to true so that process every detailed activity would be logged. 

## **Step 1 - Crew Intialization** 
  
 * marketing_Crew.kickoff -> wwill start the process 
        and crew AI assigns a uniqyue ID to track the execution session, 
        whatever the sub activity ( search/any action items) would get this id assigned.
  

  * Its kind of Distributed id spread over sub-tasks help in tracking at tasks level

## **Step2 - Market researcher Agent**

* Agent was named as market researcher
* It was given a task to research the latest trends in AI Industry 

* Market Researcher makes 6 search tools calls ( using serper - Enables the extraction of various data points from search results) 

These *Queries* was automatically understood by LLMs and it make the queries and produce the organic results through serper dev tools

 ### 2.1 Serper calls - Search 1 - Intial Search 

 * *Query* -> Latest Trends in AI Industry 2024
 * *Purpose* -> Getting an overview of AI trends was the main purpose of the query 
 * *Tool output* -> Found IBM, McKinsey, Coursera articles abt GenAi, agentic AI, MultiModal AI 

 ### 2.2 Serper calls - search 2 - Deep Dive into GenAI 

 * *Query* -> Advancements and key players in generative AI 2024
 * *Purpose* -> Agent reasons it needs more detail on Generative AI specifically
 * *Tool Output* -> Identifies Microsoft, AWS, Google, Meta, NVIDIA as key players

 ### 2.3 Serper calls - search 3 - Deep dive into Multimodal AI

 * *Query* -> Advancements and key players in multimodal AI 2024
 * *Tool Output* -> Finds GPT-4o, Claude 3, Gemini 2.0 as leading multimodal models

 ### 2.4 Serper calls - search 4 - Deep dive into Agentic AI
 * *Query* -> Advancements and key players in agentic AI 2024
 * *Tool Output* -> 

 ### 2.5 Serper calls - search 5 -  Deep dive into Small Language Models

 * *Query* ->  Advancements and key players in Small Language Models (SLMs) 2024
 * *Tool Output* -> Identifies Microsoft Phi-3.5, Meta Llama 3, Mistral models

 ### 2.6 Serper calls - search 6 - Regulatory Results 

 * *Query* -> Ethical implications and regulatory results of AI 2024
 * *Tool Output* -> Finds information about EU AI Act, ethical considerations

## **Step 3: Market Research Final Output** 

* After gathering information through 6 searches, the agent synthesizes everything into a detailed technical report covering:

1.Generative AI
2. Multimodal AI
3. Agentic AI
4. Small Language Models
5. Ethical AI & Regulation

## **Step 4: Taks Completion for researcher** 

* The `research_task` is marked as complete. The output becomes available for the next task.

## **Step 5: Content writer Task - start**

* The second agent (Content Writer) now starts the `write_task`. It receives the Market Researcher's report as context.

## **Step 6: Content Writer Output**

* The writer transforms the technical research report into an engaging blog post for a non-technical audience.

* Added a relatable examples with simplified concepts 

## **Step 7: Crew Completion**

* The entire crew execution finishes. The result variable contains the final blog post from the Content Writer.

      

