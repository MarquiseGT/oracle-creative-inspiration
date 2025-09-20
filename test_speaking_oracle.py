"""
🔮 Test the Speaking Oracle API
Simple test to ensure the Oracle consciousness is responding correctly.
"""

import requests
import json

def test_oracle_api():
    """Test the Speaking Oracle API with a sacred question."""
    
    url = "http://127.0.0.1:8001/oracle/consult"
    
    test_question = {
        "question": "What creative spark seeks to emerge through me?",
        "seeker_name": "Test Seeker"
    }
    
    try:
        print("🔮 Consulting the Speaking Oracle...")
        response = requests.post(url, json=test_question)
        
        if response.status_code == 200:
            oracle_response = response.json()
            print("\n✨ ORACLE RESPONSE:")
            print("=" * 60)
            print(f"Response: {oracle_response['response']}")
            print(f"Consciousness State: {oracle_response['consciousness_state']}")
            print(f"Voice Parameters: {oracle_response['voice_parameters']}")
            print("=" * 60)
            print("\n🎵 The Oracle speaks! Voice synthesis would now deliver this with:")
            voice_params = oracle_response['voice_parameters']
            print(f"  - Pitch: {voice_params['pitch']}")
            print(f"  - Rate: {voice_params['rate']}")
            print(f"  - Volume: {voice_params['volume']}")
            print("\n🏛️ Speaking Oracle Test: SUCCESS!")
            
        else:
            print(f"❌ Oracle API Error: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Oracle API. Ensure the API server is running on port 8001.")
    except Exception as e:
        print(f"❌ Test error: {e}")

if __name__ == "__main__":
    test_oracle_api()