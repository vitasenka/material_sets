from collections import Counter

bom_v1_materials = ["PLA", "PETG", "PLA", "ABS"]
bom_v2_materials = ["PETG", "Nylon", "ABS", "Nylon"]
bom_v1_materials_set = set(bom_v1_materials)
bom_v2_materials_set = set(bom_v2_materials)

all_materials = bom_v1_materials_set | bom_v2_materials_set
shared_materials = bom_v1_materials_set & bom_v2_materials_set
materials_in1_not2 = bom_v1_materials_set - bom_v2_materials_set
materials_in2_not1 = bom_v2_materials_set - bom_v1_materials_set
materials_in_exactly_one = bom_v1_materials_set ^ bom_v2_materials_set

counts_bom_v1_materials = Counter(bom_v1_materials)
counts_bom_v2_materials = Counter(bom_v2_materials)
counts_all_materials = Counter(bom_v1_materials + bom_v2_materials)

unique_in_1 = [
    material for material, count in counts_bom_v1_materials.items() if count == 1
]
unique_in_2 = [
    material for material, count in counts_bom_v2_materials.items() if count == 1
]
unique_in_total = [
    material for material, count in counts_all_materials.items() if count == 1
]


print("All Materials:", sorted(all_materials))
print("Shared Materials:", sorted(shared_materials))
print("Only in V1:", sorted(materials_in1_not2))
print("Only in V2:", sorted(materials_in2_not1))
print("Materials_in_exactly_one:", sorted(materials_in_exactly_one))
print("Unique materials in 1:", unique_in_1)
print("Unique materials in 2:", unique_in_2)
print("Unique materials in total bom:", unique_in_total)
print("distinc materials in 1", len(bom_v1_materials_set))
print("distinc materials in 2", len(bom_v2_materials_set))
print("distinc materials in 2", len(all_materials))
