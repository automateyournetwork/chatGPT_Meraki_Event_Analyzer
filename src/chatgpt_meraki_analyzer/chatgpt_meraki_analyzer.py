import os
import json
import openai
import rich_click as click
import meraki.aio
import asyncio
import urllib3
import requests
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings()

webexToken = os.getenv("WEBEX_TOKEN")
webexRoomId = os.getenv("WEBEX_ROOMID")
openai.api_key = os.getenv("OPENAI_KEY")

class ChatGPT_Meraki_Analyzer():
    def chatgpt_meraki_analyzer(self):
        asyncio.run(self.organizations())
        asyncio.run(self.networks())
        asyncio.run(self.network_events())

    async def get_networks(self,org_id):
        async with meraki.aio.AsyncDashboardAPI() as aiomeraki:
            try:
                my_networks = await aiomeraki.organizations.getOrganizationNetworks(org_id)
                return(my_networks)
            except:
                print("No Networks")                

    async def networks(self):
        async with meraki.aio.AsyncDashboardAPI() as aiomeraki:
            self.network_list = await asyncio.gather(*(self.get_networks(org['id']) for org in self.my_orgs))
        
    async def organizations(self):
        async with meraki.aio.AsyncDashboardAPI() as aiomeraki:
            self.my_orgs = await aiomeraki.organizations.getOrganizations()  

    async def get_network_events(self,network_id):
        async with meraki.aio.AsyncDashboardAPI() as aiomeraki:
            try:
                my_clients = await aiomeraki.networks.getNetworkEvents(network_id)
                return(my_clients)
            except:
                print("No Network Events")

    async def network_events(self):
        results = await asyncio.gather(*(self.get_network_events(network['id']) for hit in self.network_list if hit for network in hit))
        event_descriptions = []
        for hit in results:
            if hit:
                for event in hit['events']:
                    event_descriptions.append(event['description'])

                unique_events = set(event_descriptions)
                print(unique_events)
                for event in unique_events:
                    print(f"I'm asking chatGPT about the event { event }")
                    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                            {"role": "system", "content": "You are a network troubleshooting tool"},
                            {"role": "user", "content": f"Please describe the following network condition { event }"},
                        ]
                    )

                    result = ''
                    for choice in response.choices:
                        result += choice.message.content

                    print(f"We asked chatGPT Please describe the following network condition { event } - here was there response:")
                    print(result)

                    if webexToken:
                        url = "https://webexapis.com/v1/messages"
            
                        payload = json.dumps({
                          "roomId": f"{ webexRoomId }",
                          "text": f"We asked chatGPT Please describe the following network condition { event } - here was there response:"
                        })
                        headers = {
                          'Authorization': f'Bearer { webexToken }',
                          'Content-Type': 'application/json'
                        }
            
                        response = requests.request("POST", url, headers=headers, data=payload)

                        payload = json.dumps({
                          "roomId": f"{ webexRoomId }",
                          "text": f"{ result }"
                        })

                        response = requests.request("POST", url, headers=headers, data=payload)

                    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                            {"role": "system", "content": "You are a chatbot"},
                            {"role": "user", "content": f"Please describe the following network condition { event } and explain it like I'm 5"},
                        ]
                    )

                    result = ''
                    for choice in response.choices:
                        result += choice.message.content

                    print(f"We asked chatGPT Please describe the following network condition { event } and explain it like I'm 5 - here was there response:")
                    print(result)

                    if webexToken:
                        url = "https://webexapis.com/v1/messages"
            
                        payload = json.dumps({
                          "roomId": f"{ webexRoomId }",
                          "text": f"We asked chatGPT Please describe the following network condition { event } and explain it like I'm 5 - here was there response:"
                        })
                        headers = {
                          'Authorization': f'Bearer { webexToken }',
                          'Content-Type': 'application/json'
                        }
            
                        response = requests.request("POST", url, headers=headers, data=payload)

                        payload = json.dumps({
                          "roomId": f"{ webexRoomId }",
                          "text": f"{ result }"
                        })

                        response = requests.request("POST", url, headers=headers, data=payload)

                    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                            {"role": "system", "content": "You are a network troubleshooting tool"},
                            {"role": "user", "content": f"Is the network event { event } a problem with the network?"},
                        ]
                    )

                    result = ''
                    for choice in response.choices:
                        result += choice.message.content

                    print(f"We asked chatGPT Is the network event { event } a problem with the network? - here was there response:")
                    print(result)

                    if webexToken:
                        url = "https://webexapis.com/v1/messages"
            
                        payload = json.dumps({
                          "roomId": f"{ webexRoomId }",
                          "text": f"We asked chatGPT Is the network event { event } a problem with the network? - here was there response:"
                        })
                        headers = {
                          'Authorization': f'Bearer { webexToken }',
                          'Content-Type': 'application/json'
                        }
            
                        response = requests.request("POST", url, headers=headers, data=payload)

                        payload = json.dumps({
                          "roomId": f"{ webexRoomId }",
                          "text": f"{ result }"
                        })

                        response = requests.request("POST", url, headers=headers, data=payload)

                    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                            {"role": "system", "content": "You are a network troubleshooting tool"},
                            {"role": "user", "content": f"How do I troubleshoot a { event } problem with Meraki?"},
                        ]
                    )

                    result = ''
                    for choice in response.choices:
                        result += choice.message.content

                    print(f"We asked chatGPT How do I troubleshoot a { event } problem with Meraki? - here was there response:")
                    print(result)

                    if webexToken:
                        url = "https://webexapis.com/v1/messages"
            
                        payload = json.dumps({
                          "roomId": f"{ webexRoomId }",
                          "text": f"We asked chatGPT How do I troubleshoot a { event } problem with Meraki? - here was there response:"
                        })
                        headers = {
                          'Authorization': f'Bearer { webexToken }',
                          'Content-Type': 'application/json'
                        }
            
                        response = requests.request("POST", url, headers=headers, data=payload)

                        payload = json.dumps({
                          "roomId": f"{ webexRoomId }",
                          "text": f"{ result }"
                        })

                        response = requests.request("POST", url, headers=headers, data=payload)
                    
@click.command()
def cli():
    invoke_class = ChatGPT_Meraki_Analyzer()
    invoke_class.chatgpt_meraki_analyzer()

if __name__ == "__main__":
    cli()
