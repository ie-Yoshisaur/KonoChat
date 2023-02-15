from pathlib import Path
import torch
from transformers import AutoModelForCausalLM, T5Tokenizer


def load_device():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    return device


def generate_tokenizer():
    tokenizer = T5Tokenizer.from_pretrained('rinna/japanese-gpt2-small')
    tokenizer.do_lower_case = True
    return tokenizer


def generate_model(pretrained_model_path, device):
    output = Path(pretrained_model_path)
    model = AutoModelForCausalLM.from_pretrained(output)
    model.to(device)
    model.eval()
    return model


def generate_reply(inp, device, tokenizer, model, num_gen=1):
    reply = ''
    try:
        input_text = "<s>" + str(inp) + "[SEP]"
        input_ids = tokenizer.encode(input_text, return_tensors='pt').to(device)
        out = model.generate(input_ids, do_sample=False, max_length=128, num_return_sequences=num_gen, top_p=0.975, top_k=50, bad_words_ids=[[1], [5]], no_repeat_ngram_size=0)
        reply = tokenizer.batch_decode(out)[0].split('[SEP]')[-1].replace('</s>','')
    except:
        reply = 'おにーちゃーん'
    return reply
