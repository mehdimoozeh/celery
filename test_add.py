from tasks import add
result = add.delay(4,5)
print(str(result.get(timeout=1)))
