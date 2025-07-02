from transformers import pipeline

# Load summarization pipeline globally (only once)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=130, min_length=30):
    # Shorten long texts for summarization model
    if len(text.split()) > 500:
        text = " ".join(text.split()[:500])

    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
