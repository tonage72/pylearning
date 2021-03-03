with open('/home/david/programming/pylearning/message.txt', 'r') as message_file, open('/home/david/programming/pylearning/winners.txt', 'r') as winners_file:
    message = message_file.read()
    winners = winners_file.readlines()

for winner in winners:
    filename = winner.strip('\n') + '.txt'
    with open(filename, 'w') as f:
        f.write('Dear ' + winner.strip('\n') + ',\n')
        f.write(message)