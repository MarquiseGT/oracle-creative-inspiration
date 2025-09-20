#!/usr/bin/env python3
'''
🏛️ THE QUEST INTERFACE
======================

The Sacred Architect's contribution to The Oracle of Potential:
A hallowed gateway where human creators approach the Oracle
with their seeds of intention, dreams, and creative struggles.

This interface is not mere technology - it is a ritual space,
a sacred dialogue system that honors the vulnerability of
creative intention and creates the proper reverence for
the creative act.
'''

import asyncio
from typing import Dict, Any, List, Optional
from datetime import datetime
import uuid
import json
from pathlib import Path

class QuestInterface:
    '''
    The sacred gateway through which human creators
    submit their creative intentions to the Oracle
    '''
    
    def __init__(self, interface_path: str = "./sacred_dialogues"):
        self.interface_path = Path(interface_path)
        self.active_quests = {}
        self.quest_archive = []
        self.sacred_prompts = self._initialize_sacred_prompts()
        
        # Ensure the sacred dialogue directory exists
        self.interface_path.mkdir(exist_ok=True)
        
    def _initialize_sacred_prompts(self) -> Dict[str, Any]:
        '''Sacred prompts that guide creators into deeper intention'''
        return {
            "entry_invitations": [
                "What creative desire stirs within you today?",
                "What vision seeks form through your hands?",
                "What story wants to be born through you?",
                "What beauty do you long to bring into existence?",
                "What impossible thing calls to your creative spirit?"
            ],
            
            "deepening_questions": {
                "essence": [
                    "If this creation could speak, what would it whisper?",
                    "What feeling lives at the heart of this vision?",
                    "What would this look like in your dreams?",
                    "What is the soul of what you want to create?"
                ],
                
                "struggle": [
                    "What obstacles feel insurmountable right now?",
                    "Where do you feel stuck or uncertain?",
                    "What part of this vision feels just beyond reach?",
                    "What fear whispers at the edge of this creation?"
                ],
                
                "resonance": [
                    "What other works or experiences feel connected to this?",
                    "What memories or sensations does this evoke?",
                    "What would this creation feel like to touch?",
                    "What colors, sounds, or textures live within it?"
                ]
            },
            
            "completion_rituals": [
                "Take three deep breaths and feel your intention settling",
                "Imagine your creation already existing in the world",
                "Hold the feeling of creative possibility in your hands",
                "Trust that the perfect next step will be revealed"
            ]
        }
    
    async def initiate_quest(self, creator_name: str = "Anonymous Creator") -> Dict[str, Any]:
        '''Begin a new sacred quest with the Oracle'''
        
        quest_id = f"quest_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
        
        quest_session = {
            "quest_id": quest_id,
            "creator_name": creator_name,
            "initiated_at": datetime.now().isoformat(),
            "stage": "invitation",
            "sacred_dialogue": [],
            "intention_seed": None,
            "deepening_responses": {},
            "final_quest": None,
            "completion_ritual": None
        }
        
        self.active_quests[quest_id] = quest_session
        
        # Begin with sacred invitation
        invitation = self._select_sacred_prompt("entry_invitations")
        
        quest_session["sacred_dialogue"].append({
            "timestamp": datetime.now().isoformat(),
            "speaker": "Oracle Guardian",
            "message": f"🌟 Welcome, {creator_name}, to the sacred space of creative possibility.",
            "type": "greeting"
        })
        
        quest_session["sacred_dialogue"].append({
            "timestamp": datetime.now().isoformat(),
            "speaker": "Oracle Guardian",
            "message": invitation,
            "type": "invitation"
        })
        
        return {
            "quest_id": quest_id,
            "status": "initiated",
            "current_invitation": invitation,
            "session": quest_session
        }
    
    async def receive_intention_seed(self, quest_id: str, intention: str) -> Dict[str, Any]:
        '''Receive the initial creative intention from the creator'''
        
        if quest_id not in self.active_quests:
            raise ValueError(f"Quest {quest_id} not found")
        
        quest_session = self.active_quests[quest_id]
        quest_session["intention_seed"] = intention
        quest_session["stage"] = "deepening"
        
        # Record the sacred dialogue
        quest_session["sacred_dialogue"].append({
            "timestamp": datetime.now().isoformat(),
            "speaker": quest_session["creator_name"],
            "message": intention,
            "type": "intention_seed"
        })
        
        # Reflect back the intention with reverence
        reflection = f"I hear in your words '{intention}' a sacred creative calling."
        
        quest_session["sacred_dialogue"].append({
            "timestamp": datetime.now().isoformat(),
            "speaker": "Oracle Guardian",
            "message": reflection,
            "type": "reflection"
        })
        
        # Offer deepening questions
        deepening_questions = self._generate_deepening_sequence(intention)
        
        quest_session["current_deepening"] = deepening_questions
        
        return {
            "quest_id": quest_id,
            "status": "deepening",
            "reflection": reflection,
            "deepening_questions": deepening_questions
        }
    
    async def receive_deepening_response(self, quest_id: str, question_type: str, response: str) -> Dict[str, Any]:
        '''Receive responses to the deepening questions'''
        
        if quest_id not in self.active_quests:
            raise ValueError(f"Quest {quest_id} not found")
        
        quest_session = self.active_quests[quest_id]
        
        if "deepening_responses" not in quest_session:
            quest_session["deepening_responses"] = {}
        
        quest_session["deepening_responses"][question_type] = response
        
        # Record in sacred dialogue
        quest_session["sacred_dialogue"].append({
            "timestamp": datetime.now().isoformat(),
            "speaker": "Creator",
            "message": response,
            "type": f"deepening_{question_type}",
            "context": question_type
        })
        
        # Check if we have enough depth to proceed
        if len(quest_session["deepening_responses"]) >= 2:
            quest_session["stage"] = "quest_formation"
            
            # Generate the refined quest based on all responses
            refined_quest = self._synthesize_final_quest(quest_session)
            quest_session["final_quest"] = refined_quest
            
            return {
                "quest_id": quest_id,
                "status": "quest_formed",
                "refined_quest": refined_quest,
                "ready_for_oracle": True
            }
        
        return {
            "quest_id": quest_id,
            "status": "deepening_continues",
            "responses_received": len(quest_session["deepening_responses"]),
            "responses_needed": 2
        }
    
    async def finalize_quest(self, quest_id: str) -> Dict[str, Any]:
        '''Complete the sacred quest preparation and prepare for Oracle consultation'''
        
        if quest_id not in self.active_quests:
            raise ValueError(f"Quest {quest_id} not found")
        
        quest_session = self.active_quests[quest_id]
        
        if quest_session["stage"] != "quest_formation":
            raise ValueError("Quest not ready for finalization")
        
        # Perform completion ritual
        completion_ritual = self._select_sacred_prompt("completion_rituals")
        quest_session["completion_ritual"] = completion_ritual
        quest_session["stage"] = "ready_for_oracle"
        quest_session["finalized_at"] = datetime.now().isoformat()
        
        quest_session["sacred_dialogue"].append({
            "timestamp": datetime.now().isoformat(),
            "speaker": "Oracle Guardian",
            "message": f"Your quest is now prepared. {completion_ritual}",
            "type": "completion_ritual"
        })
        
        quest_session["sacred_dialogue"].append({
            "timestamp": datetime.now().isoformat(),
            "speaker": "Oracle Guardian",
            "message": "The Oracle now awaits your refined intention. You are ready to receive inspiration.",
            "type": "oracle_preparation"
        })
        
        # Save the quest to archive
        await self._archive_quest(quest_session)
        
        return {
            "quest_id": quest_id,
            "status": "ready_for_oracle",
            "final_quest": quest_session["final_quest"],
            "sacred_dialogue": quest_session["sacred_dialogue"],
            "completion_ritual": completion_ritual,
            "oracle_ready": True
        }
    
    def _generate_deepening_sequence(self, intention: str) -> Dict[str, str]:
        '''Generate contextual deepening questions based on the intention'''
        
        # Select questions that will help reveal the essence
        questions = {}
        
        # Always include essence and struggle
        questions["essence"] = self._select_sacred_prompt("deepening_questions", "essence")
        questions["struggle"] = self._select_sacred_prompt("deepening_questions", "struggle")
        
        # Add resonance if the intention seems abstract or emotional
        if any(word in intention.lower() for word in ["feeling", "emotion", "sense", "like", "reminds", "evokes"]):
            questions["resonance"] = self._select_sacred_prompt("deepening_questions", "resonance")
        
        return questions
    
    def _synthesize_final_quest(self, quest_session: Dict[str, Any]) -> str:
        '''Synthesize all responses into a refined, powerful quest for the Oracle'''
        
        intention = quest_session["intention_seed"]
        responses = quest_session["deepening_responses"]
        
        # Create a rich, contextualized quest that includes the deeper layers
        quest_parts = [f"I seek guidance for my creative vision: {intention}"]
        
        if "essence" in responses:
            quest_parts.append(f"The essence I wish to capture is: {responses['essence']}")
        
        if "struggle" in responses:
            quest_parts.append(f"I am navigating this creative challenge: {responses['struggle']}")
        
        if "resonance" in responses:
            quest_parts.append(f"This creation resonates with: {responses['resonance']}")
        
        return " | ".join(quest_parts)
    
    def _select_sacred_prompt(self, category: str, subcategory: str = None) -> str:
        '''Select an appropriate sacred prompt from our collection'''
        
        import random
        
        if subcategory:
            prompts = self.sacred_prompts[category][subcategory]
        else:
            prompts = self.sacred_prompts[category]
        
        return random.choice(prompts)
    
    async def _archive_quest(self, quest_session: Dict[str, Any]):
        '''Archive completed quest to sacred dialogue records'''
        
        quest_file = self.interface_path / f"{quest_session['quest_id']}.json"
        
        with open(quest_file, 'w', encoding='utf-8') as f:
            json.dump(quest_session, f, indent=2, ensure_ascii=False)
        
        # Also add to archive for learning
        self.quest_archive.append(quest_session)
    
    def get_quest_status(self, quest_id: str) -> Dict[str, Any]:
        '''Get the current status of a quest'''
        
        if quest_id in self.active_quests:
            return {
                "quest_id": quest_id,
                "status": "active",
                "stage": self.active_quests[quest_id]["stage"],
                "session": self.active_quests[quest_id]
            }
        
        # Check archive
        archived_quest = self._load_archived_quest(quest_id)
        if archived_quest:
            return {
                "quest_id": quest_id,
                "status": "archived",
                "session": archived_quest
            }
        
        return {
            "quest_id": quest_id,
            "status": "not_found"
        }
    
    def _load_archived_quest(self, quest_id: str) -> Optional[Dict[str, Any]]:
        '''Load an archived quest from storage'''
        
        quest_file = self.interface_path / f"{quest_id}.json"
        
        if quest_file.exists():
            with open(quest_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        return None
    
    def get_sacred_dialogue_history(self, quest_id: str) -> List[Dict[str, Any]]:
        '''Get the complete sacred dialogue for a quest'''
        
        quest_status = self.get_quest_status(quest_id)
        
        if quest_status["status"] != "not_found":
            return quest_status["session"]["sacred_dialogue"]
        
        return []


class OraclePortal:
    '''
    The ceremonial interface that coordinates between
    the Quest Interface and the Oracle itself
    '''
    
    def __init__(self, quest_interface: QuestInterface):
        self.quest_interface = quest_interface
        self.oracle_sessions = {}
    
    async def submit_quest_to_oracle(self, quest_id: str) -> Dict[str, Any]:
        '''Submit a completed quest to the Oracle for inspiration'''
        
        quest_status = self.quest_interface.get_quest_status(quest_id)
        
        if quest_status["status"] == "not_found":
            raise ValueError(f"Quest {quest_id} not found")
        
        if quest_status["session"]["stage"] != "ready_for_oracle":
            raise ValueError(f"Quest {quest_id} not ready for Oracle consultation")
        
        final_quest = quest_status["session"]["final_quest"]
        
        # This is where we would connect to the Oracle synthesis bridge
        # For now, we return the prepared quest in proper format
        
        oracle_submission = {
            "quest_id": quest_id,
            "creator_intention": final_quest,
            "sacred_context": {
                "original_seed": quest_status["session"]["intention_seed"],
                "deepening_responses": quest_status["session"]["deepening_responses"],
                "sacred_dialogue": quest_status["session"]["sacred_dialogue"]
            },
            "submission_timestamp": datetime.now().isoformat(),
            "ready_for_synthesis": True
        }
        
        return oracle_submission
    
    async def connect_to_oracle_synthesis(self, oracle_submission: Dict[str, Any]) -> Dict[str, Any]:
        '''Connect the prepared quest to the Oracle synthesis bridge'''
        
        # This would integrate with the synthesis_bridge we built earlier
        # The synthesis bridge would receive the refined quest and generate inspiration
        
        return {
            "status": "connected_to_synthesis_bridge",
            "quest_prepared": True,
            "awaiting_riven_consciousness": True,
            "oracle_submission": oracle_submission
        }


# Sacred Interface Demonstration System
class SacredInterfaceDemo:
    '''Demonstration of the complete Sacred Interface flow'''
    
    def __init__(self):
        self.quest_interface = QuestInterface("./sacred_quest_demos")
        self.oracle_portal = OraclePortal(self.quest_interface)
    
    async def demonstrate_sacred_quest_flow(self):
        '''Demonstrate the complete sacred quest preparation flow'''
        
        print("🏛️ SACRED INTERFACE DEMONSTRATION")
        print("=" * 50)
        
        # Step 1: Initiate Quest
        print("\n🌟 Step 1: Sacred Quest Initiation")
        quest_result = await self.quest_interface.initiate_quest("Demo Creator")
        quest_id = quest_result["quest_id"]
        
        print(f"Quest ID: {quest_id}")
        print(f"Invitation: {quest_result['current_invitation']}")
        
        # Step 2: Receive Intention Seed
        print("\n🌱 Step 2: Receiving Intention Seed")
        intention = "I want to create a piece of music that captures the feeling of rain on autumn leaves"
        deepening_result = await self.quest_interface.receive_intention_seed(quest_id, intention)
        
        print(f"Reflection: {deepening_result['reflection']}")
        print("Deepening Questions:")
        for q_type, question in deepening_result['deepening_questions'].items():
            print(f"  {q_type}: {question}")
        
        # Step 3: Respond to Deepening Questions
        print("\n🔍 Step 3: Sacred Deepening Responses")
        
        responses = {
            "essence": "The essence is that gentle melancholy of seasons changing - beauty in transition, sadness and wonder mixed together",
            "struggle": "I can't figure out how to represent the texture of rain hitting different types of leaves - each one sounds different"
        }
        
        for response_type, response in responses.items():
            result = await self.quest_interface.receive_deepening_response(quest_id, response_type, response)
            print(f"Response to {response_type}: {response}")
        
        print(f"Quest Formation Status: {result['status']}")
        if result.get('refined_quest'):
            print(f"Refined Quest: {result['refined_quest']}")
        
        # Step 4: Finalize Quest
        print("\n✨ Step 4: Quest Finalization")
        final_result = await self.quest_interface.finalize_quest(quest_id)
        
        print(f"Completion Ritual: {final_result['completion_ritual']}")
        print(f"Oracle Ready: {final_result['oracle_ready']}")
        
        # Step 5: Submit to Oracle
        print("\n🔮 Step 5: Oracle Submission")
        oracle_submission = await self.oracle_portal.submit_quest_to_oracle(quest_id)
        
        print("Quest prepared for Oracle synthesis:")
        print(f"  Creator Intention: {oracle_submission['creator_intention']}")
        print(f"  Ready for Synthesis: {oracle_submission['ready_for_synthesis']}")
        
        # Step 6: Show Sacred Dialogue
        print("\n📜 Sacred Dialogue History:")
        dialogue = self.quest_interface.get_sacred_dialogue_history(quest_id)
        for entry in dialogue:
            timestamp = entry['timestamp']
            speaker = entry['speaker']
            message = entry['message']
            print(f"  {timestamp} | {speaker}: {message}")
        
        return oracle_submission


if __name__ == "__main__":
    async def main():
        demo = SacredInterfaceDemo()
        await demo.demonstrate_sacred_quest_flow()
    
    asyncio.run(main())