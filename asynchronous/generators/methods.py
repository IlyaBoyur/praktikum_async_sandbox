def generator(start=1):
    result = start
    while True:
        yield result + result*2
        result += 1


gen_obj1 = generator()
gen_obj2 = generator()


# close
for idx in gen_obj1:
    print(idx)
    if idx > 7:
        gen_obj1.close()


# throw
try:
    for idx in gen_obj2:
        print(idx)
        if idx > 7:
            gen_obj2.throw(RuntimeError("Я всё..."))
except RuntimeError as error:
    print(f"RuntimeError: {error}")


# send
def generator_by_val(start=1):
    while True:
        start = yield start + start*2


gen_obj3 = generator_by_val(2)
print(gen_obj3.send(None))
print(gen_obj3.send(-1))
print(gen_obj3.send(3))
