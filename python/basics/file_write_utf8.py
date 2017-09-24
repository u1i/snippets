import io

with io.open('test.html', encoding='utf-8', mode='w') as f:
    f.write(stuff)
    f.close()
