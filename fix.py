import nbformat

fname = "ATML_PA0.ipynb"
outname = "ATML_PA0_fixed.ipynb"

# Read notebook
nb = nbformat.read(fname, as_version=4)

# Remove problematic metadata keys at notebook-level
for bad_key in ["widgets", "colab", "varInspector"]:
    nb.metadata.pop(bad_key, None)

# Clean each cell's metadata (but keep outputs)
for cell in nb.cells:
    if "metadata" in cell:
        for bad_key in ["execution", "widgets"]:
            cell["metadata"].pop(bad_key, None)

# Save new notebook
with open(outname, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"✅ Cleaned notebook written to {outname}")
