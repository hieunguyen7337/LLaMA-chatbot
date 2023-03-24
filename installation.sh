pip install -q datasets loralib sentencepiece
pip uninstall transformers
pip install -q git+https://github.com/zphang/transformers@c3dc391
pip -q install git+https://github.com/huggingface/peft.git
pip -q install bitsandbytes