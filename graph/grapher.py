from pyvis.network import Network
import networkx as nx
import os
import shutil
import json
import re


def clean_and_parse_json(json_str):
    json_str = re.sub(r",(\s*[}\]])", r"\1", json_str)
    return json.loads(json_str)


def merge_json(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        pattern = r"\[.*?\](?=\s*\[|$)"
        json_strings = re.findall(pattern, content, re.DOTALL)
        all_json_objects = []
        for json_str in json_strings:
            try:
                parsed_json = clean_and_parse_json(json_str)
                all_json_objects.extend(parsed_json)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")
                print("Faulty JSON:", json_str)
        return all_json_objects


ontology_data = merge_json("dump.txt")


if os.path.isfile("ontology_graph.html"):
    os.remove("ontology_graph.html")
if os.path.isfile("temp_ontology_graph.html"):
    os.remove("temp_ontology_graph.html")
if os.path.isfile("ouput.txt"):
    os.remove("ouput.txt")
if os.path.isdir("lib"):
    shutil.rmtree("lib")
# Write the string to the file
with open("output.txt", "w") as file:
    file.write(json.dumps(ontology_data, indent=4))
net = Network(notebook=True)
G = nx.Graph()

for entry in ontology_data:
    G.add_edge(
        entry["node_1"], entry["node_2"], title=entry["edge"], label=entry["edge"]
    )

degrees = dict(G.degree())

for node, degree in degrees.items():
    net.add_node(node, label=node, size=degree * 10)

for entry in ontology_data:
    net.add_edge(
        entry["node_1"], entry["node_2"], title=entry["edge"], label=entry["edge"]
    )

# Save to a temporary HTML file
net.save_graph("temp_ontology_graph.html")

# Read the temporary file and append the search functionality
with open("temp_ontology_graph.html", "r") as file:
    html_content = file.read()

search_html = """
<form onsubmit="searchNode(); return false;">
    <input type="text" id="searchTerm" placeholder="Search term...">
    <input type="submit" value="Search">
</form>
<script>
function searchNode() {
    var searchTerm = document.getElementById('searchTerm').value;
    var allNodes = network.body.data.nodes.get();
    var matchedNodes = allNodes.filter(node => node.label.includes(searchTerm));
    var updateArray = allNodes.map(node => {
        node.color = matchedNodes.includes(node) ? 'red' : 'blue';
        return node;
    });
    network.body.data.nodes.update(updateArray);
}
</script>
"""

# Add the search HTML before the closing body tag
html_content = html_content.replace("</body>", search_html + "</body>")

# Write the modified HTML back to the file
with open("ontology_graph.html", "w") as file:
    file.write(html_content)
