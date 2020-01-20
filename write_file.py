with open('testtxt', 'r') as reader:
    line=reader.readlines()
    #reversed(line)
    with open('testtxt', 'w') as writer:
        for line1 in reversed(line):
            writer.write(line1)



