import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# Define the data structure based on the provided JSON
data = {
    "center": "THE ART OF CALISTHENICS",
    "stages": {
        "Stage 1": {
            "name": "Creating Base",
            "elements": ["Foundation", "Scapula prep", "Body aware", "Mobility"]
        },
        "Stage 2": {
            "name": "Building Struct", 
            "elements": ["Big-7 moves", "Progression", "Skill intro", "Strength dev"]
        },
        "Stage 3": {
            "name": "Mastering Cal",
            "elements": ["Specialization", "Discipline", "Advanced", "Personal"]
        }
    },
    "disciplines": {
        "Bodybuilding": ["Aesthetics", "Volume", "Muscle build", "Hypertrophy"],
        "Power Free": ["Static holds", "Planche", "Front lever", "Straight arm"],
        "Freestyle": ["Creativity", "Flow", "Dynamic", "Artistic"],
        "Street Lift": ["Weighted", "Max strength", "Powerlifting", "1RM focus"],
        "Hand-Balance": ["Balance", "Alignment", "Surface var", "Equilibrium"],
        "Mobility": ["Flexibility", "ROM", "Strength", "Joint mob"],
        "Hybrid": ["Combinations", "Well-rounded", "Complement", "Balance"]
    },
    "book_parts": {
        "Parts 1-2": "Foundation",
        "Part 3": "Mastering", 
        "Part 4": "6 Disciplines",
        "Part 5": "Programs",
        "Parts 6-7": "Journey"
    }
}

# Create coordinate system for positioning elements
points = []
colors = []
sizes = []
texts = []
hover_texts = []
categories = []

# Brand colors
brand_colors = ['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F', '#D2BA4C', '#B4413C', '#964325']

# Center element
points.append([0, 0])
colors.append(brand_colors[0])
sizes.append(30)
texts.append("ART OF CAL")
hover_texts.append("THE ART OF CALISTHENICS<br>Complete System")
categories.append("Center")

# Left side - 3 Stages (arranged vertically)
stage_y_positions = [2, 0, -2]
for i, (stage_key, stage_data) in enumerate(data["stages"].items()):
    # Main stage point
    points.append([-4, stage_y_positions[i]])
    colors.append(brand_colors[1])
    sizes.append(20)
    texts.append(stage_data["name"][:12])
    hover_text = f"{stage_key}: {stage_data['name']}<br>" + "<br>".join(stage_data["elements"][:4])
    hover_texts.append(hover_text)
    categories.append("Stages")
    
    # Sub-elements for each stage
    for j, element in enumerate(stage_data["elements"][:4]):
        points.append([-5.5, stage_y_positions[i] + (j-1.5)*0.3])
        colors.append(brand_colors[1])
        sizes.append(8)
        texts.append(element[:10])
        hover_texts.append(f"{stage_key}<br>{element}")
        categories.append("Stage Elements")

# Right side - Disciplines in circular pattern
discipline_angles = np.linspace(0, 2*np.pi, 7, endpoint=False)  # 6 disciplines + hybrid
discipline_radius = 3

for i, (disc_name, disc_elements) in enumerate(data["disciplines"].items()):
    if disc_name == "Hybrid":
        # Place hybrid in center-right
        x, y = 2, 0
        size = 18
        color_idx = 6
    else:
        # Place other disciplines in circle
        angle = discipline_angles[i]
        x = discipline_radius * np.cos(angle) + 2
        y = discipline_radius * np.sin(angle)
        size = 15
        color_idx = (i % 6) + 1
    
    points.append([x, y])
    colors.append(brand_colors[color_idx])
    sizes.append(size)
    texts.append(disc_name[:12])
    hover_text = f"{disc_name}<br>" + "<br>".join(disc_elements[:4])
    hover_texts.append(hover_text)
    categories.append("Disciplines")

# Top - Book parts
book_x_positions = np.linspace(-3, 3, 5)
for i, (part_key, part_name) in enumerate(data["book_parts"].items()):
    points.append([book_x_positions[i], 4])
    colors.append(brand_colors[4])
    sizes.append(12)
    texts.append(part_key)
    hover_texts.append(f"{part_key}: {part_name}")
    categories.append("Book Parts")

# Convert to DataFrame
df = pd.DataFrame({
    'x': [p[0] for p in points],
    'y': [p[1] for p in points],
    'color': colors,
    'size': sizes,
    'text': texts,
    'hover': hover_texts,
    'category': categories
})

# Create the figure
fig = go.Figure()

# Add scatter points for each category
for category in df['category'].unique():
    cat_data = df[df['category'] == category]
    fig.add_trace(go.Scatter(
        x=cat_data['x'],
        y=cat_data['y'],
        mode='markers+text',
        marker=dict(
            size=cat_data['size'],
            color=cat_data['color'],
            line=dict(width=2, color='white')
        ),
        text=cat_data['text'],
        textposition='middle center',
        textfont=dict(size=10, color='white'),
        hovertemplate='%{hovertext}<extra></extra>',
        hovertext=cat_data['hover'],
        name=category,
        showlegend=True
    ))

# Add connecting lines from stages to center
for i in range(3):
    fig.add_trace(go.Scatter(
        x=[-4, -1], 
        y=[stage_y_positions[i], 0],
        mode='lines',
        line=dict(color='gray', width=2, dash='dot'),
        showlegend=False,
        hoverinfo='skip'
    ))

# Add connecting lines from center to disciplines
for i in range(6):
    angle = discipline_angles[i]
    x_end = discipline_radius * np.cos(angle) + 2
    y_end = discipline_radius * np.sin(angle)
    fig.add_trace(go.Scatter(
        x=[1, x_end], 
        y=[0, y_end],
        mode='lines',
        line=dict(color='gray', width=1, dash='dot'),
        showlegend=False,
        hoverinfo='skip'
    ))

# Update layout
fig.update_layout(
    title="Calisthenics System Structure",
    xaxis=dict(
        range=[-7, 7],
        showgrid=False,
        showticklabels=False,
        zeroline=False
    ),
    yaxis=dict(
        range=[-4, 5],
        showgrid=False,
        showticklabels=False,
        zeroline=False
    ),
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.05,
        xanchor='center',
        x=0.5
    ),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

# Save the chart
fig.write_image("calisthenics_system_chart.png")