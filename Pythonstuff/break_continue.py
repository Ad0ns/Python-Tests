# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")


# break → completely exits the loop when the condition is met.
# continue → skips only the current iteration, and moves to the next one.
# So in both cases, i == 3 never prints "Inside the loop." because:
# break skips it by exiting.
# continue skips it by jumping to the next loop iteration.


