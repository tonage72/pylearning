with open('/home/david/programming/pylearning/data.txt', 'r') as file, open('/home/david/programming/pylearning/whileloops.py', 'r') as pyfile:
    for line in file:
        print(line)
    # refill the cup
    #file.seek(0)
    #for line in pyfile:
    #    print(line)