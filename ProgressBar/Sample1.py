from progress.bar import Bar
bar = Bar('Processing', max=20000)
for i in range(20000):
    # Do some work
    bar.next()
bar.finish()