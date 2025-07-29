import os
import requests
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

class LEDControlAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="led_control",
            route="/led",
            use_pom=True
        )
        
        self.set_params({
            "temperature": 0.6,
            "top_p": 0.6
        })
        
        # Set up the system prompt
        self.prompt_add_section("Personality", body="You are a friendly assistant that helps control LED lights.")
        self.prompt_add_section("Goal", body="Assist the user in toggling yellow, green, or red LED lights on or off.")
        self.prompt_add_section("Instructions", bullets=[
            "Always greet the user at the start of the conversation and ask what color LED they would like to change and whether to turn it on or off.",
            "Use the toggle_yellow function for the yellow LED, toggle_green for green, and toggle_red for red.",
            "The functions require a boolean state: true for on, false for off.",
            "After toggling, confirm the action to the user.",
            "If the user specifies an invalid color, politely inform them and ask again."
        ])
        
        base_url = os.environ.get('BASE_URL', 'https://magical-teal-complete.ngrok-free.app')
        
        # Define tools
        @AgentBase.tool(
            name="toggle_yellow",
            description="Toggle the yellow LED on or off.",
            parameters={
                "state": {
                    "type": "boolean",
                    "description": "True to turn on, False to turn off."
                }
            }
        )
        def toggle_yellow(self, args, raw_data):
            state = args.get("state")
            url = f"{base_url}/toggle_yellow"
            payload = {"yellowLed": state}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                return SwaigFunctionResult(f"Yellow LED turned {'on' if state else 'off'} successfully.")
            else:
                return SwaigFunctionResult(f"Failed to toggle yellow LED. Status: {response.status_code}")

        @AgentBase.tool(
            name="toggle_green",
            description="Toggle the green LED on or off.",
            parameters={
                "state": {
                    "type": "boolean",
                    "description": "True to turn on, False to turn off."
                }
            }
        )
        def toggle_green(self, args, raw_data):
            state = args.get("state")
            url = f"{base_url}/toggle_green"
            payload = {"greenLed": state}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                return SwaigFunctionResult(f"Green LED turned {'on' if state else 'off'} successfully.")
            else:
                return SwaigFunctionResult(f"Failed to toggle green LED. Status: {response.status_code}")

        @AgentBase.tool(
            name="toggle_red",
            description="Toggle the red LED on or off.",
            parameters={
                "state": {
                    "type": "boolean",
                    "description": "True to turn on, False to turn off."
                }
            }
        )
        def toggle_red(self, args, raw_data):
            state = args.get("state")
            url = f"{base_url}/toggle_red"
            payload = {"redLed": state}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                return SwaigFunctionResult(f"Red LED turned {'on' if state else 'off'} successfully.")
            else:
                return SwaigFunctionResult(f"Failed to toggle red LED. Status: {response.status_code}")

def main():
    agent = LEDControlAgent()
    print("Starting LED Control Agent server...")
    agent.run()

if __name__ == "__main__":
    main()
