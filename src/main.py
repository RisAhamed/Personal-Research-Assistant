# app.py

import streamlit as st
from src.agent.core import run_agent_orchestrator

def main():
    """The main function for the Streamlit app."""
    
    st.set_page_config(page_title="Personal Research Assistant", page_icon="🤖", layout="wide")
    st.header("🤖 Personal Research Assistant", divider="rainbow")

    # Initialize session state variables if they don't exist
    if 'report' not in st.session_state:
        st.session_state.report = None
    if 'steps' not in st.session_state:
        st.session_state.steps = {}

    topic = st.text_input(
        "Enter the research topic:",
        placeholder="e.g., The impact of AI on the Indian banking sector"
    )

    if st.button("Start Research", type="primary"):
        if topic:
            # Clear previous results when starting new research
            st.session_state.report = None
            st.session_state.steps = {}
            
            # This is where we call our agent's orchestrator
            # We will loop through the updates it yields
            agent_updates = run_agent_orchestrator(topic)
            
            # Create placeholders for real-time updates
            status_placeholder = st.empty()
            plan_placeholder = st.empty()
            steps_placeholder = st.empty()
            
            for update in agent_updates:
                if update["type"] == "status":
                    status_placeholder.info(update["message"])
                elif update["type"] == "plan":
                    with plan_placeholder.container():
                        st.subheader("Research Plan:")
                        st.markdown(update["plan"])
                elif update["type"] == "step_result":
                    # Store the result and update the display
                    st.session_state.steps[update["step"]] = update["result"]
                    with steps_placeholder.container():
                        st.subheader("Execution Progress:")
                        for step_num, result in st.session_state.steps.items():
                            st.text(f"Step {step_num}:")
                            st.info(result)
                elif update["type"] == "final_report":
                    st.session_state.report = update["report"]
                    # Clear the status and progress updates
                    status_placeholder.empty()
                    plan_placeholder.empty()
                    steps_placeholder.empty()
                elif update["type"] == "error":
                    st.error(f"An error occurred at step {update['step']}: {update['error']}")

    # Display the final report if it exists in the session state
    if st.session_state.report:
        st.subheader("Final Research Report")
        st.markdown(st.session_state.report)


if __name__ == '__main__':
    main()