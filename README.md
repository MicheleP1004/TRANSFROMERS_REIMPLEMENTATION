# TRANSFROMERS_REIMPLEMENTATION

This project aims at reimplementing a simpler version of the transformer architecture proposed in the article [Attention is All You Need](https://arxiv.org/abs/1706.03762) in PyTorch.

The final objective is to understand transformer architectural bases and fundamental aspects of Machine Learning pipeline (preprocessing, training, testing, results interpretation).

## ROAD MAP

- [ ] Generate toy dataset (Italian → English)
- [ ] Tokenization and vocabulary building
- [ ] Positional Encoding implementation
- [ ] Scaled Dot-Product Attention
- [ ] Multi-Head Attention
- [ ] Encoder Layer implementation
- [ ] Decoder Layer implementation
- [ ] Complete Transformer model
- [ ] Training and evaluation of the model


## HOW TO RUN

```bash
# Environment setup
python -m venv venv
source venv/bin/activate       # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt

# Generate toy dataset
python data/generate_toy_dataset.py

# Model training
python train.py