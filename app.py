from quantum_phoenix import Phoenix

engine = Phoenix()

print("Phoenix Ignition Runtime")
print("=========================")

while not engine.is_terminal():
    engine.step("dynamo", "plates")
    print(engine)

print("Ignition complete.")
