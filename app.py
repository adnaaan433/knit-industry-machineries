"""
Streamlit Webapp: Knit Textile Industry Machineries & Process Workflows
"""
import streamlit as st
from data import WORKFLOW_DATA
from components import render_department_page, inject_custom_css

st.set_page_config(
    page_title="Knit Textile Machineries — Technical Reference",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    inject_custom_css()

    departments = list(WORKFLOW_DATA.keys())

    with st.sidebar:
        st.markdown('<div class="sidebar-brand">Technical Reference Manual</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-title">Knit Industry Machineries</div>', unsafe_allow_html=True)

        selected_page = st.radio(
            "DEPARTMENT",
            options=departments,
            index=0,
            format_func=lambda x: f"0{departments.index(x) + 1} · {x}",
        )

        st.markdown("<hr style='margin: 18px 0; border-color: #cbd5e1;'>", unsafe_allow_html=True)
        st.markdown('<div class="sidebar-brand" style="margin-bottom:10px;">Curriculum Index</div>', unsafe_allow_html=True)

        for idx, (dept, info) in enumerate(WORKFLOW_DATA.items(), start=1):
            subs_html = "<br>".join(info["subsections"].keys())
            st.markdown(
                f"""
                <div class="sidebar-index-group">
                    <div class="sidebar-index-dept">0{idx}. {dept}</div>
                    <div class="sidebar-index-sub">{subs_html}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    dept_idx = departments.index(selected_page) + 1
    render_department_page(selected_page, WORKFLOW_DATA[selected_page], dept_index=dept_idx)


if __name__ == "__main__":
    main()
