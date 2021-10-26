print("       ", end="")
for i in range(1, 10):
    print(f"{i:4}", end=" ")

print()
print()
for i in range(1, 10):
    print(f"{i:7}", end="")
    for j in range(1, 10):
        print(f"{i * j:4}", end=" ")
    print()

x = 1.2345667
print(f"{x:.3f}")
print(f"x{x:^40.10f}x")

# pyformat.com