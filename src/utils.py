import os
import time
from bytez import Bytez

def generate_with_bytez(prompt, model_id="google/gemini-2.5-flash", system_message=None, max_tokens=2048):
    """
    Generate content using the official Bytez SDK.
    """
    api_key = os.getenv("BYTEZ_API_KEY")
    if not api_key:
        raise ValueError("BYTEZ_API_KEY not found in environment variables")

    sdk = Bytez(api_key)
    model = sdk.model(model_id)
    
    messages = []
    if system_message:
        messages.append({"role": "system", "content": system_message})
    messages.append({"role": "user", "content": prompt})
    
    # Send input to model with retries
    max_retries = 3
    for attempt in range(max_retries):
        try:
            results = model.run(messages)
            
            if results.error:
                error_msg = f"Bytez SDK Error (Attempt {attempt+1}/{max_retries}): {results.error}"
                print(f"[BYTEZ ERROR] {error_msg}")
                # Save error to file for debugging
                with open("bytez_error_log.txt", "a", encoding="utf-8") as f:
                    f.writelines([f"\n--- {time.ctime()} ---\n", str(results.error), "\n"])
                
                if attempt < max_retries - 1:
                    time.sleep(5 * (attempt + 1))
                    continue
                else:
                    raise Exception(f"Bytez SDK Error: {results.error}")
            
            # Extract content from the message object/dict
            output = results.output
            if isinstance(output, dict) and "content" in output:
                return output["content"]
            elif isinstance(output, list) and len(output) > 0:
                if isinstance(output[0], dict) and "content" in output[0]:
                    return output[0]["content"]
                    
            return str(output)
            
        except Exception as e:
            print(f"[BYTEZ EXCEPTION] (Attempt {attempt+1}/{max_retries}): {str(e).encode('ascii', 'ignore').decode()}")
            if attempt < max_retries - 1:
                time.sleep(5 * (attempt + 1))
            else:
                raise e
