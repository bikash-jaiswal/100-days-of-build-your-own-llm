# Day 1 Notes

## Introduction

- Traditional Deep Learning approaches for NLP
  - Excelled in many narrow tasks
    - categorization tasks eg. spam detection, sentiment analysis
    - Translation
  - Lack of context understanding and generations abilities
    - parsing and understanding text
    - generating coherent text based on context or original text or instructions
    - handling multi-turn conversations
- LLMs (Large Language Models) excelled in wide range of tasks
  - understand context and generate text based on it
  - succeeded in various domains like text generation, translation, summarization, etc.
  - can be fine-tuned for specific tasks
  - attributed to the transformer architecture
  - trained on massive amounts of text data
  - require significant computational resources for training and inference


## What is LLM?
 - Large + language + model
    - Large: trained on massive amounts of text data + models size (in billions of parameters)
    - Language: understand human language
    - Model: mathematical representation of the language
 -  parameters are the adjustable weights optimized during training to predict the next word in a sequence.

 - Architecture: transformer
    - Self-attention mechanism allows the model to weigh the importance of different words in a sequence when making predictions.
    - Parallel processing of input sequences
    - Encoder-decoder structure
