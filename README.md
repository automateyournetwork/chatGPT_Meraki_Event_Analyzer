# chatGPT_Meraki_Event_Analyzer
A chatGPT / Meraki SDK Python powered event analyzer

## Current API Coverage

Network Events

## Current chatGPT Prompts

### Network Events 

```json

{"role": "system", "content": "You are a network troubleshooting tool"},
{"role": "user", "content": f"Please describe the following ncondition { event }"},

```

```json

{"role": "system", "content": "You are a chatbot"},
{"role": "user", "content": f"Please describe the following network condition { event } and explain it like I'm 5"},

```

```json

{"role": "system", "content": "You are a network troubleshooting tool"},
{"role": "user", "content": f"Is the network event { event } a problem with the network?"}

```

```json

{"role": "system", "content": "You are a network troubleshooting tool"},
{"role": "user", "content": f"How do I troubleshoot a { event } problem with Meraki?"},

```
## Installation

```console
$ python3 -m venv meraki
$ source meraki/bin/activate
(meraki) $ pip install chatgpt_meraki_analyzer
```

## Usage - Environment Variables - IMPORTANT

Please export / setup this environment variable prior to running vivlio

```console
(meraki) $ export MERAKI_DASHBOARD_API_KEY=<Meraki API Token>

```

Also please create a .env file with the following 

* Required
OPENAI_KEY=""

Available from platform.openai.com

** Optional for WebEx Messages

WEBEX_TOKEN=""
WEBEX_ROOMID=""

## Usage - In-line

```console
(meraki) $ chatgpt_meraki_analyzer
```

## Always On Sandbox

This code works with the always on sandbox! 

https://devnetsandbox.cisco.com/RM/Diagram/Index/a9487767-deef-4855-b3e3-880e7f39eadc?diagramType=Topology

```console
export MERAKI_DASHBOARD_API_KEY=fd6dd87d96915f21bc0e0b3d96a866ff0e53e381


```

## Contact

Please contact John Capobianco if you need any assistance
