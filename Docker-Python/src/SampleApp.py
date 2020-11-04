if __name__ == '__main__':
    file_name = 'sample_file.txt'

    with open(file_name,'w') as file_write:
        for i in range(1,11):
            file_write.write(f'{i} \n' )


    with open(file_name) as file_read:
        lines = file_read.readlines()
        for i in lines:
            print(i)




