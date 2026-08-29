from quantum_phoenix import Phoenix

engine = Phoenix()

print("Step 1:")
engine.step("stress_align", "apex_stable")
print(engine)

print("Step 2:")
engine.step("stress_align", "apex_stable")
print(engine)

print("Step 3:")
engine.step("dynamo", "plates")
print(engine)

print("Continue:")
while not engine.is_terminal():
    engine.step("dynamo", "plates")
    print(engine)
