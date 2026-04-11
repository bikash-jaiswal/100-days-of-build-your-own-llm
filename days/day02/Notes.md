# Day 2 Notes

## Topic: Introduction to Transformers architecture

## Key Concepts
- Transformer architecture
    - Deep learning model architecture
    - Uses self-attention mechanism
    - consist of two modules: encoder and decoder
    - Each module contains multiple layers connected by self-attention mechanisms
    - self-attention uses weights to determine the importance of each token in a sequence of relative to each other

- encoder
     - Architecture flow: Input text → tokens → embeddings → encoder → output embeddings
     - The encoder takes the full input text
     - Embeddings are vector representations of the input texts
     - Each token is converted to a vector
     - Vectors capture semantic meaning
     - These vectors are then passed to the decoder
     
- Decoder
     - Architecture flow: Previous tokens → embeddings → decoder → next token → repeat
     - The decoder takes:
       - previously generated text tokens
       - embeddings from the encoder
     - Converts tokens into embeddings
     - Generates output one token at a time
     - Uses both past output and encoder information
     - Produces the final output text

**One-line intuition**
Encoder = understands the input and creates embeddings
Decoder = uses those embeddings to generate output step by step

```text
ENCODER
"I   love   AI"
 ↓     ↓     ↓
[emb] [emb] [emb]
 e1     e2     e3
        ↓
   Encoder processes full sentence
        ↓
Context Embeddings:
 c1     c2     c3
 (I)  (love)  (AI)
        ↓
-------------------------------
        ↓
DECODER (step-by-step)

Step 1:
Input: <start>
 ↓
[emb]
 e_start
 ↓
Decoder + (c1, c2, c3)
 ↓
Output: "J'aime"

--------------------------------

Step 2:
Input: <start>, "J'aime"
 ↓        ↓
[emb]    [emb]
 e_start  e_j'aime
 ↓
Decoder + (c1, c2, c3)
 ↓
Output: "l'"

--------------------------------

Step 3:
Input: <start>, "J'aime", "l'"
 ↓        ↓         ↓
[emb]    [emb]     [emb]
 e_start  e_j'aime  e_l'
 ↓
Decoder + (c1, c2, c3)
 ↓
Output: "IA"

--------------------------------

Step 4:
Input: <start>, "J'aime", "l'", "IA"
 ↓        ↓         ↓      ↓
[emb]    [emb]     [emb]  [emb]
 e_start  e_j'aime  e_l'  e_IA
 ↓
Decoder
 ↓
Output: <end>
```


## Transformer Architecture Variants
- Encoder-only models (e.g., BERT)
- Decoder-only models (e.g., GPT)
- Encoder-decoder models (e.g., BART, T5)

- BERT: Bidirectional Encoder Representations from Transformers
    - build on transformer encoder submodules
    - Uses bidirectional context
    - predicts masked tokens or hidden words in a given sentence
    - used for classification, sentiment analysis, document categorization, etc.
    - Twitter uses BERT to detect toxic content, spam, etc.
- GPT: Generative Pre-trained Transformer
    - build on transformer decoder submodules
    - designed for text generation
    - machine translation, text summarization, fiction writing, writing computer code, and more
    - OpenAI's GPT-3, GPT-4, and GPT-5 are examples of GPT models
    - GPT are good at zero-shot and few-shot learning tasks
    - they are autoregressive, meaning they generate text one token at a time
    - They are pre-trained on relatively simple tasks like predicting the next word in a sentence


**Zero-shot learning:** The model can perform a task it has never been explicitly trained on.

**Few-shot learning:** The model can perform a task after seeing only a few examples.

**Tokens**: a token is a unit of text that the model processes. It can be a word, a subword, or a character, depending on the tokenizer used.

**Emergent Properties**: Properties that appear in large language models that were not explicitly programmed or designed, but emerge from the model's training and architecture.

# Building Blocks of LLMs
- Stage 1:
    - Data Collection and Preprocessing
    - Attention Mechanism
    - LLM Architecture 
- Stage 2:
    - Pretraining
    - Training Loop
    - Model Evaluation
    - Load pre-trained weights
    - Fine-tuning
- Stage 3:
    - Answer Generation
    - Prompt Engineering
    - Classification
    
## Key Takeaways
1. Not all transformers are LLMs since transformers can also be used for computer vision. Also, not all LLMs are transformers, as there are LLMs based on recurrent and convolutional architectures.
2. The scale and diversity of training data significantly impact model performance.
3. LLMs can be fine-tuned for specific tasks using smaller, task-specific datasets, reducing the need for massive training data and improving performance.
4. GPT models—despite their larger yet simpler decoder-only architecture aimed at next-word prediction—exhibit emergent properties like few-shot learning and zero-shot learning.



