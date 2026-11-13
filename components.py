"""
Reusable UI components for rendering process flowcharts and machinery specification sheets.
Uses a strict 3-color eye-friendly palette:
1. Warm Alabaster / Sand (#F4F1EA & #EAE5DB) — Soft paper background (zero glare)
2. Deep Charcoal Slate (#1F2933) — Primary structure & readable ink
3. Muted Botanical Teal (#2E6F73) — Calm educational accent
"""
import os
import streamlit as st


def inject_custom_css():
    """Injects a soft, eye-friendly 3-color palette directly onto the Streamlit app."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap');

        :root {
            --bg-cream: #F4F1EA;
            --bg-sand: #EAE5DB;
            --bg-card: #FAF8F5;
            --ink-slate: #1F2933;
            --ink-muted: #52606D;
            --accent-teal: #2E6F73;
            --accent-teal-soft: #E3EFEF;
            --border-warm: #D6D0C4;
        }

        /* Force warm paper background & deep slate text even if browser is in dark mode */
        .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            background-color: var(--bg-cream) !important;
            color: var(--ink-slate) !important;
        }

        html, body, [class*="css"], p, span, div, label {
            font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            color: var(--ink-slate);
        }

        .block-container {
            padding-top: 2.2rem;
            padding-bottom: 4rem;
            max-width: 1160px;
        }

        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background-color: var(--bg-sand) !important;
            border-right: 1px solid var(--border-warm) !important;
        }
        section[data-testid="stSidebar"] * {
            color: var(--ink-slate) !important;
        }
        .sidebar-brand {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.72rem;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            color: var(--accent-teal) !important;
            font-weight: 600;
            margin-bottom: 2px;
        }
        .sidebar-title {
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--ink-slate) !important;
            letter-spacing: -0.02em;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 1px solid var(--border-warm);
        }
        .sidebar-index-group {
            margin-bottom: 12px;
        }
        .sidebar-index-dept {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--accent-teal) !important;
            margin-bottom: 4px;
        }
        .sidebar-index-sub {
            font-size: 0.82rem;
            color: var(--ink-muted) !important;
            padding-left: 10px;
            border-left: 2px solid var(--accent-teal);
            line-height: 1.55;
        }

        /* Department Header */
        .dept-eyebrow {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.76rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--accent-teal);
            margin-bottom: 4px;
        }
        .dept-title {
            font-size: 2rem;
            font-weight: 700;
            letter-spacing: -0.025em;
            color: var(--ink-slate);
            margin: 0 0 6px 0;
        }
        .dept-desc {
            font-size: 0.98rem;
            color: var(--ink-muted);
            max-width: 780px;
            line-height: 1.55;
            margin-bottom: 18px;
        }

        /* Clean Tabs */
        div[data-testid="stTabs"] button {
            font-family: 'IBM Plex Sans', sans-serif;
            font-weight: 600;
            font-size: 0.92rem;
            color: var(--ink-muted) !important;
            padding: 10px 18px;
        }
        div[data-testid="stTabs"] button[aria-selected="true"] {
            color: var(--accent-teal) !important;
            border-bottom-color: var(--accent-teal) !important;
        }

        /* Bordered Containers (Flowchart & Cards) */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: var(--bg-card) !important;
            border: 1px solid var(--border-warm) !important;
            border-radius: 8px !important;
            padding: 4px;
        }

        /* Sub-section Header */
        .sub-header-bar {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            border-bottom: 2px solid var(--accent-teal);
            padding-bottom: 8px;
            margin-top: 10px;
            margin-bottom: 8px;
        }
        .sub-title {
            font-size: 1.35rem;
            font-weight: 700;
            color: var(--ink-slate);
            margin: 0;
        }
        .sub-meta {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.76rem;
            color: var(--accent-teal);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }
        .sub-description {
            font-size: 0.94rem;
            color: var(--ink-muted);
            margin-bottom: 20px;
            line-height: 1.55;
        }

        /* Section Label */
        .section-caption {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.09em;
            color: var(--accent-teal);
            margin-top: 20px;
            margin-bottom: 10px;
        }

        /* Technical Spec Card for Machineries */
        .spec-card-header {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            border-bottom: 1px solid var(--border-warm);
            padding-bottom: 8px;
            margin-bottom: 10px;
            gap: 12px;
            flex-wrap: wrap;
        }
        .spec-machine-title {
            font-size: 1.08rem;
            font-weight: 700;
            color: var(--ink-slate);
            margin: 0;
        }
        .spec-index {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.82rem;
            font-weight: 600;
            color: var(--accent-teal);
            margin-right: 8px;
        }
        .spec-stage-tag {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.73rem;
            font-weight: 600;
            color: var(--accent-teal);
            background: var(--accent-teal-soft);
            border: 1px solid #B8D8D8;
            padding: 3px 9px;
            border-radius: 4px;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }
        .spec-purpose {
            font-size: 0.9rem;
            color: var(--ink-muted);
            line-height: 1.5;
            margin-bottom: 14px;
        }

        /* Input / Output Technical Grid */
        .io-grid {
            display: grid;
            grid-template-columns: 1fr 36px 1fr;
            align-items: stretch;
            border: 1px solid var(--border-warm);
            border-radius: 6px;
            background: var(--bg-cream);
            overflow: hidden;
        }
        .io-cell {
            padding: 10px 14px;
        }
        .io-cell-in {
            background: var(--bg-cream);
        }
        .io-cell-out {
            background: var(--accent-teal-soft);
        }
        .io-divider {
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--bg-sand);
            border-left: 1px solid var(--border-warm);
            border-right: 1px solid var(--border-warm);
            font-family: 'IBM Plex Mono', monospace;
            color: var(--accent-teal);
            font-weight: 700;
            font-size: 0.95rem;
        }
        .io-key {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.68rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--ink-muted);
            margin-bottom: 3px;
        }
        .io-key-out {
            color: var(--accent-teal);
        }
        .io-val {
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--ink-slate);
        }

        /* Technical Figure Placeholder */
        .figure-frame {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 148px;
            border: 1px dashed var(--accent-teal);
            border-radius: 6px;
            background: var(--bg-cream);
            padding: 12px;
            text-align: center;
        }
        .figure-code {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.72rem;
            font-weight: 600;
            color: var(--accent-teal);
            text-transform: uppercase;
            letter-spacing: 0.06em;
            margin-bottom: 4px;
        }
        .figure-note {
            font-size: 0.76rem;
            color: var(--ink-muted);
        }

        /* Serpentine / Boustrophedon Continuous Flowchart */
        .flow-canvas {
            padding: 12px 10px;
        }
        .flow-row {
            display: flex;
            align-items: stretch;
            justify-content: space-between;
            width: 100%;
        }
        .flow-row-rtl {
            flex-direction: row-reverse;
        }
        .flow-node {
            flex: 1 1 0;
            display: flex;
            align-items: center;
            gap: 10px;
            background-color: var(--accent-teal-soft);
            border: 1.5px solid var(--accent-teal);
            border-radius: 6px;
            padding: 11px 14px;
            min-height: 52px;
            box-shadow: 0 1px 2px rgba(31, 41, 51, 0.05);
        }
        .flow-node-spacer {
            flex: 1 1 0;
            visibility: hidden;
            padding: 11px 14px;
        }
        .flow-num {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.75rem;
            font-weight: 700;
            color: #FAF8F5 !important;
            background-color: var(--accent-teal);
            padding: 3px 7px;
            border-radius: 4px;
            flex-shrink: 0;
        }
        .flow-label {
            font-size: 0.87rem;
            font-weight: 600;
            color: var(--ink-slate) !important;
            line-height: 1.3;
        }
        .flow-node-body {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }
        .flow-sub {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.72rem;
            font-weight: 500;
            color: var(--accent-teal) !important;
        }
        .product-summary-banner {
            font-size: 0.86rem;
            color: var(--ink-slate);
            background-color: var(--bg-sand);
            border-left: 3px solid var(--accent-teal);
            padding: 8px 12px;
            border-radius: 0 4px 4px 0;
            margin-bottom: 10px;
        }
        .flow-h-arrow {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 36px;
            flex-shrink: 0;
            color: var(--accent-teal) !important;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 1.25rem;
            font-weight: 700;
        }
        .flow-h-arrow-spacer {
            width: 36px;
            flex-shrink: 0;
            visibility: hidden;
        }
        .flow-turn-row {
            display: flex;
            width: 100%;
            justify-content: space-between;
            padding: 3px 0;
        }
        .flow-turn-cell {
            flex: 1 1 0;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--accent-teal) !important;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 1.25rem;
            font-weight: 700;
            height: 26px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_flowchart(
    steps: list,
    subsection_name: str,
    subtitle: str = "",
    section_num: str = "01",
    heading_prefix: str = "Process Flow Diagram",
):
    """Renders a continuous serpentine (snake) block diagram so arrows never break across rows."""
    header_label = f"{section_num} / {heading_prefix} — {subsection_name}"
    if subtitle:
        header_label += f" ({subtitle})"
    st.markdown(
        f'<div class="section-caption">{header_label}</div>',
        unsafe_allow_html=True,
    )

    if not steps:
        st.info("No flowchart steps defined.")
        return

    cols_per_row = 3 if len(steps) > 4 else len(steps)
    chunks = [steps[i : i + cols_per_row] for i in range(0, len(steps), cols_per_row)]

    rows_html = []
    step_counter = 1

    for row_idx, chunk in enumerate(chunks):
        is_rtl = row_idx % 2 == 1
        row_class = "flow-row flow-row-rtl" if is_rtl else "flow-row"
        arrow_symbol = "&#10229;" if is_rtl else "&#10230;"  # ⟵ for RTL row, ⟶ for LTR row

        row_cells = []
        for col_idx in range(cols_per_row):
            if col_idx < len(chunk):
                step_item = chunk[col_idx]
                if isinstance(step_item, dict):
                    op_name = step_item.get("operation", "")
                    mach_name = step_item.get("machine", "")
                    qty = step_item.get("qty")
                    qty_str = f" · {qty}x" if qty else ""
                    body_html = (
                        f'<div class="flow-node-body">'
                        f'<span class="flow-label">{op_name}</span>'
                        f'<span class="flow-sub">{mach_name}{qty_str}</span>'
                        f'</div>'
                    )
                else:
                    body_html = f'<span class="flow-label">{step_item}</span>'

                row_cells.append(
                    f'<div class="flow-node">'
                    f'<span class="flow-num">{step_counter:02d}</span>'
                    f'{body_html}'
                    f'</div>'
                )
                step_counter += 1
            else:
                row_cells.append('<div class="flow-node-spacer"></div>')

            if col_idx < cols_per_row - 1:
                if col_idx < len(chunk) - 1:
                    row_cells.append(f'<div class="flow-h-arrow">{arrow_symbol}</div>')
                else:
                    row_cells.append('<div class="flow-h-arrow-spacer"></div>')

        rows_html.append(f'<div class="{row_class}">{"".join(row_cells)}</div>')

        # Add vertical downward connector aligned directly under the last active node of this row
        if row_idx < len(chunks) - 1:
            turn_cells = []
            target_col = 0 if is_rtl else (cols_per_row - 1)
            for col_idx in range(cols_per_row):
                if col_idx == target_col:
                    turn_cells.append('<div class="flow-turn-cell">&#8595;</div>')
                else:
                    turn_cells.append('<div class="flow-turn-cell"></div>')
                if col_idx < cols_per_row - 1:
                    turn_cells.append('<div class="flow-h-arrow-spacer"></div>')
            rows_html.append(f'<div class="flow-turn-row">{"".join(turn_cells)}</div>')

    with st.container(border=True):
        st.markdown(
            f'<div class="flow-canvas">{"".join(rows_html)}</div>',
            unsafe_allow_html=True,
        )


def render_machineries(machineries: list[dict], subsection_name: str, section_num: str = "02"):
    """Renders clean engineering specification sheets for each machine."""
    st.markdown(
        f'<div class="section-caption">{section_num} / Machinery & Material Flow Specifications ({len(machineries)} Units)</div>',
        unsafe_allow_html=True,
    )

    if not machineries:
        st.info("No machinery entries populated yet.")
        return

    for idx, item in enumerate(machineries, start=1):
        step_name = item.get("step", f"Stage {idx}")
        machine_name = item.get("machine_name", "Machine Name TBD")
        input_mat = item.get("input", "TBD")
        output_mat = item.get("output", "TBD")
        purpose = item.get("purpose", "")
        image_path = item.get("image")

        with st.container(border=True):
            col_fig, col_spec = st.columns([1.15, 3.85], gap="medium")

            with col_fig:
                if image_path and (
                    image_path.startswith(("http://", "https://"))
                    or os.path.exists(image_path)
                ):
                    st.image(image_path, caption=f"Fig {idx:02d}. {machine_name}", use_container_width=True)
                else:
                    st.markdown(
                        f"""
                        <div class="figure-frame">
                            <div class="figure-code">FIG. {idx:02d} // IMAGE SLOT</div>
                            <div class="figure-note">Machine photograph to be added</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

            with col_spec:
                st.markdown(
                    f"""
                    <div class="spec-card-header">
                        <div class="spec-machine-title">
                            <span class="spec-index">M-{idx:02d}</span>{machine_name}
                        </div>
                        <span class="spec-stage-tag">Stage: {step_name}</span>
                    </div>
                    <div class="spec-purpose">{purpose}</div>
                    <div class="io-grid">
                        <div class="io-cell io-cell-in">
                            <div class="io-key">Material Input</div>
                            <div class="io-val">{input_mat}</div>
                        </div>
                        <div class="io-divider">→</div>
                        <div class="io-cell io-cell-out">
                            <div class="io-key io-key-out">Processed Output</div>
                            <div class="io-val">{output_mat}</div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


def render_department_page(dept_name: str, dept_data: dict, dept_index: int = 1):
    """Renders a department page with clean editorial hierarchy."""
    inject_custom_css()

    description = dept_data.get("description", "")
    subsections = dept_data.get("subsections", {})

    st.markdown(
        f"""
        <div class="dept-eyebrow">Section 0{dept_index} // Knit Textile Manufacturing</div>
        <h1 class="dept-title">{dept_name}</h1>
        <div class="dept-desc">{description}</div>
        """,
        unsafe_allow_html=True,
    )

    subsection_names = list(subsections.keys())
    tabs = st.tabs(subsection_names)

    for tab, sub_name in zip(tabs, subsection_names):
        with tab:
            sub_data = subsections[sub_name]
            steps = sub_data.get("flowchart_steps", [])
            machines = sub_data.get("machineries", [])
            product_flowcharts = sub_data.get("product_flowcharts", {})

            st.markdown(
                f"""
                <div class="sub-header-bar">
                    <h2 class="sub-title">{sub_name}</h2>
                    <span class="sub-meta">{len(steps)} Process Stages · {len(machines)} Machineries</span>
                </div>
                <div class="sub-description">{sub_data.get("description", "")}</div>
                """,
                unsafe_allow_html=True,
            )

            if product_flowcharts:
                # 01: Overall Department Process Flowchart
                render_flowchart(
                    steps,
                    sub_name,
                    subtitle="Overall Department Workflow",
                    section_num="01",
                    heading_prefix="Overall Process Flow Diagram",
                )

                # 02: Product-Specific Sewing Line Layout Flowchart
                st.markdown(
                    f'<div class="section-caption" style="margin-top:26px;">02 / Product-Wise Line Layout Flowchart — {sub_name}</div>',
                    unsafe_allow_html=True,
                )
                product_names = list(product_flowcharts.keys())
                col_sel, col_filter = st.columns([2.2, 2.8])
                with col_sel:
                    selected_product = st.radio(
                        "Product Category",
                        options=product_names,
                        index=0,
                        horizontal=True,
                        key=f"prod_select_{sub_name}",
                    )
                prod_info = product_flowcharts[selected_product]
                req_machines = prod_info.get("required_machines", [])

                with col_filter:
                    st.write("")
                    filter_by_product = st.checkbox(
                        f"Filter machinery catalog below to only the {len(req_machines)} machine types used in {selected_product}",
                        value=False,
                        key=f"prod_filter_{sub_name}",
                    )

                if prod_info.get("summary"):
                    st.markdown(
                        f'<div class="product-summary-banner">{prod_info["summary"]}</div>',
                        unsafe_allow_html=True,
                    )

                render_flowchart(
                    prod_info.get("steps", []),
                    selected_product,
                    subtitle="Operation & Machine Sequence",
                    section_num="02A",
                    heading_prefix="Product Line Flowchart",
                )

                displayed_machines = (
                    [m for m in machines if m.get("machine_name") in req_machines]
                    if filter_by_product and req_machines
                    else machines
                )
                render_machineries(displayed_machines, sub_name, section_num="03")
            else:
                render_flowchart(steps, sub_name, section_num="01")
                render_machineries(machines, sub_name, section_num="02")
