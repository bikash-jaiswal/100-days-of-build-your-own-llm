# Day 3 Notes

## Topic

## Key Concepts

- Word Embeddings
    - Textual Data are not numbers - they need to be converted to numbers for mathematical operations in CPU/GPU
    - Word Embeddings are dense vectors that represent words in a continuous vector space that neural networks can process
    - **important**: Different data formats require different embedding techniques
        - Video: CNN-based embeddings
        - Audio: Spectrograms or MFCCs
        - Text: Word embeddings (Word2Vec, GloVe, etc.)
    - Embeddings for sentences, paragraphs, or whole documents.

    - **Word2Vec** trained Neural Networks architecture to generate word embeddings by predicting context of a given word given the target word or vice versa.
    - **LLMs produce their own embeddings during training** instead of using Word2Vec or similar pre-trained models as the embeddings are specific to the task at hand.

## Understanding Preprocessing steps if Stage 1
- **Preprocessing**
    1. **Tokenizing text**
        - Convert text into tokens 
        - tokens are either individual words or special characters, including punctuation characters
        - look on Day_3.ipynb for more details
    2. **Token to ID mapping**
        - Convert tokens to IDs
        - build a vocabulary of tokens and their corresponding IDs
        - Add special tokens like  <|unk|>,  <|pad|>, <|bos|>, <|eos|>,  etc.
        - look on Day_3.ipynb for more details

    3. **Byte Pair encoding**
        - sophistocated tokenization technique that combines the benefits of character-level and word-level tokenization
        - use tokenization libraries like tiktoken, sentencepiece, etc.
        - look on Day_3.ipynb for more details
        - BPE Tokenizer used by GPT-2, GPT-3, GPT-4, etc.
        - BPE Tokenizer can encode, decode any unknown word
        - it builds its vocabulary by iteratively merging frequent characters into subwords and frequent subwords into words.
- **Embeddings**
    - creating the embeddings for the LLM is to generate the input–target pairs required for training an LLM
    - simple input-target pairs (X,y) could be used by sliding window approach
        - X contains the input tokens
        - y contains the input tokens shifted by one position (next token in the sequence)
    - this will create next-word prediction task
    - The stride setting dictates the number of positions the inputs shift across batches, emulating a sliding window 
    - batch size is a tradeoff and a hyperparameter to experiment with when training LLMs.

- **Creating token embeddings**
    - Last step in preprocessing is to create token embeddings
    - Token embeddings are dense vectors that represent tokens in a continuous vector space
    - look on Day_3.ipynb for more details

## Important Details
