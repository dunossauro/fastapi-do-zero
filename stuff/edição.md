# Algumas notas sobre os vídeos

Por padrão usarei a configuração tiny do [VMH](https://github.com/dunossauro/videomaker-helper).

## Iluminação

- Fundo: RGCBCW - 5 3 7 3 0
- Recorte: 1% - 2800k
- Hair: 3%
- Principal: 13% - 5600k

## Captação

- ProRes LT

Cadeia -> 4k -> Carla [isso é mesmo necessário?] -> ninja

## Audio

1. O áudio deve ser removido do vídeo sem equalização usando o vmh:

	```bash
	vmh extract-audio <video>.MOV --no-eq
	```

2. Após isso deve ser jogado na cadeira de processamento [parte manual]

audio -> noise supressor -> Mouth De-Clicker -> De-Esser -> De-Breath -> out

Sobre a cadeia:

- noise supressor: Default
- Mouth De-Clicker: 40%
- De-Esser: 60%
- De-Breath: 84%, sensibilidade 7.0

3. Render

A1: 5,02dB
A2: -4,68dB
Master: 4,29dB


## Vídeo

1. Devem ser colocados na timeline do kdenlive .MOV e o .wav e salvar o arquivo.

2. Processo de cortes com o VMH:
   ```bash
   vmh kdenlive \
	   <aula_XX>.kdenlive <video>.MOV <cuts_aula_XX>.kdenlive \
	   <eq_audio_xx>.wav -d tiny
   ```

3. Editar os cortes

4. Adicionar abertura e tela final!

5. Render: 
   - Redimensionar para 4k
   - Procurar algo no MLT para não precisar renderizar no kdenlive
