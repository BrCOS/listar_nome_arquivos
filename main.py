import os

def itens_name(folders, final_txt):
    with open(final_txt, 'w') as save_names:
        for folder in folders:
            directory_name = os.path.basename(folder)
            save_names.write(f'Files in: {directory_name}\n')
            print(f'Files in - {directory_name}:')
            files = os.listdir(folder)
            for file_name in files:
                save_names.write(file_name + '\n')
                if file_name.endswith('.FILE EXTENSION'):
                    print(file_name)


directory_folders = ['DIRECTORIES HERE']

final_txt = os.path.expanduser('TXT TO SAVE RESULTS')
itens_name(directory_folders, final_txt)
