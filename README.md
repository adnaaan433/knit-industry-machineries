# Knit Textile Industry Machineries — Technical Reference

A Streamlit web application presenting the process flowcharts, machine layouts, and machinery input/output specifications across the **Knit Textile Manufacturing** value chain.

## Pages & Sub-Sections

1. **Spinning** *(Rieter Spinning Systems)*
   - Fiber preparation machines
   - Spinning preparation machines
   - Ring spinning machines
   - Compact-spinning machines
   - Rotor spinning machines
   - Air-jet spinning machines
   - Winding machines
   - Texturing machines
2. **Knitting**
   - Circular Knitting
   - Flat Knitting
3. **Dyeing**
   - Fabric Dyeing
   - Yarn Dyeing
   - Fiber Dyeing
4. **Garments**
   - Cutting
   - Sewing *(Overall Department Flowchart + Product-Wise Machine Layout Flowchart & 25 Industrial Sewing Machine Specifications)*
   - Printing
   - Embroidery
   - Washing
   - Finishing
5. **Laboratory**
   - Laboratory Testing *(Placeholder — to be populated)*
6. **Utility**
   - Utility Machineries *(Fire-Tube Boiler, Generator, Compressor, HVAC & Filtration Systems)*

## Project Structure

```text
├── .streamlit/
│   └── config.toml          # Streamlit theme configuration
├── assets/
│   └── machines/            # Folder for machine photographs
├── app.py                   # Main Streamlit entrypoint
├── components.py            # Serpentine flowchart & specification card UI components
├── data.py                  # Structured workflow & machinery dataset
└── requirements.txt         # Python dependencies
```

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with GitHub.
3. Click **Create app** → select your repository, branch (`main`), and set **Main file path** to `app.py`.
4. Click **Deploy**.

