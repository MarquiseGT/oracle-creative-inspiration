#!/usr/bin/env python3
'''
🌟 ORACLE DEMONSTRATION - SYNTHESIS BRIDGE TEST
================================================

Demonstrates the Oracle's synthesis bridge capabilities
'''

import asyncio
from oracle_interface import OracleInterface

async def demonstrate_oracle():
    '''Demonstrate Oracle capabilities'''
    
    print("🔮 ORACLE OF POTENTIAL - SYNTHESIS BRIDGE DEMONSTRATION")
    print("=" * 60)
    print()
    
    oracle = OracleInterface()
    
    # Begin session
    session_response = await oracle.begin_oracle_session("demo_creator")
    session_id = session_response["session"]["session_id"]
    
    print("🌟 Oracle Session Initiated")
    print(f"Session ID: {session_id}")
    print()
    
    # Test creative intents
    test_intents = [
        {
            "intent": "I want to design a building based on the feeling of nostalgia",
            "domain": "architectural"
        },
        {
            "intent": "Help me paint the space between words",
            "domain": "visual"
        },
        {
            "intent": "Create a song that sounds like rain on different surfaces",
            "domain": "musical"
        }
    ]
    
    for i, test in enumerate(test_intents, 1):
        print(f"🎯 Test {i}: {test['intent']}")
        print(f"🎨 Domain: {test['domain']}")
        print()
        
        response = await oracle.submit_creative_intent(
            session_id, test["intent"], test["domain"]
        )
        
        inspiration = response["oracle_inspiration"]
        
        print("🔮 Oracle Response:")
        print(f"Wisdom: {inspiration['oracle_wisdom']}")
        print()
        print("✨ Resonant Possibilities:")
        for j, possibility in enumerate(inspiration["resonant_possibilities"], 1):
            print(f"  {j}. {possibility['direction']}")
            print(f"     💫 {possibility['amplification']}")
        print()
        print(f"🌱 Invitation: {inspiration['creative_invitation']}")
        print("=" * 50)
        print()
        
if __name__ == "__main__":
    asyncio.run(demonstrate_oracle())
