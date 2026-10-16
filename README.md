# Anchorite-7B (it talks like shi, in dev. now)
A fine-tuned language model based on Qwen/Qwen2.5-7B.
<br> ``` /b/, /ai/, /s/ ```- from 2ch.su.
<br> only in russian language now.

## Structure

```
Anchorite-7B
├── datasets/
│   └── dataset_clean_2ch_ai.jsonl
├── pars/
│   └── pars.py                
├── LICENSE             
└── README.md                   
```
## Download and use

1.Get the `.gguf` file:
```bash
git clone https://huggingface.co/efesint/Anchorite-7B
```
2.Install llama.cpp:
```
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make
```
3. Run model with llama.cpp
```
./build/bin/llama-cli -m /home/USER/Anchorite-7B/anchorite-7b-Q4_K_M.gguf -ngl 15 -c 2048 -p "hello"
```

## Dataset

- **Name:** `dataset_clean_2ch_ai.jsonl`
- **Size:** ~ 12 000 posts
- **Source:** 2ch.su (/b/, /ai/, /s/)
- **Language:** Russian
- **License:** CC BY-SA 4.0
- **HuggingFace:** [efesint/dataset_clean_2ch_ai.jsonl](https://huggingface.co/datasets/efesint/dataset_clean_2ch_ai.jsonl)
  
# NOTICE

## Disclaimer

This software is provided "AS IS", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement.

The author is NOT responsible for any damage, data loss, moral harm, psychological distress, offense, or illegal use arising from the use or inability to use this software.

Recommended for adults aged 18 and older.
## Content Warning

This model was trained on unfiltered data from imageboards and may generate:
- Offensive language
- Hate speech
- Violent or disturbing content
- Sexually explicit material
- Misinformation

The author does not endorse, support, or condone any of the views expressed by the model.

## Usage

By using this software, you agree that:
- You are solely responsible for any content you generate.
- You will not use this software for illegal purposes.
- You will not hold the author liable for any consequences.

## License

Model weights: Apache 2.0 (based on Qwen/Qwen2.5-7B)
<br>Code: GPL v3.0
