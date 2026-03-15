from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import nest_asyncio
from pyngrok import ngrok
import threading

nest_asyncio.apply()

app = FastAPI()

class PromptRequest(BaseModel):
    query: str

# Create an API endpoint
@app.post("/generate")
async def generate_code(request: PromptRequest):
    print(f"Received request from frontend: {request.query}")
    
    # Call the Router Agent to determine task routing
    # Ensure router_agent and session_service are already initialized in memory
    router_session = await session_service.create_session(app_name=router_agent.name, user_id=my_user_id)
    chosen_route = await run_agent_query(router_agent, request.query, router_session, my_user_id, is_router=True)
    chosen_route = chosen_route.strip().replace("'", "")
    
    final_output = ""
    
    if chosen_route == "mycoguard_sequential_combo":
        # Run the three agents sequentially and combine their generated code
        
        auditor_session = await session_service.create_session(app_name=data_auditor_agent.name, user_id=my_user_id)
        auditor_code = await run_agent_query(
            data_auditor_agent,
            "Please write the Python code to load 'mushroom(1).csv', handle missing values, and encode categorical variables.",
            auditor_session,
            my_user_id
        )
        
        forge_session = await session_service.create_session(app_name=classifier_forge_agent.name, user_id=my_user_id)
        forge_code = await run_agent_query(
            classifier_forge_agent,
            f"Based on this preprocessing code:\n{auditor_code}\nWrite the next part of the script to train a Random Forest classifier.",
            forge_session,
            my_user_id
        )
        
        validator_session = await session_service.create_session(app_name=safety_validator_agent.name, user_id=my_user_id)
        validator_code = await run_agent_query(
            safety_validator_agent,
            f"Based on the training code:\n{forge_code}\nWrite the final part of the script to output a Confusion Matrix and strictly check for False Negatives.",
            validator_session,
            my_user_id
        )
        
        # Combine the generated code sections
        final_output = (
            f"# --- Data Auditor ---\n{auditor_code}\n\n"
            f"# --- Classifier Forge ---\n{forge_code}\n\n"
            f"# --- Safety Validator ---\n{validator_code}"
        )
    
    else:
        final_output = "Sorry, the MycoGuard safety pipeline was not triggered."

    print("Code generation completed. Returning results to frontend...")
    return {"status": "success", "generated_code": final_output}

# Insert your NGROK authentication token here
NGROK_AUTH_TOKEN = "paste your NGROK token here "
ngrok.set_auth_token(NGROK_AUTH_TOKEN)

# Start the Ngrok tunnel
public_url = ngrok.connect(8000).public_url
print(f"Public API endpoint: {public_url}/generate")
print("Server started and waiting for frontend requests...")

# Run FastAPI server in a background thread
threading.Thread(
    target=lambda: uvicorn.run(app, host="0.0.0.0", port=8000)
).start()
