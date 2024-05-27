import websocket
import json

sys_instruct = """You are a network graph maker who extracts terms and their relations from a given context. You are provided with a context chunk (delimited by ```) Your task is to extract the ontology of terms mentioned in the given context. These terms should represent the key concepts as per the context.

Thought 1: While traversing through each sentence, Think about the key terms mentioned in it.

    Terms may include object, entity, location, organization, person,

    condition, acronym, documents, service, concept, etc.

    Terms should be as atomistic as possible


Thought 2: Think about how these terms can have one on one relation with other terms.
    
    Terms that are mentioned in the same sentence or the same paragraph are typically related to each other.

    Terms can be related to many other terms


Thought 3: Find out the relation between each such related pair of terms.


Format your output as a list of json. Each element of the list contains a pair of terms and the relation between them, like the following:

[
   {
       "node_1": "A concept from extracted ontology",

       "node_2": "A related concept from extracted ontology",

       "edge": "relationship between the two concepts, node_1 and node_2 in one or two sentences"

   }, {...}
]

"""


def on_message(ws, message):
    print(message, end="")
    if "Completed" in message:
        print("\nReceived 'Completed' message. Closing WebSocket.")
        ws.close()


def on_error(ws, error):
    print("WebSocket error:", error)


def on_close(ws, a, b):
    print("WebSocket connection closed")


def on_open(ws):
    print("WebSocket connection opened")
    print()
    request = {
        "action": "stream",
        "sys_instruct": sys_instruct,
        "user_request": f"```{user_req}```",
        "deployment_name": "GPT-4",
    }
    ws.send(json.dumps(request))


if __name__ == "__main__":
    # fill this wis the approperiate wss://
    ws_url = "wss://jz92qcvyd4.execute-api.ap-southeast-1.amazonaws.com/prod/"
    ws = websocket.WebSocketApp(
        ws_url, on_message=on_message, on_error=on_error, on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()
