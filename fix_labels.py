import os

mapping = {
    3: 0,  # white_helmet -> helmet
    6: 0,  # yellow_helmet -> helmet
    4: 0,  # wrong_helmet -> helmet
    0: 1   # no_helmet -> no_helmet
}

folders = [
    "dataset_small/train/labels",
    "dataset_small/valid/labels"
]

for folder in folders:
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        with open(path, "r") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            cls = int(parts[0])

            if cls in mapping:
                parts[0] = str(mapping[cls])
                new_lines.append(" ".join(parts) + "\n")

        with open(path, "w") as f:
            f.writelines(new_lines)

print("✅ Labels converted to helmet / no_helmet")