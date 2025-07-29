# LED Control Agent

This project is a SignalWire AI Agent built using the SignalWire Agents SDK. It allows users to interact with the agent to toggle yellow, green, or red LED lights on or off via webhooks.

The agent greets the user and asks which color LED they would like to change and whether to turn it on or off. It uses specified webhook endpoints to control the LEDs.


## Run on Replit

[![Run on Replit](https://replit.com/badge?caption=Run%20on%20Replit&color=3b82f6&variant=plain&logo=true&radius=6&theme=light)](https://replit.com/github/Len-PGH/2025)

Click the badge above to import and run this repository directly on Replit.

## Setup and Dependencies

- Python 3
- Required packages: `signalwire-agents`, `requests`

Install dependencies with:

```
pip install signalwire-agents requests
```


## Environment Variables

Set the `BASE_URL` environment variable to the base URL of the LED control service (default: `https://magical-teal-complete.ngrok-free.app`).

On Replit, you can set this in the Secrets tab or in the `.replit` file under `[env]`.

## Running the Agent

The agent server runs and listens for interactions. The system prompt is configured with temperature 0.6 and top_p 0.6.

To run locally:

```
python agent.py
```

