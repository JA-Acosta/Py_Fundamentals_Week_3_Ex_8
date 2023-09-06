'''
>>> JAAR
>>> 09/06/2023
>>> Practicing Fundamentals Program 20
>>> Version 1
'''

'''
>>> Generates a program that takes an existing file, prints it to the screen then it offers the user the ability to append the file.
'''

def read_file(file_name) :
    '''
    >>> Opens a file and prints the contents to the console.
    >>> Param: (file) file_name
    '''
    with open(file_name, 'r') as file :
        contents = file.read()
        print('File Contents:')
        print(contents)

def append_file(file_name) :
    '''
    >>> Takes a user input and appends it to the end of a file.
    >>> Param: (file) file_name
    '''
    user_input = input('Enter file updates: ')
    with open(file_name, 'a') as file :
        file.write(' ' + user_input)

def response()-> str :
    '''
    >>> Asks the user to input either yes or no. Otherwise, the user will be prompted to enter another response.
    '''
    while True :
        user_input = input('Do you want to update the file?: ').lower()
        if user_input == 'yes' or user_input == 'no' :
            return user_input
        else :
            print('Your response is invalid. ', end= '')

def main() :
    file_name = 'practice_text.txt'
    read_file(file_name)
    user_response = response()
    if user_response == 'yes' :
        append_file(file_name)
        print('________________________UPDATED FILE________________________')
        read_file(file_name)
    print('\tDone!')


if __name__ == '__main__' :
    main()