data = [
    {
        "id": "US Market",
        "datum": 6721.897981,
        "children": [
            {
                "id": "Consumer Discretionary",
                "datum": 1194.79423,
                "children": [
                    {"id": "Revenue Growth", "datum": 81.52003},
                    {"id": "Gross Profit", "datum": 592.3901},
                    {"id": "Net Income", "datum": 520.8841},
                ],
            },
            {
                "id": "Consumer Non-Discretionary",
                "datum": 2328.5305,
                "children": [
                    {"id": "Revenue Growth", "datum": 769.4358},
                    {"id": "Gross Profit", "datum": 939.8358},
                    {"id": "Net Income", "datum": 619.2589},
                ],
            },
            {
                "id": "Energy",
                "datum": 1691.8709959,
                "children": [
                    {"id": "Revenue Growth", "datum": 7.343696},
                    {"id": "Gross Profit", "datum": 791.135},
                    {"id": "EBITDA", "datum": 338.9421},
                    {"id": "Net Income", "datum": 554.4502},
                ],
            },
            {
                "id": "Financial Services",
                "datum": 81.07515,
                "children": [
                    {"id": "Revenue Growth", "datum": 22.80559},
                    {"id": "Net Income", "datum": 58.26956},
                ],
            },
            {
                "id": "Healthcare",
                "datum": 1287.21963,
                "children": [
                    {"id": "Revenue Growth", "datum": 78.90833},
                    {"id": "Gross Profit", "datum": 52.0296},
                    {"id": "EBITDA", "datum": 469.9968},
                    {"id": "Net Income", "datum": 686.2849},
                ],
            },
            {
                "id": "Technology",
                "datum": 138.407475,
                "children": [
                    {"id": "Revenue Growth", "datum": 2.162382},
                    {"id": "Gross Profit", "datum": 131.5924},
                    {"id": "EBITDA", "datum": 4.652693},
                ],
            },
        ],
    }
]

# import libraries
import circlify
import matplotlib.pyplot as plt

# Compute circle positions thanks to the circlify() function
circles = circlify.circlify(
    data, show_enclosure=False, target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

# Create just a figure and only one subplot
fig, ax = plt.subplots(figsize=(8, 8))

# Title
ax.set_title("Impact by Industry")

# Remove axes
ax.axis("off")

# Find axis boundaries
lim = max(
    max(
        abs(circle.x) + circle.r,
        abs(circle.y) + circle.r,
    )
    for circle in circles
)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)

# Print circle the highest level (continents):
for circle in circles:
    if circle.level != 2:
        continue
    x, y, r = circle
    ax.add_patch(plt.Circle((x, y), r, alpha=0.5, linewidth=2, color="lightblue"))

# Print circle and labels for the highest level:
for circle in circles:
    if circle.level != 3:
        continue
    x, y, r = circle
    label = circle.ex["id"]
    ax.add_patch(plt.Circle((x, y), r, alpha=0.5, linewidth=2, color="#69b3a2"))
    plt.annotate(label, (x, y), ha="center", color="white")

# Print labels for the continents
for circle in circles:
    if circle.level != 2:
        continue
    x, y, r = circle
    label = circle.ex["id"]
    plt.annotate(
        label,
        (x, y),
        va="center",
        ha="center",
        bbox=dict(facecolor="white", edgecolor="black", boxstyle="round", pad=0.5),
    )

plt.show()
