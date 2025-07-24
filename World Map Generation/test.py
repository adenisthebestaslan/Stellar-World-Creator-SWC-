from PIL import Image, ImageDraw
import random
import math

def generate_blob(center, radius, num_points=30, irregularity=0.3):
    """
    Generate a blob shape around a center point.

    :param center: (x, y)
    :param radius: average radius of the blob
    :param num_points: number of points in the blob's outline
    :param irregularity: how spiky or smooth the blob is (0–1)
    :return: list of (x, y) points
    """
    cx, cy = center
    angle_step = 2 * math.pi / num_points
    points = []

    for i in range(num_points):
        angle = i * angle_step
        # Perturb the radius randomly
        r = radius * (1 + random.uniform(-irregularity, irregularity))
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        points.append((x, y))

    return points

# Image setup
width, height = 400, 400
image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Generate and draw blob
blob_points = generate_blob(center=(200, 200), radius=80, irregularity=0.35)
draw.polygon(blob_points, fill=(150, 100, 255, 255))  # Purple-ish blob

# Save or show
image.show()  # or image.save("blob.png")
generate_blob()