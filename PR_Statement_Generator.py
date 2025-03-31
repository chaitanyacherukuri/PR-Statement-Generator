import streamlit as st
import os
from typing import Literal, TypedDict
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]

#Initialize LLM
llm = ChatGroq(model_name="llama3-70b-8192")

#State dictionary thats keeps track of information throughout the workflow
class State(TypedDict):
    pr_statement: str
    topic: str
    grade: str
    feedback: str

#Schema for structured ouput
class Feedback(BaseModel):
    grade: Literal["good", "needs improvement"] = Field(
        description="Decide if the PR statement is well-formed or needs improvement."
    )

    feedback: str = Field(
        description="If the PR statement needs improvement, provide feedback on how to improve it."
    )

#Augment LLM with schema for structured output
evaluator = llm.with_structured_output(Feedback)

#Node for PR statement generation
def generate_pr_statement(state: State):
    """Generate a PR statement based on the given topic."""

    prompt = f"""
    Generate a compelling PR statement for the topic {state['topic']}. 

    - The statement should highlight key benefits, address any potential concerns, and capture the excitement and innovation surrounding the subject. 
    - Ensure that the tone is professional yet engaging, appealing to the target audience while maintaining clarity and impact."""

    if state.get("feedback"):
        response = llm.invoke(prompt + f" Also take provided feedback into account: {state['feedback']}")
    else:
        response = llm.invoke(prompt)

    return {"pr_statement": response.content}

#Node for evaluating the PR statement
def evaluate_pr_statement(state: State):
    """Evaluate the generated PR statement and provide feedback."""

    prompt = f"""
    Review the following PR statement: {state['pr_statement']}. 
    
    - Assess its clarity, engagement, and overall effectiveness in capturing the key benefits and addressing potential concerns. 
    - Decide whether the statement is well-formed ('good') or if it requires further refinement ('needs improvement'). 
    - If it needs improvement, please provide concise and actionable feedback on how to enhance the statement."""

    decision = evaluator.invoke(prompt)

    return {"grade": decision.grade, 
            "feedback": decision.feedback}

#Conditional edge function to determine the next node based on the grade
def route_statement(state: State):
    """Route to the appropriate node based on the evaluation grade."""

    if state["grade"] == "good":
        return "Accepted"
    else:
        return "Rejected + Feedback"
    
#State graph for the PR statement generation workflow
workflow = StateGraph(State)

#Add Nodes
workflow.add_node("Generate_PR_Statement", generate_pr_statement)
workflow.add_node("Evaluate_PR_Statement", evaluate_pr_statement)

#Add Edges
workflow.add_edge(START, "Generate_PR_Statement")
workflow.add_edge("Generate_PR_Statement", "Evaluate_PR_Statement")
workflow.add_conditional_edges("Evaluate_PR_Statement", route_statement, {"Accepted": END, "Rejected + Feedback": "Generate_PR_Statement"})

#Compile the workflow
graph = workflow.compile()

#Streamlit UI
st.title("📝 AI-Powered PR Statement Generator")

#Add sidebar with workflow diagram
with st.sidebar:
    st.subheader("Workflow Diagram")

    try:
        #Generate Mermaid Workflow Diagram
        mermaid_diagram = graph.get_graph().draw_mermaid_png()

        #Save and Display the Image in the sidebar
        image_path = "workflow_diagram.png"

        with open(image_path, "wb") as f:
            f.write(mermaid_diagram)
        
        st.image(image_path, caption="PR Statement Generation Workflow", use_container_width=True)
    except Exception as e:
        st.error(f"Unable to generate workflow diagram: {e}")
        st.info("The workflow still functions correctly even without the visualization.")

#Main content
st.markdown(
    """
    Welcome to the AI-powered PR Statement Generator! 🚀

    This application helps you create compelling Public Relations (PR) statements for various topics. 
    Simply provide the topic you want to create a PR statement for, and the AI model will generate a refined PR statement for you. 

    Let's get started! 🎉
    """
)

#Get user input for the topic
topic = st.text_input("Enter the Topic for the PR Statement:", "Company's AI-Powered Chatbot Launch")

#Track generation process
if st.button("Generate PR Statement"):
    with st.spinner("Generating optimized PR statement..."):
        #Create columns to show generation process
        col1, col2 = st.columns(2)

        #Initialize state
        progress_placeholder = st.empty()
        progress_placeholder.info("Starting PR statement generation...")

        #Invoke the workflow
        state = graph.invoke({"topic": topic})

        #Show success message
        progress_placeholder.success("PR statement generated successfully!")

        #Display the generated PR statement
        st.subheader("Generated PR Statement:")
        st.write(state["pr_statement"])

st.markdown("---")
st.markdown("### 🔗 Powered by LangGraph, Groq 🚀")