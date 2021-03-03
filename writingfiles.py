output_filename = '/home/david/programming/pylearning/output.txt'
with open('/home/david/programming/pylearning/data.txt', 'r') as input_file, open(output_filename, 'w') as output:
    for line in input_file:
        if line != '\n':
            output.write(line)