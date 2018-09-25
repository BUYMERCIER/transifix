import os
import sys

def transifexify(path):
    for fname in os.listdir(path + '/_i18n/'):
        if '.yml' in fname:
            full_path = path + '/_i18n/' + fname
            content = ''
            with open(full_path, 'r') as f:
                line = f.readline()
                while line:
                    content += '  ' + line # add a tab (2 spaces)
                    line = f.readline()
            with open(full_path, 'w') as f:
                locale = fname.split('.')[0] # remove file extension
                f.write(locale + ':\n' + content)
                print(locale + ':\n' + content)
        else:
            print(fname, 'is not a YAML file, skipping')


def untransifexify(path):
    for fname in os.listdir(path + '/_i18n/'):
        if '.yml' in fname:
            full_path = path + '/_i18n/' + fname
            content = ''
            with open(full_path, 'r') as f:
                line = f.readline()
                while line:
                    # remove 2 first characters of the line
                    # (the tab or 2 spaces)
                    content += line[2:]
                    line = f.readline()
            l = len(fname) - 4 # length of the filename without extension
            content = content[l::]
            with open(full_path, 'w') as f:
                f.write(content)
                print(content)
        else:
            print(fname, 'is not a YAML file, skipping')

def main():
    if len(sys.argv) < 2 or not sys.argv[1] in ['tx', 'untx']:
        print('Usage:')
        print('python transifix.py [tx|untx]')
        sys.exit()

    if sys.argv[1] == 'tx':
        path = input('Path of the bitcoincash repo: ')
        print('transifexifying')
        transifexify(path)
    elif sys.argv[1] == 'untx':
        path = input('Path of the bitcoincash repo: ')
        print('untransifexifying')
        untransifexify(path)
    print('Done')

if __name__ == '__main__':
    main()
