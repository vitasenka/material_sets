bom_v1_materials = ["PLA", "PETG", "PLA", "ABS"]
bom_v2_materials = ["PETG", "Nylon", "ABS", "Nylon"]

bom_v1_materials_set = set(bom_v1_materials)
bom_v2_materials_set = set(bom_v2_materials)

all_materials = bom_v1_materials_set | bom_v2_materials_set
shared_materials = bom_v1_materials_set & bom_v2_materials_set
materials_in1_not2 = bom_v1_materials_set - bom_v2_materials_set
materials_in2_not1 = bom_v2_materials_set - bom_v1_materials_set

print("All Materials:", sorted(all_materials))
print("Shared Materials:", sorted(shared_materials))
print("Only in V1:", sorted(materials_in1_not2))
print("Only in V2:", sorted(materials_in2_not1))
