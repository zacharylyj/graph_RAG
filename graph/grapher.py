from pyvis.network import Network
import networkx as nx
import os
import shutil

# Define the file and folder to be deleted
file_to_delete = "ontology_graph.html"
folder_to_delete = "lib"

# Check if the file exists and delete it
if os.path.isfile(file_to_delete):
    os.remove(file_to_delete)
    print(f"File '{file_to_delete}' has been deleted.")
else:
    print(f"File '{file_to_delete}' does not exist.")

# Check if the folder exists and delete it
if os.path.isdir(folder_to_delete):
    shutil.rmtree(folder_to_delete)
    print(f"Folder '{folder_to_delete}' has been deleted.")
else:
    print(f"Folder '{folder_to_delete}' does not exist.")
# Ensure you have pyvis installed
# pip install pyvis

# Extracted data
ontology_data = [
    {
        "node_1": "Hyperplasia",
        "node_2": "Increased number of cells within an organ",
        "edge": "Hyperplasia is described as an increased number of cells within an organ.",
    },
    {
        "node_1": "RBC lysis",
        "node_2": "Ineffective Na+ pumping",
        "edge": "RBCs lyse in hypotonic solutions because they cannot pump Na+ out effectively.",
    },
    {
        "node_1": "Stroke progression",
        "node_2": "Endothelial injury, thrombosis, embolism, ischaemia",
        "edge": "The progression of a stroke typically follows endothelial injury, thrombosis, embolism, and ischaemia.",
    },
    {
        "node_1": "Unequal chromosome numbers in daughter cells",
        "node_2": "Improper microtubule function",
        "edge": "Improper function of microtubules can lead to unequal numbers of chromosomes in daughter cells after mitosis.",
    },
    {
        "node_1": "Nucleosome disassembly",
        "node_2": "RNA transcription",
        "edge": "Disassembly of nucleosomes is involved in RNA transcription.",
    },
    {
        "node_1": "Listeria actin comet tails",
        "node_2": "Arp2/3 nucleation",
        "edge": "Arp2/3 is the most important nucleator of actin filament growth for Listeria's actin comet tails.",
    },
    {
        "node_1": "Semi-conservative DNA replication",
        "node_2": "Newly synthesized DNA and parent DNA strands",
        "edge": "In semi-conservative DNA replication, each daughter cell contains one newly synthesized DNA strand and one DNA strand inherited from the parent cell.",
    },
    {
        "node_1": "Colon cancer genetic defect",
        "node_2": "MSH-2 gene mutation",
        "edge": "A loss of function mutation in the MSH-2 gene affecting DNA mismatch repair is likely responsible for colon cancer.",
    },
    {
        "node_1": "Foot anatomical position",
        "node_2": "Inversion",
        "edge": "The anatomical term describing the foot position shown is inversion.",
    },
    {
        "node_1": "Aorta histological structure",
        "node_2": "Elastic fibers",
        "edge": "The structure indicated by the arrows in the histological section of the aorta is elastic fibers.",
    },
    {
        "node_1": "Cell bursting prevention",
        "node_2": "Sodium-potassium pump",
        "edge": "The sodium-potassium pump maintains a low intracellular sodium concentration, preventing cells from bursting.",
    },
    {
        "node_1": "Colloid osmotic pressure",
        "node_2": "Water retention in capillaries",
        "edge": "Colloid osmotic pressure retains water in the capillaries.",
    },
    {
        "node_1": "Schwann cell destruction",
        "node_2": "Speed of conductance",
        "edge": "Destruction of Schwann cells affects the speed of conductance in neurons.",
    },
    {
        "node_1": "Mushroom toxin",
        "node_2": "Muscarinic receptor stimulation",
        "edge": "The mushroom toxin stimulates muscarinic receptors, explaining the symptoms experienced.",
    },
    {
        "node_1": "Lactate production under anaerobic conditions",
        "node_2": "Pyruvate conversion",
        "edge": "Pyruvate is converted to lactate under anaerobic conditions during exercise.",
    },
    {
        "node_1": "LDL cholesterol reduction",
        "node_2": "HMG-CoA reductase inhibitors",
        "edge": "HMG-CoA reductase inhibitors are used to reduce the level of LDL cholesterol in patients with hyperlipidaemia.",
    },
    {
        "node_1": "Energy extraction from lipids",
        "node_2": "FADH2 and NADH production",
        "edge": "During beta-oxidation, the energy extracted from a lipid is in the form of FADH2 and NADH.",
    },
    {
        "node_1": "Neutral lipids fate",
        "node_2": "Hydrolysis to free fatty acids",
        "edge": "Neutral lipids within lipid droplets are likely hydrolyzed to free fatty acids.",
    },
    {
        "node_1": "MHC molecules",
        "node_2": "CD4+ T lymphocytes recognition of MHC II",
        "edge": "CD4+ T lymphocytes recognize extracellular antigens presented by MHC II molecules.",
    },
    {
        "node_1": "Anti-PD-1 antibodies",
        "node_2": "Reduction of tumour-infiltrating regulatory T-cells",
        "edge": "Anti-PD-1 antibodies work by decreasing tumour-infiltrating regulatory T-cells within the tumour.",
    },
    {
        "node_1": "Th1 cells",
        "node_2": "IFN-γ production",
        "edge": "Th1 cells are important for eliminating tumour cells because they produce IFN-γ, activating cytotoxic T cells.",
    },
    {
        "node_1": "Hypersensitivity types",
        "node_2": "I and IV",
        "edge": "Asthma and eczema flare-ups represent Type I and IV hypersensitivities, respectively.",
    },
    {
        "node_1": "SLE infection risk",
        "node_2": "Increased immune response",
        "edge": "Infections can increase the immune response, worsening SLE symptoms.",
    },
    {
        "node_1": "Green watery diarrhea organism",
        "node_2": "Giardia lamblia",
        "edge": "The organism most likely identified with green watery diarrhea and other symptoms is Giardia lamblia.",
    },
    {
        "node_1": "Histological diagnosis of lung mass",
        "node_2": "Squamous cell carcinoma",
        "edge": "The histological diagnosis of the lung mass shown is squamous cell carcinoma.",
    },
    {
        "node_1": "Surfactant production",
        "node_2": "Type II alveolar epithelial cells",
        "edge": "Type II alveolar epithelial cells produce surfactant in the developing lung.",
    },
    {
        "node_1": "Asthma exacerbation",
        "node_2": "Mucus hypersecretion",
        "edge": "An acute exacerbation of asthma is associated with mucus hypersecretion.",
    },
    {
        "node_1": "Nerve injured during mastectomy",
        "node_2": "Intercostobrachial nerve",
        "edge": "The intercostobrachial nerve is most likely to have been injured during a total mastectomy causing loss of sensation.",
    },
    {
        "node_1": "Oesophagus constriction",
        "node_2": "Arch of aorta",
        "edge": "The arch of aorta is constricting the oesophagus in the case described.",
    },
    {
        "node_1": "Blood vessel above left lung root",
        "node_2": "Aortic arch",
        "edge": "The aortic arch crosses superior to the left lung root.",
    },
    {
        "node_1": "Last structure opacified by contrast",
        "node_2": "Right subclavian artery",
        "edge": "The right subclavian artery is the last structure to be opacified by the contrast.",
    },
    {
        "node_1": "Vascular insult to left anterior descending artery",
        "node_2": "Atrioventricular bundle",
        "edge": "An occlusion in the left anterior descending artery is most likely to injure the atrioventricular bundle.",
    },
    {
        "node_1": "Aortic dissection presentation",
        "node_2": "Lower limb ischaemia",
        "edge": "Aortic dissection distal to the left subclavian artery is most likely associated with lower limb ischaemia.",
    },
    {
        "node_1": "Injury to left phrenic nerve",
        "node_2": "Raised left hemi-diaphragm",
        "edge": "Injury to the left phrenic nerve results in a raised left hemi-diaphragm.",
    },
    {
        "node_1": "Right common carotid artery origin",
        "node_2": "Brachiocephalic artery",
        "edge": "The right common carotid artery arises from the brachiocephalic artery.",
    },
    {
        "node_1": "Foetal atrial blood flow",
        "node_2": "Foramen ovale",
        "edge": "The foramen ovale allows blood to enter the left atrium from the right atrium during foetal life.",
    },
    {
        "node_1": "Pneumonia effect on gas exchange",
        "node_2": "Increased intrapulmonary shunting",
        "edge": "Pneumonia in the lung increases intrapulmonary shunting, affecting gas exchange.",
    },
    {
        "node_1": "High altitude adaptation",
        "node_2": "Decreased serum bicarbonate",
        "edge": "Decreased serum bicarbonate is a physiological adaptation present after living at high altitude.",
    },
    {
        "node_1": "Highest expiratory flow",
        "node_2": "End of maximal inspiration",
        "edge": "To achieve the highest expiratory flow, forced expiration should be initiated at the end of maximal inspiration.",
    },
    {
        "node_1": "Compensatory response to prevent fainting",
        "node_2": "Stimulation of beta-1 receptors in ventricles",
        "edge": "The compensatory physiological response that prevents fainting involves stimulation of beta-1 receptors in the ventricles.",
    },
    {
        "node_1": "Myocardial infarction location",
        "node_2": "Inferior wall of left ventricle",
        "edge": "Pathological Q waves and ST segment elevation in leads II, III, and aVF indicate a myocardial infarction in the inferior wall of the left ventricle.",
    },
    {
        "node_1": "Tachypnoea mechanism",
        "node_2": "Central chemoreceptors responding to high PaCO2",
        "edge": "The underlying mechanism for tachypnoea is the response of central chemoreceptors to high PaCO2.",
    },
    {
        "node_1": "Ciliated airway cells",
        "node_2": "Epithelial lining cells",
        "edge": "The epithelial lining cells in the airway are ciliated.",
    },
    {
        "node_1": "Left ventricle end-systolic volume",
        "node_2": "DA line",
        "edge": "The DA line on the pressure-volume loop represents the end-systolic volume of the left ventricle.",
    },
    {
        "node_1": "Lung volume equilibrium",
        "node_2": "D",
        "edge": "The lung volume at which collapsing pressure of the lung balances expanding pressure of the chest wall is represented by point D.",
    },
    {
        "node_1": "Skin oedema mechanism",
        "node_2": "Increased capillary permeability",
        "edge": "The underlying physiological mechanism for skin oedema is increased capillary permeability.",
    },
    {
        "node_1": "Pulmonary function test result",
        "node_2": "Emphysema",
        "edge": "The pulmonary function test results are indicative of emphysema.",
    },
    {
        "node_1": "Cardiac valvular disorder",
        "node_2": "Aortic stenosis",
        "edge": "A harsh, crescendo-decrescendo systolic murmur radiating to the carotid arteries suggests aortic stenosis.",
    },
]

net = Network(notebook=True)

# Create a NetworkX graph to calculate node degrees
G = nx.Graph()

# Add nodes and edges to the NetworkX graph
for entry in ontology_data:
    node_1 = entry["node_1"]
    node_2 = entry["node_2"]
    edge = entry["edge"]

    G.add_edge(node_1, node_2, title=edge, label=edge)

# Calculate the degree of each node
degrees = dict(G.degree())

# Add nodes and edges to the Pyvis network with size adjustments based on degree
for node, degree in degrees.items():
    net.add_node(
        node, label=node, size=degree * 10
    )  # Adjust the multiplier as needed for better visualization

for entry in ontology_data:
    node_1 = entry["node_1"]
    node_2 = entry["node_2"]
    edge = entry["edge"]

    net.add_edge(node_1, node_2, title=edge, label=edge)

# Generate and show the interactive network
net.show("ontology_graph.html")
