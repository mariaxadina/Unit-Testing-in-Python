import json
import subprocess

result = subprocess.run(
    ["cosmic-ray", "dump", "session.sqlite"],
    capture_output=True,
    text=True
)

for line in result.stdout.splitlines():
    line = line.strip()
    if not line:
        continue

    try:
        data = json.loads(line)
    except json.JSONDecodeError:
        continue

    # fiecare entry e listă [meta, rezultat]
    if isinstance(data, list) and len(data) == 2:
        mutation_info = data[0]
        result_info = data[1]

        if result_info.get("test_outcome") == "survived":
            mutation = mutation_info["mutations"][0]

            print("\n" + "="*60)
            print("MUTANT NEOMORÂT")
            print(f"Operator: {mutation['operator_name']}")
            print(f"Linie: {mutation['start_pos']}")

            print("\n Modificare:")
            print(result_info["diff"])