# listar_nome_arquivos
Python Script que pega o nome dos arquivos de uma/s pasta/s e depois salva em um txt.

# Listar Arquivos de uma/s pasta/s

Criado com a intenção de listar todos os arquivos de um enorme diretório, porém filtrar somente nos arquivos que fossem '.mp4'.

## Como usar:

### Extensão de arquivos:
```http
  if file_name.endswith('.FILE EXTENSION'):
```
A linha acima, é totalmente opcional, caso queira filtrar por um formato de arquivos específicos, basta colocar o formato entre aspas, como é mostrado abaixo.
```http
if file_name.endswith('.mp4'):
```
Caso não queira usar, basta apagar a linha e identar a a próxima linha.

### Pastas de onde estão os arquivos a serem listados:
```http
directory_folders = ['DIRECTORIES / FOLDERS HERE']
```

Uma lista contento todas as pastas pode ser passada para essa variável.

### Arquivo txt:
```http
final_txt = os.path.expanduser('TXT TO SAVE RESULTS')
```

coloque o caminho de onde o arquivo txt está, para salvar a listagem de arquivos.
