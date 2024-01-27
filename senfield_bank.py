greeting = input("Greeting: ").strip().lower()

# I had to cobble this together from rearch and knowing how lists work. Was there a simplier solution?
reply = []
reply = list(greeting)
indexes = reply.index("h")

if indexes == 0 and greeting != "hello" and greeting != "hello, newman":
    print("$20")
elif greeting == "hello":
    print("$0")
elif greeting == "hello, newman":
    print("$0")
else:
    print("$100")