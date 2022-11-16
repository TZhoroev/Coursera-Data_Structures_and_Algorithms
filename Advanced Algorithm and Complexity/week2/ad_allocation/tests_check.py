import os
from subprocess import Popen, PIPE, STDOUT


def test():

    display = input('Display inputs and outputs for test cases {Yes: 1, No: 0}?')
    if display not in ['1', '0']:
        print('Did not enter valid option. Program Terminated.')
        return

    for file in os.listdir():
        if file.endswith('.py') and not file.startswith('tests_check'):
            print('\nCHECKING TEST CASES FOR FILE:  ', file)
            break

    path = './tests'
    for filename in sorted(os.listdir(path)):
        f = open(path+'/' + filename, 'r')
        content = f.read()
        if not filename.endswith('.a'):
            p = Popen(['python3', file], stdout=PIPE, stdin=PIPE, stderr=PIPE)
            test_input = content
            stdout_data = p.communicate(input=test_input.encode())[0]
        else:
            if stdout_data.decode().strip() == content.strip():
                if display == '1':
                    print('----PASSED----')
                    print('Input:  {}'.format(test_input.strip()))
                    print('Output:  {}\n'.format(content.strip()))
                pass
            else:
                print('----FAILED----')
                print('Input:  {}'.format(test_input.strip()))
                print('Output of program:  {}'.format(stdout_data.decode().strip()))
                print('Correct answer:  {}'.format(content.strip()))
                return

    print('Passed All Test Cases.')


if __name__ == '__main__':
    test()
