# Description
Modern software often accepts inputs with highly complex grammars. To conduct greybox fuzzing and uncover security bugs in such software, it is essential to generate inputs that conform to the software input grammar. However, this is a well-known challenging task because it requires a deep understanding of the grammar, which is often not available and hard to infer. Recent advances in large language models (LLMs) have shown that they can be used to synthesize high-quality natural language text and code that conforms to the grammar of a given input format. Nevertheless, LLMs are often incapable or too costly to generate non-textual outputs, such as images, videos, and PDF files. This limitation hinders the application of LLMs in grammar-aware fuzzing.

This paper presents a novel approach to enabling grammar-aware fuzzing over non-textual inputs. We employ LLMs (e.g., GPT-3.5) to synthesize and further mutate input generators, often in the format of Python scripts, that generate data that conform to the grammar of a given input format. Then, non-textual data yielded by the input generators are further mutated by traditional fuzzers (e.g., AFL++) to explore the software input space more effectively. Holistically, our approach, namely G2FUZZ, features a hybrid strategy that combines a “holistic search” driven by LLMs and a “local search” driven by industrial quality fuzzers. Two key advantages of G2FUZZ are: (1) LLMs are good at synthesizing and mutating input generators and enabling jumping out of local optima, thus achieving a synergistic effect when combined with mutation-based fuzzers; (2) LLMs are less frequently invoked unless really needed, thus significantly reducing the cost of LLM usage. 



# How to use it
## lib
```
  pip install openai==1.63.2
```

## prepare the setting files
```
    cd evaluation_path
    cp path/to/G2FUZZ/openai_key.txt .
    cp path/to/G2FUZZ/program_to_format.json .
    cp path/to/G2FUZZ/model_setting.json .
```

## Step I: Run seed generation to get init output
```
python ./G2FUZZ/program_gen.py --output ./target_output --program <program_name>
```

For example:
```
python ./G2FUZZ/program_gen.py --output ./exiv2_output --program exiv2
```

## Step II: Run fuzzing
1. Construct input corpus
```
mkdir initial_seeds
cp -r seeds/* initial_seeds
cp -r output/gen_seeds initial_seeds
```

2. Run:
```
./G2FUZZ/run.sh ./G2FUZZ/afl-fuzz ./initial_seeds ./target_output ./program.cmp program_name /path/to/G2FUZZ ./program.afl
```
Note that: `./target_output` is the `--output ./target_output` in `Step I`.

For example:
./G2FUZZ/run.sh ./G2FUZZ/afl-fuzz ./initial_seeds ./exiv2_output exiv2 /evaluation/G2FUZZ_test/ ./justafl/exiv2