from stack_mod import stack

stack_ = stack(3)

for i in range(3):
    stack_.push(f"{i+1}")

for i in range(2):
    print(stack_.pop_())

print(stack_.peek())
print(stack_.tops)