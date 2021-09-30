def read_data():
    with open('image.jpg', 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))+2
        f.seek(offset)
        data = f.read().decode('ascii')
    return data

def insert_data():
    with open('image.jpg', 'ab') as f:
        print('Choose an option\n \
                1. Encode a file\n \
                2. Encode a text')
        ch = int(input('Enter choice : '))
        if ch == 1:
            file_to_encode = input('Enter file to encode : ')
            with open(file_to_encode, 'rb') as fe:
                data = fe.read()
                f.write(data)
        if ch == 2:
            data = input('Enter data to add : ')
            data += ' '
            f.write(data.encode('ascii'))

def delete_data():
    with open('image.jpg', 'rb') as f:                  
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))+2
        f.seek(0)
        original_data = f.read(offset)
                                                        
    with open('image.jpg', 'wb') as f:
        f.write(original_data)
        print('Past data has been deleted')





print('Choices available\n \
        1. Input data into image\n \
        2. Read data from image\n \
        3. Delete extra data')

choice = int(input('Enter choice : '))

if choice == 1:
    past_data = read_data()
    if past_data != '':
        print(f'Past data exists : \'{past_data}\'')
        c = input('Delete past data [y/n] : ')
        if c == 'y':
            delete_data()
            insert_data()
        else:
            insert_data()
    else:
        insert_data()
    print('Inserted data : \'', read_data(), '\'')

if choice == 2:
    print(read_data())

if choice == 3:
    delete_data()
