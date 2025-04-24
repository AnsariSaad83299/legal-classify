from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_path = "model/legal_summarization/checkpoint-2916"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

summarizer = pipeline(
    "summarization",
    model=model,
    tokenizer=tokenizer,
    device=0 if torch.cuda.is_available() else -1
)

def safe_summarize(text, max_input=512):
    try:
        inputs = tokenizer(text, return_tensors="pt", truncation=False)
        if len(inputs['input_ids'][0]) > max_input:
            print(f"Input truncated from {len(inputs['input_ids'][0])} to {max_input} tokens")
        
        summary = summarizer(
            text,
            max_length=150,
            min_length=50,
            do_sample=False,
            truncation=True,
            no_repeat_ngram_size=3
        )
        return summary[0]['summary_text']
    except Exception as e:
        return f"Summarization failed: {str(e)}"

def summarize_from_file(input_path="input.txt", output_path="output.txt"):
    with open(input_path, "r", encoding="utf-8") as f:
        input_text = f.read()

    summary = safe_summarize(input_text)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(summary)

    print("Summary written to", output_path)

# Optional CLI trigger
if __name__ == "__main__":
    summarize_from_file()
