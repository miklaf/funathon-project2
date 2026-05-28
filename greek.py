
# %%
from rdflib import Graph
import pandas as pd

# Load RDF graph
g = Graph()

# Replace with your RDF file path
g.parse("/diffusion/NACE_Rev.2.1.rdf")   # auto-detects many formats



install.packages()

# %%
from rdflib import Graph
import pandas as pd

# Load RDF graph
g = Graph()

# Replace with your RDF file path
g.parse("data.rdf")   # auto-detects many formats

# Convert triples to rows
rows = []

for s, p, o in g:
    rows.append({
        "subject": str(s),
        "predicate": str(p),
        "object": str(o)
    })

# Create DataFrame
df = pd.DataFrame(rows)

# Show first rows
print(df.head())

# Save to CSV
df.to_csv("rdf_output.csv", index=False)

print("CSV saved as rdf_output.csv")