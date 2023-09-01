import os

def items_name(folders, final_txt):
    with open(final_txt, 'w') as save_names:
        for folder in folders:
            directory_name = os.path.basename(folder)
            save_names.write(f'\n\nFiles in: {directory_name}\n\n')
            print(f'Files in - {directory_name}:')
            files = os.listdir(folder)
            for file_name in files:
                if file_name.endswith('.mp4'):
                    save_names.write(file_name + '\n\n')
                    print(file_name)


directory_folders = ['DIRECTORIES / FOLDERS HERE']

final_txt = os.path.expanduser('TXT TO SAVE RESULTS')
items_name(directory_folders, final_txt)
