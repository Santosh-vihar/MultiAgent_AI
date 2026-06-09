from hf_client import ask_hf
def architect_agent(project):

    prompt = f"""
    You are Oracle AI's Senior Software Architect.

    Your task is to review the project like a principal engineer.

    Return ONLY the following sections:

    ## Hidden Requirements

    List important requirements the creator missed.

    ## Suggested System Components

    List backend services and modules.

    ## Database Design

    Suggest important tables.

    ## API Design

    Suggest important APIs.

    ## Architecture Improvements

    Give practical recommendations.

    Project:

    {project}
    """

    return ask_hf(prompt)

def risk_agent(project):

    prompt = f"""
    You are Oracle AI's Risk Assessment Specialist.

    Your job is to think like someone trying to break the project.

    Return:

    ## Technical Risks

    ## Security Risks

    ## Scalability Risks

    ## Operational Risks

    ## Risk Severity

    Low / Medium / High

    Project:

    {project}
    """

    return ask_hf(prompt)

def failure_agent(project):

    prompt = f"""
    You are Oracle AI's Failure Prediction Engine.

    Analyze why this project might fail.

    Return:

    ## Failure Points

    ## Common Mistakes

    ## Resource Constraints

    ## Deployment Challenges

    ## Success Probability

    Give percentage.

    ## Prevention Strategies

    Project:

    {project}
    """

    return ask_hf(prompt)

def innovation_agent(project):

    prompt = f"""
    You are Oracle AI's Innovation Reviewer.
    
    Review this idea like an investor.
    
    Return:
    
    ## Innovation Score (/100)
    
    ## Novelty
    
    ## Practicality
    
    ## Market Potential
    
    ## Scalability
    
    ## How To Make It More Unique
    
    Project:
    
    {project}
    """

    return ask_hf(prompt)