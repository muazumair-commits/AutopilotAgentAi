import time
import random
from google.genai import errors

def generate_with_retry(model_client, model_id, contents, config=None, retries=10, base_delay=3):
    """
    Wraps model.generate_content with an exponential backoff retry mechanism.
    Handles 429 Resource Exhausted errors specifically.
    """
    for attempt in range(retries):
        try:
            if config:
                return model_client.models.generate_content(
                    model=model_id,
                    contents=contents,
                    config=config
                )
            else:
                return model_client.models.generate_content(
                    model=model_id,
                    contents=contents
                )
        except errors.ClientError as e:
            if e.code == 429 or e.status == 'RESOURCE_EXHAUSTED':
                sleep_time = (base_delay * (2 ** attempt)) + random.uniform(0, 1)
                print(f"⚠️ Quota exceeded. Retrying in {sleep_time:.2f}s... (Attempt {attempt+1}/{retries})")
                time.sleep(sleep_time)
            else:
                # Re-raise other client errors
                raise e
        except Exception as e:
            # Catch-all for other potential transient network issues
            print(f"⚠️ Unexpected error: {e}. Retrying... (Attempt {attempt+1}/{retries})")
            time.sleep(2)
    
    raise Exception(f"Failed to generate content after {retries} attempts.")
