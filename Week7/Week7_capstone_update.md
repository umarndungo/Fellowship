# Week 7 Capstone Progress Update: FreshRoute AI
Author: Amos Ndungo
Project: FreshRoute AI
Date: August 14, 2026

## 1. Dashboard Development Status

This week marks the official transition from backend architecture to frontend visualization. My team and I have successfully initiated the building phase of the FreshRoute AI dashboard.
We began by constructing a robust frontend "shell." 

The primary goal of this shell is to provide a clean, high-performance interface that can effectively showcase our core findings, logistics projections, and relevant supply chain data. By focusing on the layout and navigation early, we are ensuring that when the heavy data pipelines are fully integrated, the user experience remains intuitive and the data remains the focal point.

## 2. Technology Stack & Decision Making

Our architectural approach is hybrid. We have committed to a stack involving Next.js for the core frontend experience and Python for our backend data processing and AI logic.

Regarding the specific visualization libraries, we are currently in a deliberation phase. While we recognize the rapid prototyping power of Streamlit and the deep customization offered by Plotly Dash, we are weighing these against our specific use-case scenarios. 

Because FreshRoute AI requires real-time logistics tracking and predictive analytics, we are evaluating which library offers the best integration with our Next.js shell without compromising on rendering speed or interactivity. We expect to finalize this choice early next week once our data schemas are fully locked in.


## 3. Challenges & Roadblocks

One significant challenge often faced at this stage is the complexity of visualizing multi-dimensional logistics data. However, we are not yet at the specific data visualization stage.

Currently, our main hurdle is ensuring the "plumbing"—the connection between our Python-based AI models and the Next.js shell—is seamless. By prioritizing the structural integrity of the application now, we hope to avoid the common pitfall of having beautiful charts that lack stable data sources. We are moving methodically to ensure that once we begin mapping our data, the visualizations are both accurate and actionable.

## 4. Goals for Week 8

- Finalize Visualization Library: Choose between Plotly Dash or Streamlit (or potentially custom D3.js components) based on our performance benchmarks.
- Data Integration: Begin piping dummy data from the Python backend into the Next.js shell to test component responsiveness.
- UI Refinement: Polish the shell to include the specific KPIs identified in our initial project scope.