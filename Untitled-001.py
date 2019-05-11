with open('/Users/zhutuo/Desktop/python-test/text-file-process-18zhutuo/log_files/201811113008.log', 'rb')as file:
    a=0
    for line in file:
        data = file.readline()
        data = data[26:38]
        data_str = bytes.decode(data)

        if data_str == '201811113008':
            a = a + 1

    print(a)